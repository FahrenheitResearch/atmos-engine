"""
LaTeX Report Builder for AI Agents

Provides a programmatic API for generating professional atmospheric research
reports, fire weather forecasts, case studies, and research bulletins as PDF
documents via LaTeX.

Pure Python (stdlib + subprocess for pdflatex). No external packages required.

Usage:
    from tools.agent_tools.report_builder import ReportBuilder, ReportConfig

    # Quick forecast report
    rb = ReportBuilder.forecast_template(
        title="Southern Colorado Fire Weather Forecast",
        scope="Pueblo, Fremont, and Custer Counties",
        output_dir="reports/20260209"
    )
    rb.set_abstract("Elevated fire weather conditions expected...")
    s = rb.add_section("Synoptic Analysis", "A deep upper-level trough...")
    rb.add_figure(s, "figures/wind_f12.png", "12-hr wind speed cross-section")
    rb.add_figure(s, "figures/rh_f12.png", "12-hr relative humidity cross-section")
    pdf_path = rb.compile_pdf()

    # Or build from scratch
    config = ReportConfig(title="My Report", report_type="research")
    rb = ReportBuilder(config, output_dir="reports/custom")
    rb.add_section("Introduction", "This study examines...")
    rb.save_latex()
"""
import os
import re
import subprocess
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional, Union


# =============================================================================
# pdflatex path (MiKTeX on Windows)
# =============================================================================

PDFLATEX_PATH = (
    r"C:\Users\drew\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
)


# =============================================================================
# LaTeX Helper Functions (module-level)
# =============================================================================

# Characters that have special meaning in LaTeX and need escaping.
_LATEX_SPECIAL = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}

# Regex that matches any single special character.
_LATEX_SPECIAL_RE = re.compile(
    "|".join(re.escape(k) for k in _LATEX_SPECIAL)
)


def escape_latex(text: str) -> str:
    """Escape LaTeX special characters in plain text.

    Handles: & % $ # _ { } ~ ^
    Backslashes are converted to \\textbackslash{}.

    Args:
        text: Plain text string.

    Returns:
        String safe for inclusion in LaTeX body text.
    """
    # Backslash must be handled first (before other replacements introduce
    # backslashes), and separately from the regex to avoid infinite loops.
    text = text.replace("\\", r"\textbackslash{}")
    return _LATEX_SPECIAL_RE.sub(lambda m: _LATEX_SPECIAL[m.group()], text)


def format_number(val: float, decimals: int = 1, units: str = "") -> str:
    """Format a number for LaTeX with optional units.

    Args:
        val: Numeric value.
        decimals: Decimal places (default 1).
        units: Unit string appended after a thin space (e.g. "kt", "hPa").

    Returns:
        LaTeX-formatted number string, e.g. ``"12.3\\,kt"``.
    """
    formatted = f"{val:.{decimals}f}"
    if units:
        return f"{formatted}\\,{escape_latex(units)}"
    return formatted


def risk_color_box(level: str) -> str:
    """Return a LaTeX colored box representing a risk level.

    Supported levels (case-insensitive):
        CRITICAL, HIGH, ELEVATED, MODERATE, LOW

    Args:
        level: Risk level string.

    Returns:
        LaTeX snippet producing a small colored box with bold white text.
    """
    colors = {
        "critical": ("red",       "white"),
        "high":     ("orange",    "white"),
        "elevated": ("YellowOrange", "black"),
        "moderate": ("yellow",    "black"),
        "low":      ("green",     "white"),
    }
    bg, fg = colors.get(level.strip().lower(), ("gray", "white"))
    safe = escape_latex(level.strip().upper())
    return (
        f"\\colorbox{{{bg}}}{{\\textcolor{{{fg}}}"
        f"{{\\textbf{{\\small {safe}}}}}}}"
    )


def wind_barb_latex(speed_kt: float, direction: int) -> str:
    """Return a text representation of wind speed and direction for LaTeX.

    Args:
        speed_kt: Wind speed in knots.
        direction: Meteorological wind direction in degrees (0-360).

    Returns:
        LaTeX string like ``"SW 25 kt (210)"`` with proper formatting.
    """
    cardinals = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW",
    ]
    idx = int((direction % 360 + 11.25) / 22.5) % 16
    card = cardinals[idx]
    return f"\\textbf{{{card}}} {speed_kt:.0f}\\,kt ({direction}$^\\circ$)"


def format_timestamp(cycle: str, fhr: int) -> str:
    """Convert a cycle key and forecast hour to a human-readable valid time.

    Args:
        cycle: Cycle key in ``YYYYMMDD_HHz`` format (e.g. ``"20260209_06z"``).
        fhr: Forecast hour offset.

    Returns:
        String like ``"2026-02-09 18:00 UTC (F12 from 06z)"`` safe for LaTeX.
    """
    # Parse cycle
    try:
        date_part, hour_part = cycle.split("_")
        init_hour = int(hour_part.replace("z", "").replace("Z", ""))
        year = int(date_part[:4])
        month = int(date_part[4:6])
        day = int(date_part[6:8])
        init_dt = datetime(year, month, day, init_hour, tzinfo=timezone.utc)
        from datetime import timedelta
        valid_dt = init_dt + timedelta(hours=fhr)
        valid_str = valid_dt.strftime("%Y-%m-%d %H:%M UTC")
        return f"{valid_str} (F{fhr:02d} from {init_hour:02d}z)"
    except (ValueError, IndexError):
        return f"F{fhr:02d} from {cycle}"


def table_from_dict(data: dict, caption: str = "") -> str:
    """Generate a simple two-column LaTeX table from a dictionary.

    Args:
        data: Dictionary mapping keys to values.
        caption: Optional table caption.

    Returns:
        Complete LaTeX table environment string.
    """
    lines = [
        r"\begin{table}[htbp]",
        r"\centering",
        r"\begin{tabular}{lr}",
        r"\toprule",
        r"\textbf{Parameter} & \textbf{Value} \\",
        r"\midrule",
    ]
    for k, v in data.items():
        key_safe = escape_latex(str(k))
        val_safe = escape_latex(str(v))
        lines.append(f"{key_safe} & {val_safe} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    if caption:
        lines.append(f"\\caption{{{escape_latex(caption)}}}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class Figure:
    """A figure to be included in a report section.

    Attributes:
        path: Absolute or relative path to the image file.
        caption: Figure caption text (plain text, will be escaped).
        label: LaTeX label for cross-referencing (e.g. ``fig:wind-speed``).
        width: LaTeX width specification (default ``0.95\\textwidth``).
        position: Float position specifier (default ``htbp``).
    """
    path: str
    caption: str
    label: str = ""
    width: str = "0.95\\textwidth"
    position: str = "htbp"

    def to_latex(self, output_dir: str = "") -> str:
        """Generate LaTeX for this figure.

        Args:
            output_dir: The report output directory; used to compute a
                relative path for ``\\includegraphics``.

        Returns:
            Complete LaTeX figure environment.
        """
        # Determine the image path for LaTeX.  We convert backslashes to
        # forward slashes (pdflatex on Windows accepts both, but forward
        # slashes are safer).  If the path is already relative (no drive
        # letter / root), use it directly — it was set by add_figure()
        # relative to output_dir.  Otherwise resolve against output_dir.
        if not os.path.isabs(self.path):
            img_path = self.path.replace("\\", "/")
        else:
            img_path = os.path.abspath(self.path).replace("\\", "/")
            if output_dir:
                abs_out = os.path.abspath(output_dir).replace("\\", "/")
                if img_path.startswith(abs_out):
                    img_path = img_path[len(abs_out):].lstrip("/")

        lines = [
            f"\\begin{{figure}}[{self.position}]",
            "\\centering",
            f"\\includegraphics[width={self.width}]{{{img_path}}}",
            f"\\caption{{{escape_latex(self.caption)}}}",
        ]
        if self.label:
            lines.append(f"\\label{{{self.label}}}")
        lines.append("\\end{figure}")
        return "\n".join(lines)


@dataclass
class Table:
    """A table to be included in a report section.

    Attributes:
        caption: Table caption (plain text, will be escaped).
        headers: Column header strings.
        rows: List of rows, each a list of cell strings.
        label: LaTeX label for cross-referencing.
        column_format: LaTeX column spec (e.g. ``lrrr``). Auto-generated
            from header count if empty.
    """
    caption: str
    headers: list  # list[str]
    rows: list     # list[list[str]]
    label: str = ""
    column_format: str = ""

    def to_latex(self) -> str:
        """Generate LaTeX for this table.

        Wide tables (6+ columns) are wrapped in adjustbox to prevent
        overflowing page margins.

        Returns:
            Complete LaTeX table environment with booktabs rules.
        """
        ncols = len(self.headers)
        col_fmt = self.column_format or ("l" + "r" * (ncols - 1))
        wide = ncols >= 6

        lines = [
            r"\begin{table}[htbp]",
            r"\centering",
            r"\small",
        ]
        if wide:
            lines.append(r"\begin{adjustbox}{max width=\textwidth}")
        lines.extend([
            f"\\begin{{tabular}}{{{col_fmt}}}",
            r"\toprule",
        ])
        header_row = " & ".join(
            f"\\textbf{{{escape_latex(h)}}}" for h in self.headers
        )
        lines.append(f"{header_row} \\\\")
        lines.append(r"\midrule")
        for row in self.rows:
            cells = " & ".join(escape_latex(str(c)) for c in row)
            lines.append(f"{cells} \\\\")
        lines.append(r"\bottomrule")
        lines.append(r"\end{tabular}")
        if wide:
            lines.append(r"\end{adjustbox}")
        lines.append(f"\\caption{{{escape_latex(self.caption)}}}")
        if self.label:
            lines.append(f"\\label{{{self.label}}}")
        lines.append(r"\end{table}")
        return "\n".join(lines)


@dataclass
class Section:
    """A report section with optional figures and tables.

    Attributes:
        title: Section heading text.
        content: LaTeX body content (may contain raw LaTeX commands).
        label: LaTeX label for cross-referencing.
        level: Heading level (1 = ``\\section``, 2 = ``\\subsection``,
            3 = ``\\subsubsection``).
        figures: Figures attached to this section.
        tables: Tables attached to this section.
    """
    title: str
    content: str = ""
    label: str = ""
    level: int = 1
    figures: list = field(default_factory=list)   # list[Figure]
    tables: list = field(default_factory=list)     # list[Table]

    def to_latex(self, output_dir: str = "") -> str:
        """Generate LaTeX for this section including all figures and tables.

        Args:
            output_dir: Passed through to Figure.to_latex for path resolution.

        Returns:
            LaTeX string for the complete section.
        """
        cmd = {1: "section", 2: "subsection", 3: "subsubsection"}.get(
            self.level, "section"
        )
        lines = [f"\\{cmd}{{{escape_latex(self.title)}}}"]
        if self.label:
            lines.append(f"\\label{{{self.label}}}")
        if self.content:
            lines.append("")
            lines.append(self.content)
        for fig in self.figures:
            lines.append("")
            lines.append(fig.to_latex(output_dir))
        for tbl in self.tables:
            lines.append("")
            lines.append(tbl.to_latex())
        return "\n".join(lines)


@dataclass
class ReportConfig:
    """Configuration for a LaTeX report.

    Attributes:
        title: Report title.
        author: Author line (default: AI agent attribution).
        date: Date string; auto-filled with today if empty.
        report_type: One of ``forecast``, ``case_study``, ``bulletin``,
            ``research``.
        institution: Institutional attribution line.
        confidential: If True, adds a confidential watermark.
        paper_size: LaTeX paper size (default ``letter``).
        font_size: Base font size in points (default 11).
    """
    title: str
    author: str = "AI Atmospheric Research Agent"
    date: str = ""
    report_type: str = "forecast"
    institution: str = "wxsection.com"
    confidential: bool = False
    paper_size: str = "letter"
    font_size: int = 11

    def __post_init__(self):
        if not self.date:
            self.date = datetime.now(timezone.utc).strftime("%B %d, %Y")


# =============================================================================
# ReportBuilder
# =============================================================================

class ReportBuilder:
    """Programmatic builder for LaTeX atmospheric research reports.

    Designed for AI agents: add sections, figures, and tables via method
    calls, then compile to PDF.

    Args:
        config: Report configuration.
        output_dir: Directory for generated .tex and .pdf files.
            Created automatically if it does not exist.
    """

    def __init__(self, config: ReportConfig, output_dir: str):
        self.config = config
        self.output_dir = os.path.abspath(output_dir)
        os.makedirs(self.output_dir, exist_ok=True)
        self._sections: list[Section] = []
        self._abstract: str = ""
        self._methodology: str = ""

    # -----------------------------------------------------------------
    # Section management
    # -----------------------------------------------------------------

    def _resolve_section(self, ref: Union[str, int, Section]) -> Section:
        """Resolve a section reference to a Section object.

        Args:
            ref: Section title (str), index (int), or Section object.

        Returns:
            The matching Section.

        Raises:
            KeyError: If a string title is not found.
            IndexError: If an integer index is out of range.
            TypeError: If ref is not a supported type.
        """
        if isinstance(ref, Section):
            return ref
        if isinstance(ref, int):
            return self._sections[ref]
        if isinstance(ref, str):
            for s in self._sections:
                if s.title == ref:
                    return s
            raise KeyError(f"No section with title {ref!r}")
        raise TypeError(f"Expected str, int, or Section; got {type(ref).__name__}")

    def add_section(
        self,
        title: str,
        content: str = "",
        label: str = "",
        level: int = 1,
    ) -> Section:
        """Add a new section to the report.

        Args:
            title: Section heading.
            content: LaTeX body content (raw LaTeX is fine).
            label: Cross-reference label.
            level: 1 = section, 2 = subsection, 3 = subsubsection.

        Returns:
            The created Section, so the caller can attach figures/tables.
        """
        sec = Section(title=title, content=content, label=label, level=level)
        self._sections.append(sec)
        return sec

    # -----------------------------------------------------------------
    # Figures
    # -----------------------------------------------------------------

    def add_figure(
        self,
        section: Union[str, int, Section],
        path: str,
        caption: str,
        label: str = "",
        width: str = "0.95\\textwidth",
    ) -> Figure:
        """Add a figure to an existing section.

        The image file is copied into the output directory so that pdflatex
        can find it regardless of the original file location.

        Args:
            section: Section title, index, or Section object.
            path: File path to the image (PNG, PDF, JPG).
            caption: Figure caption (plain text).
            label: LaTeX label for cross-referencing.
            width: LaTeX width spec.

        Returns:
            The created Figure object.
        """
        sec = self._resolve_section(section)
        # Copy the image into output_dir/figures/ so pdflatex can find it.
        fig_dir = os.path.join(self.output_dir, "figures")
        os.makedirs(fig_dir, exist_ok=True)
        basename = os.path.basename(path)
        dest = os.path.join(fig_dir, basename)
        abs_src = os.path.abspath(path)
        if abs_src != os.path.abspath(dest) and os.path.isfile(abs_src):
            shutil.copy2(abs_src, dest)
        # Use the relative path from output_dir for LaTeX.
        rel_path = f"figures/{basename}"
        fig = Figure(path=rel_path, caption=caption, label=label, width=width)
        sec.figures.append(fig)
        return fig

    def add_figure_grid(
        self,
        section: Union[str, int, Section],
        figures: list,  # list[dict] with keys: path, caption, (optional) label
        caption: str,
        ncols: int = 2,
        label: str = "",
    ) -> str:
        """Add a multi-panel figure grid using subfigures.

        Each panel is a subfigure within a single figure environment.
        Image files are copied into the output directory.

        Args:
            section: Section title, index, or Section object.
            figures: List of dicts with keys ``path``, ``caption``, and
                optionally ``label``.
            caption: Overall figure caption.
            ncols: Number of columns in the grid (default 2).
            label: LaTeX label for the overall figure.

        Returns:
            The generated LaTeX string (also appended to section content).
        """
        sec = self._resolve_section(section)
        fig_dir = os.path.join(self.output_dir, "figures")
        os.makedirs(fig_dir, exist_ok=True)

        sub_width = f"{0.95 / ncols:.2f}\\textwidth"
        lines = [
            r"\begin{figure}[htbp]",
            r"\centering",
        ]
        for i, fd in enumerate(figures):
            src = fd["path"]
            basename = os.path.basename(src)
            dest = os.path.join(fig_dir, basename)
            abs_src = os.path.abspath(src)
            if abs_src != os.path.abspath(dest) and os.path.isfile(abs_src):
                shutil.copy2(abs_src, dest)
            rel_path = f"figures/{basename}"

            lines.append(f"\\begin{{subfigure}}[t]{{{sub_width}}}")
            lines.append("\\centering")
            lines.append(
                f"\\includegraphics[width=\\textwidth]{{{rel_path}}}"
            )
            sub_cap = escape_latex(fd.get("caption", ""))
            lines.append(f"\\caption{{{sub_cap}}}")
            sub_label = fd.get("label", "")
            if sub_label:
                lines.append(f"\\label{{{sub_label}}}")
            lines.append(r"\end{subfigure}")
            # Add horizontal spacing between columns, newline between rows.
            if (i + 1) % ncols == 0 and (i + 1) < len(figures):
                lines.append("")  # new row
            elif (i + 1) < len(figures):
                lines.append(r"\hfill")

        lines.append(f"\\caption{{{escape_latex(caption)}}}")
        if label:
            lines.append(f"\\label{{{label}}}")
        lines.append(r"\end{figure}")

        latex = "\n".join(lines)
        sec.content = (sec.content + "\n\n" + latex) if sec.content else latex
        return latex

    # -----------------------------------------------------------------
    # Tables
    # -----------------------------------------------------------------

    def add_table(
        self,
        section: Union[str, int, Section],
        caption: str,
        headers: list,  # list[str]
        rows: list,     # list[list[str]]
        label: str = "",
    ) -> Table:
        """Add a table to an existing section.

        Args:
            section: Section title, index, or Section object.
            caption: Table caption.
            headers: Column header strings.
            rows: List of row data (each row is a list of strings).
            label: LaTeX label.

        Returns:
            The created Table object.
        """
        sec = self._resolve_section(section)
        tbl = Table(
            caption=caption, headers=headers, rows=rows, label=label
        )
        sec.tables.append(tbl)
        return tbl

    # -----------------------------------------------------------------
    # Special content blocks
    # -----------------------------------------------------------------

    def add_alert_box(self, text: str, color: str = "red", title: str = "ALERT") -> str:
        """Generate LaTeX for a colored alert box.

        Uses ``tcolorbox`` for a professional look. The returned string can
        be inserted into any section's content.

        Args:
            text: Alert body text (plain text, will be escaped).
            color: Box color name (LaTeX color, e.g. ``red``, ``orange``).
            title: Box title (default ``ALERT``).

        Returns:
            LaTeX tcolorbox snippet.
        """
        return (
            f"\\begin{{tcolorbox}}["
            f"colback={color}!10, colframe={color}!80!black, "
            f"title={{\\textbf{{{escape_latex(title)}}}}}]\n"
            f"{escape_latex(text)}\n"
            f"\\end{{tcolorbox}}"
        )

    def add_key_finding(self, text: str) -> str:
        """Generate LaTeX for a highlighted key finding.

        Produces a tcolorbox with a blue theme suitable for emphasizing
        important conclusions or observations.

        Args:
            text: Key finding text (plain text, will be escaped).

        Returns:
            LaTeX tcolorbox snippet.
        """
        return (
            r"\begin{tcolorbox}["
            r"colback=blue!5, colframe=blue!60!black, "
            r"title={\textbf{Key Finding}}]" "\n"
            f"{escape_latex(text)}\n"
            r"\end{tcolorbox}"
        )

    # -----------------------------------------------------------------
    # Abstract / Methodology
    # -----------------------------------------------------------------

    def set_abstract(self, text: str) -> None:
        """Set the report abstract.

        Args:
            text: Abstract text (plain text, will be escaped).
        """
        self._abstract = text

    def set_methodology(self, text: str) -> None:
        """Set a methodology section that appears after the abstract.

        Only applies to ``case_study`` and ``research`` report types.

        Args:
            text: Methodology description (plain text, will be escaped).
        """
        self._methodology = text

    # -----------------------------------------------------------------
    # LaTeX generation
    # -----------------------------------------------------------------

    def _preamble(self) -> str:
        """Generate the LaTeX document preamble."""
        cfg = self.config
        lines = [
            f"\\documentclass[{cfg.font_size}pt, {cfg.paper_size}paper]{{article}}",
            "",
            "% --- Encoding and fonts ---",
            r"\usepackage[utf8]{inputenc}",
            r"\usepackage[T1]{fontenc}",
            r"\usepackage{lmodern}",
            "",
            "% --- Page layout ---",
            r"\usepackage[margin=1in]{geometry}",
            r"\usepackage{setspace}",
            r"\onehalfspacing",
            "",
            "% --- Graphics and color ---",
            r"\usepackage{graphicx}",
            r"\usepackage[dvipsnames]{xcolor}",
            r"\usepackage{subcaption}",
            "",
            "% --- Tables ---",
            r"\usepackage{booktabs}",
            r"\usepackage{array}",
            r"\usepackage{tabularx}",
            r"\usepackage{adjustbox}",
            "",
            "% --- Headers and footers ---",
            r"\usepackage{fancyhdr}",
            r"\pagestyle{fancy}",
            r"\fancyhf{}",
            f"\\lhead{{\\small {escape_latex(cfg.institution)}}}",
            f"\\rhead{{\\small {escape_latex(cfg.title[:60])}}}",
            r"\cfoot{\thepage}",
            r"\renewcommand{\headrulewidth}{0.4pt}",
            "",
            "% --- Alert/callout boxes ---",
            r"\usepackage{tcolorbox}",
            "",
            "% --- Hyperlinks ---",
            r"\usepackage[colorlinks=true, linkcolor=blue!70!black, "
            r"urlcolor=blue!70!black, citecolor=blue!70!black]{hyperref}",
            "",
            "% --- Misc ---",
            r"\usepackage{enumitem}",
            r"\usepackage{parskip}",
        ]

        if cfg.confidential:
            lines.extend([
                "",
                "% --- Confidential watermark ---",
                r"\usepackage{draftwatermark}",
                r"\SetWatermarkText{CONFIDENTIAL}",
                r"\SetWatermarkScale{0.5}",
                r"\SetWatermarkColor[gray]{0.9}",
            ])

        # Report type styling.
        type_colors = {
            "forecast":   "red!70!black",
            "case_study": "blue!70!black",
            "bulletin":   "orange!80!black",
            "research":   "black",
        }
        title_color = type_colors.get(cfg.report_type, "black")

        type_labels = {
            "forecast":   "FORECAST",
            "case_study": "CASE STUDY",
            "bulletin":   "BULLETIN",
            "research":   "RESEARCH REPORT",
        }
        type_label = type_labels.get(cfg.report_type, "REPORT")

        lines.extend([
            "",
            "% --- Title configuration ---",
            f"\\newcommand{{\\reporttypecolor}}{{{title_color}}}",
            f"\\newcommand{{\\reporttypelabel}}{{{type_label}}}",
            "",
            r"\title{"
            r"\textcolor{\reporttypecolor}{"
            r"\large\textsc{\reporttypelabel}\\[0.3em]"
            f"\\LARGE\\textbf{{{escape_latex(cfg.title)}}}"
            r"}}",
            f"\\author{{{escape_latex(cfg.author)}}}",
            f"\\date{{{escape_latex(cfg.date)}}}",
        ])

        return "\n".join(lines)

    def generate_latex(self) -> str:
        """Assemble the complete LaTeX document source.

        Combines preamble, title page, abstract, methodology, all sections
        (with their figures and tables), and closing.

        Returns:
            Complete LaTeX document as a string.
        """
        parts = [self._preamble(), "", r"\begin{document}", ""]

        # Title
        parts.append(r"\maketitle")
        if self.config.confidential:
            parts.append(
                r"\begin{center}\textcolor{red}{\textbf{"
                r"CONFIDENTIAL --- DO NOT DISTRIBUTE}}\end{center}"
            )
        parts.append(r"\thispagestyle{fancy}")
        parts.append("")

        # Abstract
        if self._abstract:
            parts.extend([
                r"\begin{abstract}",
                escape_latex(self._abstract),
                r"\end{abstract}",
                "",
            ])

        # Table of contents for longer report types.
        if self.config.report_type in ("case_study", "research"):
            parts.extend([r"\tableofcontents", r"\newpage", ""])

        # Methodology (for case_study and research)
        if self._methodology and self.config.report_type in (
            "case_study", "research"
        ):
            parts.extend([
                r"\section{Data \& Methodology}",
                escape_latex(self._methodology),
                "",
            ])

        # Sections
        for sec in self._sections:
            parts.append(sec.to_latex(self.output_dir))
            parts.append("")

        # Footer attribution
        parts.extend([
            r"\vfill",
            r"\begin{center}",
            r"\small\textit{Generated by wxsection.com AI Atmospheric "
            r"Research Agent}",
            r"\end{center}",
            "",
            r"\end{document}",
        ])

        return "\n".join(parts)

    # -----------------------------------------------------------------
    # Output
    # -----------------------------------------------------------------

    def save_latex(self, filename: str = "main.tex") -> str:
        """Save the LaTeX source to a file in the output directory.

        Args:
            filename: Output filename (default ``main.tex``).

        Returns:
            Absolute path to the saved ``.tex`` file.
        """
        tex_path = os.path.join(self.output_dir, filename)
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(self.generate_latex())
        return tex_path

    def compile_pdf(self, passes: int = 2, filename: str = "main.tex") -> str:
        """Compile the LaTeX source to PDF using pdflatex.

        Saves the ``.tex`` file first, then runs pdflatex the requested
        number of passes (2 by default, which is sufficient for TOC and
        cross-references to resolve).

        Args:
            passes: Number of pdflatex passes (default 2).
            filename: TeX filename (default ``main.tex``).

        Returns:
            Absolute path to the compiled PDF file.

        Raises:
            FileNotFoundError: If pdflatex is not found at the expected path.
            RuntimeError: If pdflatex returns a non-zero exit code.
        """
        if not os.path.isfile(PDFLATEX_PATH):
            raise FileNotFoundError(
                f"pdflatex not found at {PDFLATEX_PATH}. "
                f"Install MiKTeX or update PDFLATEX_PATH."
            )

        tex_path = self.save_latex(filename)

        for i in range(passes):
            result = subprocess.run(
                [PDFLATEX_PATH, "-interaction=nonstopmode", "-halt-on-error",
                 filename],
                cwd=self.output_dir,
                capture_output=True,
                text=True,
                timeout=120,
            )
            if result.returncode != 0:
                # Save the log for debugging.
                log_path = os.path.join(
                    self.output_dir, filename.replace(".tex", ".log")
                )
                raise RuntimeError(
                    f"pdflatex pass {i + 1}/{passes} failed "
                    f"(exit code {result.returncode}). "
                    f"Check log: {log_path}\n"
                    f"stderr: {result.stderr[:500]}\n"
                    f"stdout (last 500 chars): {result.stdout[-500:]}"
                )

        pdf_path = os.path.join(
            self.output_dir, filename.replace(".tex", ".pdf")
        )
        if not os.path.isfile(pdf_path):
            raise RuntimeError(
                f"pdflatex completed but PDF not found at {pdf_path}"
            )
        return pdf_path

    # -----------------------------------------------------------------
    # Template class methods
    # -----------------------------------------------------------------

    @classmethod
    def forecast_template(
        cls,
        title: str,
        scope: str,
        output_dir: str,
        **config_kwargs,
    ) -> "ReportBuilder":
        """Create a report pre-configured for fire weather forecasts.

        Includes standard forecast sections: Situation Overview, Synoptic
        Analysis, Mesoscale Analysis, Fire Weather Assessment, Forecast
        Discussion, and Recommendations.

        Args:
            title: Forecast title.
            scope: Geographic scope description (inserted into the Situation
                Overview section).
            output_dir: Output directory.
            **config_kwargs: Extra keyword arguments forwarded to ReportConfig.

        Returns:
            A ReportBuilder with pre-populated sections.
        """
        config = ReportConfig(
            title=title,
            report_type="forecast",
            **config_kwargs,
        )
        rb = cls(config, output_dir)

        rb.add_section(
            "Situation Overview",
            content=(
                f"This forecast covers {escape_latex(scope)}. "
                "Conditions are assessed using HRRR model cross-section "
                "analysis via wxsection.com."
            ),
            label="sec:overview",
        )
        rb.add_section(
            "Synoptic Analysis",
            content="% Add synoptic-scale discussion here.",
            label="sec:synoptic",
        )
        rb.add_section(
            "Mesoscale Analysis",
            content="% Add mesoscale discussion here.",
            label="sec:mesoscale",
        )
        rb.add_section(
            "Fire Weather Assessment",
            content="% Add fire weather thresholds and assessment here.",
            label="sec:fire-wx",
        )
        rb.add_section(
            "Forecast Discussion",
            content="% Add forecast details, timing, and confidence here.",
            label="sec:forecast",
        )
        rb.add_section(
            "Recommendations",
            content="% Add operational recommendations here.",
            label="sec:recommendations",
        )
        return rb

    @classmethod
    def case_study_template(
        cls,
        event_name: str,
        date: str,
        output_dir: str,
        **config_kwargs,
    ) -> "ReportBuilder":
        """Create a report pre-configured for historical event case studies.

        Includes sections for: Event Overview, Data & Methodology, Synoptic
        Environment, Mesoscale Analysis, Temporal Evolution, Cross-Section
        Analysis, Ground Truth Comparison, and Conclusions.

        Args:
            event_name: Name of the weather event.
            date: Event date string (e.g. ``"2026-02-09"``).
            output_dir: Output directory.
            **config_kwargs: Extra keyword arguments forwarded to ReportConfig.

        Returns:
            A ReportBuilder with pre-populated sections.
        """
        config = ReportConfig(
            title=f"Case Study: {event_name}",
            report_type="case_study",
            **config_kwargs,
        )
        rb = cls(config, output_dir)

        rb.add_section(
            "Event Overview",
            content=(
                f"This case study examines the {escape_latex(event_name)} "
                f"event of {escape_latex(date)}."
            ),
            label="sec:overview",
        )
        # Note: Data & Methodology is handled via set_methodology() and
        # generated automatically in generate_latex().  We add a placeholder
        # prompt here so the agent knows to call set_methodology().
        rb.add_section(
            "Synoptic Environment",
            content="% Describe the large-scale atmospheric pattern.",
            label="sec:synoptic",
        )
        rb.add_section(
            "Mesoscale Analysis",
            content="% Describe mesoscale features driving the event.",
            label="sec:mesoscale",
        )
        rb.add_section(
            "Temporal Evolution",
            content="% Describe how the event evolved over time.",
            label="sec:temporal",
        )
        rb.add_section(
            "Cross-Section Analysis",
            content=(
                "% Insert wxsection.com cross-section figures and analysis."
            ),
            label="sec:xsect",
        )
        rb.add_section(
            "Ground Truth Comparison",
            content=(
                "% Compare model data with observations (METAR, RAWS, etc.)."
            ),
            label="sec:ground-truth",
        )
        rb.add_section(
            "Conclusions",
            content="% Summarize findings and lessons learned.",
            label="sec:conclusions",
        )
        return rb

    @classmethod
    def bulletin_template(
        cls,
        title: str,
        output_dir: str,
        **config_kwargs,
    ) -> "ReportBuilder":
        """Create a short-form 1--2 page bulletin.

        Includes an alert box placeholder at the top, Key Findings,
        Discussion, and Action Items sections.

        Args:
            title: Bulletin title.
            output_dir: Output directory.
            **config_kwargs: Extra keyword arguments forwarded to ReportConfig.

        Returns:
            A ReportBuilder with pre-populated sections.
        """
        config = ReportConfig(
            title=title,
            report_type="bulletin",
            font_size=11,
            **config_kwargs,
        )
        rb = cls(config, output_dir)

        # The alert section starts with a placeholder tcolorbox.
        alert_latex = rb.add_alert_box(
            "Replace this placeholder with the specific alert text.",
            color="red",
            title="WEATHER ALERT",
        )
        rb.add_section(
            "Alert",
            content=alert_latex,
            label="sec:alert",
        )
        rb.add_section(
            "Key Findings",
            content="% Use add\\_key\\_finding() to populate this section.",
            label="sec:findings",
        )
        rb.add_section(
            "Discussion",
            content="% Brief technical discussion.",
            label="sec:discussion",
        )
        rb.add_section(
            "Action Items",
            content=(
                r"\begin{itemize}[leftmargin=*]" "\n"
                r"\item Replace with specific action items." "\n"
                r"\end{itemize}"
            ),
            label="sec:actions",
        )
        return rb

    # -----------------------------------------------------------------
    # Repr
    # -----------------------------------------------------------------

    def __repr__(self) -> str:
        n_figs = sum(len(s.figures) for s in self._sections)
        n_tbls = sum(len(s.tables) for s in self._sections)
        return (
            f"<ReportBuilder "
            f"type={self.config.report_type!r} "
            f"sections={len(self._sections)} "
            f"figures={n_figs} "
            f"tables={n_tbls} "
            f"dir={self.output_dir!r}>"
        )
