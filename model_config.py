#!/usr/bin/env python3
"""
Weather Model Configuration System — Single Source of Truth

All model-specific constants (FHR lists, availability lags, GRIB patterns,
pressure levels, cycle retention, excluded styles) live here. auto_update.py
and unified_dashboard.py import from this module instead of defining their own.
"""

import os
from dataclasses import dataclass, field
from typing import Dict, FrozenSet, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Module-level constants
# ---------------------------------------------------------------------------

SYNOPTIC_HOURS: FrozenSet[int] = frozenset({0, 6, 12, 18})


@dataclass
class ModelConfig:
    """Configuration for a weather model"""

    name: str
    full_name: str
    resolution: str

    # File naming patterns
    file_types: Dict[str, str]  # Maps generic names to model-specific names
    filename_pattern: str  # Pattern for constructing filenames

    # Download sources in priority order
    download_sources: List[str]

    # Forecast configuration
    forecast_cycles: List[int]  # UTC hours when model runs
    max_forecast_hours: Dict[int, int]  # Max forecast hours by cycle

    # Grid information
    grid_type: str
    domain: str

    # Variable name mappings (if different from HRRR)
    variable_mappings: Optional[Dict[str, str]] = None

    # --- NEW: FHR lists (the canonical source for what FHRs exist) ---------
    # Base FHR list: used for non-extended cycles (and as download-priority
    # boundary — base FHRs are downloaded first for every cycle).
    base_fhr_list: Optional[List[int]] = None

    # Extended cycle hours: cycle hours that have longer forecasts.
    # None means all cycles use the same FHR list (base_fhr_list).
    extended_cycle_hours: Optional[FrozenSet[int]] = None

    # Extended FHR list: full FHR list for extended cycles.
    # Only used when extended_cycle_hours is set.
    extended_fhr_list: Optional[List[int]] = None

    # --- NEW: Availability & download config -------------------------------
    # Minutes after init time before first FHR is typically published.
    # Overridable via env vars XSECT_LAG_{MODEL}_MIN.
    availability_lag_minutes: int = 50

    # GRIB glob patterns that confirm a complete FHR download
    grib_required_patterns: Optional[List[str]] = None

    # Which file_types to request from the download orchestrator
    # (e.g. ['pressure', 'surface'] for HRRR, ['pressure'] for GFS)
    grib_file_types: Optional[List[str]] = None

    # Whether model has a separate surface file (only HRRR)
    needs_separate_sfc: bool = False

    # --- NEW: Dashboard display config -------------------------------------
    # Minimum expected pressure levels (for GRIB validation)
    min_pressure_levels: int = 40

    # Cross-section styles NOT available for this model
    excluded_styles: Optional[Set[str]] = None

    # Cycle retention policy
    synoptic_cycles_to_keep: int = 0  # 0 = no synoptic retention concept
    hourly_cycles_to_keep: int = 2  # non-synoptic cycles to keep in preload

    # -----------------------------------------------------------------------
    # Methods
    # -----------------------------------------------------------------------

    def get_fhr_list(self, cycle_hour: int = None) -> List[int]:
        """Return the complete FHR list for a given cycle hour.

        This is the single source of truth for which FHRs exist for a model+cycle.
        Handles sparse FHR lists (GFS 3h/6h, NAM hourly/3-hourly, RRFS gap at F60).
        """
        if (cycle_hour is not None
                and self.extended_cycle_hours
                and cycle_hour in self.extended_cycle_hours
                and self.extended_fhr_list is not None):
            return list(self.extended_fhr_list)
        return list(self.base_fhr_list) if self.base_fhr_list else list(range(19))

    def get_extended_only_fhrs(self) -> List[int]:
        """Return FHRs that are ONLY in the extended list (beyond base).

        Used by auto_update to queue extended FHRs at lower priority.
        Returns empty list if model has no extended cycles.
        """
        if not self.extended_fhr_list or not self.base_fhr_list:
            return []
        base_set = set(self.base_fhr_list)
        return [f for f in self.extended_fhr_list if f not in base_set]

    def is_extended_cycle(self, cycle_hour: int) -> bool:
        """Check if this cycle hour has extended (longer) forecasts."""
        if self.extended_cycle_hours is None:
            return False
        return cycle_hour in self.extended_cycle_hours

    def has_extended_cycles(self) -> bool:
        """Check if this model has any extended cycles at all."""
        return (self.extended_cycle_hours is not None
                and self.extended_fhr_list is not None)

    def get_filename(self, cycle_hour: int, file_type: str,
                     forecast_hour: int, domain: str = None) -> str:
        """Generate filename for this model"""
        model_file_type = self.file_types.get(file_type, file_type)
        filename = self.filename_pattern.format(
            hour=cycle_hour,
            file_type=model_file_type,
            forecast_hour=forecast_hour
        )

        # Handle RRFS domain variations
        if self.name == 'rrfs' and domain:
            if domain == 'conus':
                pass
            elif domain == 'na':
                filename = filename.replace('.conus', '.na')
            elif domain in ['ak', 'hi', 'pr']:
                filename = filename.replace('.3km', '.2p5km').replace('.conus', f'.{domain}')

        return filename

    def get_download_urls(self, date_str: str, cycle_hour: int, file_type: str,
                         forecast_hour: int, domain: str = 'conus') -> List[str]:
        """Get download URLs for this model"""
        filename = self.get_filename(cycle_hour, file_type, forecast_hour, domain)
        urls = []

        for source_pattern in self.download_sources:
            hour_str = f"{cycle_hour:02d}" if isinstance(cycle_hour, int) else cycle_hour
            url = source_pattern.format(
                date=date_str,
                hour=hour_str,
                filename=filename
            )
            urls.append(url)

        return urls

    def get_max_forecast_hour(self, cycle_hour: int) -> int:
        """Get maximum forecast hour for a given cycle.

        Derives from FHR lists when available, falls back to max_forecast_hours dict.
        """
        fhr_list = self.get_fhr_list(cycle_hour)
        if fhr_list:
            return fhr_list[-1]
        return self.max_forecast_hours.get(cycle_hour, 18)

    def is_valid_cycle(self, cycle_hour: int) -> bool:
        """Check if this is a valid cycle hour for the model"""
        return cycle_hour in self.forecast_cycles


# ---------------------------------------------------------------------------
# Model Registry
# ---------------------------------------------------------------------------

class ModelRegistry:
    """Registry of available weather models"""

    def __init__(self):
        self.models = self._initialize_models()

    def _initialize_models(self) -> Dict[str, ModelConfig]:
        models = {}

        # === HRRR ===
        models['hrrr'] = ModelConfig(
            name='hrrr',
            full_name='High-Resolution Rapid Refresh',
            resolution='3km',
            file_types={
                'pressure': 'wrfprs',
                'surface': 'wrfsfc',
                'native': 'wrfnat'
            },
            filename_pattern='hrrr.t{hour:02d}z.{file_type}f{forecast_hour:02d}.grib2',
            download_sources=[
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/hrrr/prod/hrrr.{date}/conus/{filename}',
                'https://noaa-hrrr-bdp-pds.s3.amazonaws.com/hrrr.{date}/conus/{filename}',
                'https://pando-rgw01.chpc.utah.edu/hrrr/hrrr.{date}/conus/{filename}'
            ],
            forecast_cycles=list(range(24)),
            max_forecast_hours={
                0: 48, 6: 48, 12: 48, 18: 48,
                **{h: 18 for h in range(24) if h not in [0, 6, 12, 18]}
            },
            grid_type='lambert_conformal',
            domain='conus',
            # FHR lists
            base_fhr_list=list(range(19)),                  # F00-F18 hourly
            extended_cycle_hours=SYNOPTIC_HOURS,            # 00/06/12/18z
            extended_fhr_list=list(range(49)),               # F00-F48 hourly
            # Availability & download
            availability_lag_minutes=int(os.environ.get('XSECT_LAG_HRRR_MIN', '50')),
            grib_required_patterns=['*wrfprs*.grib2', '*wrfsfc*.grib2'],
            grib_file_types=['pressure', 'surface'],
            needs_separate_sfc=True,
            # Dashboard
            min_pressure_levels=40,
            excluded_styles=set(),
            synoptic_cycles_to_keep=2,
            hourly_cycles_to_keep=3,
        )

        # === RRFS ===
        models['rrfs'] = ModelConfig(
            name='rrfs',
            full_name='Rapid Refresh Forecast System',
            resolution='3km',
            file_types={
                'pressure': 'prslev',
                'surface': 'prslev',
                'native': 'natlev'
            },
            filename_pattern='rrfs.t{hour:02d}z.{file_type}.3km.f{forecast_hour:03d}.conus.grib2',
            download_sources=[
                'https://noaa-rrfs-pds.s3.amazonaws.com/rrfs_a/rrfs.{date}/{hour}/{filename}',
                'https://s3.amazonaws.com/noaa-rrfs-pds/rrfs_a/rrfs.{date}/{hour}/{filename}'
            ],
            forecast_cycles=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18, 21],
            max_forecast_hours={
                0: 84, 6: 84, 12: 84, 18: 84,
                **{h: 18 for h in [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 15, 21]}
            },
            grid_type='rotated_lat_lon',
            domain='north_america',
            variable_mappings={},
            # FHR lists — synoptic: F00-F60 hourly + F63-F84 3-hourly
            base_fhr_list=list(range(19)),
            extended_cycle_hours=SYNOPTIC_HOURS,
            extended_fhr_list=list(range(61)) + list(range(63, 85, 3)),
            # Availability & download
            availability_lag_minutes=int(os.environ.get('XSECT_LAG_RRFS_MIN', '0')),
            grib_required_patterns=['*prslev*.grib2'],
            grib_file_types=['pressure'],
            needs_separate_sfc=False,
            # Dashboard
            min_pressure_levels=40,
            excluded_styles={'smoke'},
            synoptic_cycles_to_keep=1,
            hourly_cycles_to_keep=1,
        )

        # === GFS ===
        # 0.25deg pgrb2: F00-F120 available hourly (we grab every 3h),
        # F123-F384 available every 3h (we grab every 6h for disk savings).
        models['gfs'] = ModelConfig(
            name='gfs',
            full_name='Global Forecast System',
            resolution='0.25deg',
            file_types={
                'pressure': 'pgrb2.0p25',
                'surface': 'pgrb2.0p25',
                'pressure_b': 'pgrb2b.0p25'
            },
            filename_pattern='gfs.t{hour:02d}z.{file_type}.f{forecast_hour:03d}',
            download_sources=[
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.{date}/{hour}/atmos/{filename}',
                'https://ftpprd.ncep.noaa.gov/data/nccf/com/gfs/prod/gfs.{date}/{hour}/atmos/{filename}'
            ],
            forecast_cycles=[0, 6, 12, 18],
            max_forecast_hours={0: 384, 6: 384, 12: 384, 18: 384},
            grid_type='latlon',
            domain='global',
            # FHR list: 3-hourly to F120, 6-hourly F126-F384 (all cycles same)
            base_fhr_list=list(range(0, 121, 3)) + list(range(126, 385, 6)),
            extended_cycle_hours=None,
            extended_fhr_list=None,
            # Availability & download
            availability_lag_minutes=int(os.environ.get('XSECT_LAG_GFS_MIN', '180')),
            grib_required_patterns=['*pgrb2.0p25*'],
            grib_file_types=['pressure'],
            needs_separate_sfc=False,
            # Dashboard
            min_pressure_levels=20,
            excluded_styles={'smoke'},
            synoptic_cycles_to_keep=0,
            hourly_cycles_to_keep=2,
        )

        # === NAM 12km ===
        models['nam'] = ModelConfig(
            name='nam',
            full_name='North American Mesoscale',
            resolution='12km',
            file_types={
                'pressure': 'awphys',
                'surface': 'awphys',
            },
            filename_pattern='nam.t{hour:02d}z.{file_type}{forecast_hour:02d}.tm00.grib2',
            download_sources=[
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nam/prod/nam.{date}/{filename}',
                'https://noaa-nam-pds.s3.amazonaws.com/nam.{date}/{filename}',
            ],
            forecast_cycles=[0, 6, 12, 18],
            max_forecast_hours={0: 84, 6: 84, 12: 84, 18: 84},
            grid_type='lambert_conformal',
            domain='conus',
            # FHR list: hourly to F36, 3-hourly F39-F84 (all cycles same)
            base_fhr_list=list(range(37)) + list(range(39, 85, 3)),
            extended_cycle_hours=None,
            extended_fhr_list=None,
            # Availability & download
            availability_lag_minutes=int(os.environ.get('XSECT_LAG_NAM_MIN', '90')),
            grib_required_patterns=['*awphys*.grib2'],
            grib_file_types=['pressure'],
            needs_separate_sfc=False,
            # Dashboard
            min_pressure_levels=30,
            excluded_styles={'smoke', 'q', 'moisture_transport', 'cloud_total', 'icing',
                             'dewpoint_dep', 'vorticity', 'pv'},
            synoptic_cycles_to_keep=0,
            hourly_cycles_to_keep=2,
        )

        # === RAP 13km ===
        models['rap'] = ModelConfig(
            name='rap',
            full_name='Rapid Refresh',
            resolution='13km',
            file_types={
                'pressure': 'awp130pgrb',
                'surface': 'awp130pgrb',
            },
            filename_pattern='rap.t{hour:02d}z.{file_type}f{forecast_hour:02d}.grib2',
            download_sources=[
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/rap/prod/rap.{date}/{filename}',
                'https://noaa-rap-pds.s3.amazonaws.com/rap.{date}/{filename}',
            ],
            forecast_cycles=list(range(24)),
            max_forecast_hours={
                3: 51, 9: 51, 15: 51, 21: 51,
                **{h: 21 for h in range(24) if h not in [3, 9, 15, 21]}
            },
            grid_type='lambert_conformal',
            domain='conus',
            # FHR lists — extended cycles (03/09/15/21z) go to F51
            base_fhr_list=list(range(22)),               # F00-F21 hourly
            extended_cycle_hours=frozenset({3, 9, 15, 21}),
            extended_fhr_list=list(range(52)),            # F00-F51 hourly
            # Availability & download
            availability_lag_minutes=int(os.environ.get('XSECT_LAG_RAP_MIN', '50')),
            grib_required_patterns=['*awp130pgrb*.grib2'],
            grib_file_types=['pressure'],
            needs_separate_sfc=False,
            # Dashboard
            min_pressure_levels=30,
            excluded_styles={'smoke', 'q', 'moisture_transport', 'cloud_total', 'icing',
                             'dewpoint_dep', 'vorticity', 'pv'},
            synoptic_cycles_to_keep=0,
            hourly_cycles_to_keep=2,
        )

        # === NAM Nest 3km ===
        models['nam_nest'] = ModelConfig(
            name='nam_nest',
            full_name='NAM CONUS Nest',
            resolution='3km',
            file_types={
                'pressure': 'conusnest.hiresf',
                'surface': 'conusnest.hiresf',
            },
            filename_pattern='nam.t{hour:02d}z.{file_type}{forecast_hour:02d}.tm00.grib2',
            download_sources=[
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nam/prod/nam.{date}/{filename}',
                'https://noaa-nam-pds.s3.amazonaws.com/nam.{date}/{filename}',
            ],
            forecast_cycles=[0, 6, 12, 18],
            max_forecast_hours={0: 60, 6: 60, 12: 60, 18: 60},
            grid_type='lambert_conformal',
            domain='conus',
            # FHR list: hourly to F60 (all cycles same)
            base_fhr_list=list(range(61)),
            extended_cycle_hours=None,
            extended_fhr_list=None,
            # Availability & download
            availability_lag_minutes=int(os.environ.get('XSECT_LAG_NAM_NEST_MIN', '105')),
            grib_required_patterns=['*conusnest.hiresf*.grib2'],
            grib_file_types=['pressure'],
            needs_separate_sfc=False,
            # Dashboard
            min_pressure_levels=40,
            excluded_styles={'smoke', 'dewpoint_dep', 'vorticity', 'pv'},
            synoptic_cycles_to_keep=0,
            hourly_cycles_to_keep=2,
        )

        return models

    def get_model(self, model_name: str) -> Optional[ModelConfig]:
        """Get configuration for a specific model"""
        return self.models.get(model_name.lower())

    def list_models(self) -> List[str]:
        """List all available model names"""
        return list(self.models.keys())

    def get_model_info(self, model_name: str) -> Dict[str, str]:
        """Get basic information about a model"""
        model = self.get_model(model_name)
        if not model:
            return {}

        return {
            'name': model.name,
            'full_name': model.full_name,
            'resolution': model.resolution,
            'domain': model.domain,
            'cycles': f"{len(model.forecast_cycles)} per day",
            'max_forecast': f"{max(model.max_forecast_hours.values())} hours"
        }


# ---------------------------------------------------------------------------
# Singleton registry (created once on import)
# ---------------------------------------------------------------------------

_registry: Optional[ModelRegistry] = None


def get_model_registry() -> ModelRegistry:
    """Get the global model registry singleton."""
    global _registry
    if _registry is None:
        _registry = ModelRegistry()
    return _registry


# ---------------------------------------------------------------------------
# Module-level convenience functions
# ---------------------------------------------------------------------------

def get_model_config(model_name: str) -> Optional[ModelConfig]:
    """Get ModelConfig for a model name."""
    return get_model_registry().get_model(model_name)


def get_model_fhr_list(model_name: str, cycle_hour: int = None) -> List[int]:
    """Get the FHR list for a model+cycle. Single source of truth."""
    cfg = get_model_config(model_name)
    if cfg is None:
        return list(range(19))
    return cfg.get_fhr_list(cycle_hour)


def get_model_max_fhr(model_name: str, cycle_hour: int = 0) -> int:
    """Get the max FHR for a model+cycle."""
    cfg = get_model_config(model_name)
    if cfg is None:
        return 18
    return cfg.get_max_forecast_hour(cycle_hour)


def get_model_availability_lag(model_name: str) -> int:
    """Get availability lag in minutes for a model."""
    cfg = get_model_config(model_name)
    if cfg is None:
        return 50
    return cfg.availability_lag_minutes


# ---------------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    registry = get_model_registry()

    print("Available models:")
    for model_name in registry.list_models():
        info = registry.get_model_info(model_name)
        print(f"\n{model_name.upper()}:")
        for key, value in info.items():
            print(f"  {key}: {value}")

    print("\n\nFHR list tests:")
    for name in registry.list_models():
        cfg = registry.get_model(name)
        for ch in sorted(set(cfg.forecast_cycles)):
            fhrs = cfg.get_fhr_list(ch)
            ext = " [EXTENDED]" if cfg.is_extended_cycle(ch) else ""
            print(f"  {name} {ch:02d}z: {len(fhrs)} FHRs, F{fhrs[0]:02d}-F{fhrs[-1]:02d}{ext}")
            if cfg.is_extended_cycle(ch):
                break  # Only show one extended cycle per model

    print("\n\nAvailability lags:")
    for name in registry.list_models():
        cfg = registry.get_model(name)
        print(f"  {name}: {cfg.availability_lag_minutes} min")

    # Test URL generation
    print("\n\nTest URL generation:")
    hrrr = registry.get_model('hrrr')
    hrrr_urls = hrrr.get_download_urls('20250711', 12, 'pressure', 6)
    print("\nHRRR URLs for 2025-07-11 12Z F06:")
    for url in hrrr_urls:
        print(f"  {url}")

    rrfs = registry.get_model('rrfs')
    rrfs_urls = rrfs.get_download_urls('20250711', 12, 'pressure', 6)
    print("\nRRFS URLs for 2025-07-11 12Z F06:")
    for url in rrfs_urls:
        print(f"  {url}")
