# HRRR v2.2 - Essential Files to Understand the Project

> **🎯 Critical files for understanding the HRRR Weather Model Processing System v2.2**

## 📚 Core Documentation

### `/README.md`
**Primary project overview** - Start here for architecture, installation, and usage guide

### `/DERIVED_PARAMETERS.md` 
**Complete parameter reference** - All 108 parameters with SPC-aligned formulas and operational guidance

### `/SUBAGENT_CONTEXT_GUIDE.md`
**Technical implementation guide** - Detailed v2.2 task breakdown and file organization

## 🧪 Validation & Testing

### `/tests/test_v22_improvements.py`
**21 comprehensive unit tests** - Validates all v2.2 SPC-aligned parameters and improvements

### `/tests/run_all_tests.py`
**Test suite runner** - Execute validation of entire system

## 🔧 Core Implementation

### `/derived_params/constants.py`
**Centralized constants module** - All STP, EHI, SCP, SHIP normalization values (prevents parameter drift)

### `/derived_params/__init__.py`
**Parameter dispatch system** - Function registry and imports for all 108 parameters

### `/parameters/derived.json`
**Parameter configuration** - Field definitions, colormaps, and metadata for CLI system

## ⛈️ Critical Severe Weather Parameters

### `/derived_params/significant_tornado_parameter_fixed.py`
**STP canonical implementation** - SPC-aligned fixed-layer STP with CIN term

### `/derived_params/effective_layer_detection.py`
**Contiguous layer algorithm** - Advanced effective layer detection for ESRH/EBWD

### `/derived_params/significant_hail_parameter.py`
**SHIP v1.1 implementation** - SPC canonical hail parameter with corrected temperature term

## 🌍 Enhanced Physics

### `/derived_params/surface_richardson_number.py`
**Boundary layer stability** - Virtual potential temperature Richardson number calculation

### `/derived_params/ventilation_rate_from_components.py`
**Transport wind methodology** - Improved fire weather ventilation using mixed-layer winds

## 🖥️ CLI System

### `/processor_cli.py`
**Main CLI interface** - Command-line tool for processing HRRR data with all 108 parameters

### `/smart_hrrr/processor_core.py`
**Core processing engine** - Field loading, derivation, and plotting system

---

**💡 Read in order: README → DERIVED_PARAMETERS → Test files → Core implementation**  
**🎯 Total: 108 parameters, 21 unit tests, full SPC compliance achieved**