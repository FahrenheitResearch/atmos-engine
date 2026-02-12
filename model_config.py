#!/usr/bin/env python3
"""
Weather Model Configuration System
Handles configuration for different weather models (HRRR, RRFS, etc.)
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta


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
    
    def get_filename(self, cycle_hour: int, file_type: str, forecast_hour: int, domain: str = None) -> str:
        """Generate filename for this model"""
        model_file_type = self.file_types.get(file_type, file_type)
        filename = self.filename_pattern.format(
            hour=cycle_hour,
            file_type=model_file_type,
            forecast_hour=forecast_hour
        )
        
        # Handle RRFS domain variations
        if self.name == 'rrfs' and domain:
            # For RRFS, different domains have different patterns
            if domain == 'conus':
                # Already has .conus in pattern
                pass
            elif domain == 'na':
                # Full North America uses .na
                filename = filename.replace('.conus', '.na')
            elif domain in ['ak', 'hi', 'pr']:
                # Alaska, Hawaii, Puerto Rico use 2.5km resolution
                filename = filename.replace('.3km', '.2p5km').replace('.conus', f'.{domain}')
        
        return filename
    
    def get_download_urls(self, date_str: str, cycle_hour: int, file_type: str, 
                         forecast_hour: int, domain: str = 'conus') -> List[str]:
        """Get download URLs for this model"""
        filename = self.get_filename(cycle_hour, file_type, forecast_hour, domain)
        urls = []
        
        for source_pattern in self.download_sources:
            # Ensure hour is formatted correctly
            hour_str = f"{cycle_hour:02d}" if isinstance(cycle_hour, int) else cycle_hour
            
            url = source_pattern.format(
                date=date_str,
                hour=hour_str,
                filename=filename
            )
            urls.append(url)
        
        return urls
    
    def get_max_forecast_hour(self, cycle_hour: int) -> int:
        """Get maximum forecast hour for a given cycle"""
        return self.max_forecast_hours.get(cycle_hour, 18)  # Default to 18
    
    def is_valid_cycle(self, cycle_hour: int) -> bool:
        """Check if this is a valid cycle hour for the model"""
        return cycle_hour in self.forecast_cycles


class ModelRegistry:
    """Registry of available weather models"""
    
    def __init__(self):
        self.models = self._initialize_models()
    
    def _initialize_models(self) -> Dict[str, ModelConfig]:
        """Initialize all available model configurations"""
        
        models = {}
        
        # HRRR Configuration
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
                # NOMADS (recent data)
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/hrrr/prod/hrrr.{date}/conus/{filename}',
                # AWS S3 (historical data)
                'https://noaa-hrrr-bdp-pds.s3.amazonaws.com/hrrr.{date}/conus/{filename}',
                # Utah Pando (backup)
                'https://pando-rgw01.chpc.utah.edu/hrrr/hrrr.{date}/conus/{filename}'
            ],
            forecast_cycles=list(range(24)),  # Every hour
            max_forecast_hours={
                # Synoptic times (00, 06, 12, 18 UTC) go to 48 hours
                0: 48, 6: 48, 12: 48, 18: 48,
                # All other hours go to 18 hours
                **{h: 18 for h in range(24) if h not in [0, 6, 12, 18]}
            },
            grid_type='lambert_conformal',
            domain='conus'
        )
        
        # RRFS Configuration (experimental but actively downloading)
        models['rrfs'] = ModelConfig(
            name='rrfs',
            full_name='Rapid Refresh Forecast System',
            resolution='3km',
            file_types={
                'pressure': 'prslev',
                'surface': 'prslev',  # RRFS uses prslev for most products
                'native': 'natlev'
            },
            filename_pattern='rrfs.t{hour:02d}z.{file_type}.3km.f{forecast_hour:03d}.conus.grib2',
            download_sources=[
                # AWS S3 (new URL structure as of July 2025)
                'https://noaa-rrfs-pds.s3.amazonaws.com/rrfs_a/rrfs.{date}/{hour}/{filename}',
                # Alternative S3 URL format
                'https://s3.amazonaws.com/noaa-rrfs-pds/rrfs_a/rrfs.{date}/{hour}/{filename}'
            ],
            forecast_cycles=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18, 21],  # Hourly 00-12z, then 3-hourly (no 13z/14z)
            max_forecast_hours={
                # Synoptic times (00, 06, 12, 18 UTC) go to 84 hours
                0: 84, 6: 84, 12: 84, 18: 84,
                # All other hours go to 18 hours
                **{h: 18 for h in [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 15, 21]}
            },
            grid_type='rotated_lat_lon',
            domain='north_america',
            variable_mappings={
                # Map HRRR variable names to RRFS equivalents (if different)
                # This will be populated as we discover differences
                # Example: 'refc': 'composite_reflectivity'
            }
        )
        
        # GFS Configuration
        models['gfs'] = ModelConfig(
            name='gfs',
            full_name='Global Forecast System',
            resolution='0.25deg',
            file_types={
                'pressure': 'pgrb2.0p25',  # 0.25 degree pressure level data
                'surface': 'pgrb2.0p25',    # Surface data is also in pgrb2 files for GFS
                'pressure_b': 'pgrb2b.0p25' # Additional pressure level data
            },
            filename_pattern='gfs.t{hour:02d}z.{file_type}.f{forecast_hour:03d}',
            download_sources=[
                # NOMADS production server
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.{date}/{hour}/atmos/{filename}',
                # NCEP backup server
                'https://ftpprd.ncep.noaa.gov/data/nccf/com/gfs/prod/gfs.{date}/{hour}/atmos/{filename}'
            ],
            forecast_cycles=[0, 6, 12, 18],  # Four cycles per day
            max_forecast_hours={
                # All cycles go to 384 hours (16 days)
                0: 384, 6: 384, 12: 384, 18: 384
            },
            grid_type='latlon',
            domain='global'
        )
        
        # NAM 12km CONUS Configuration
        # NOTE: awphys has t/u/r/w/gh/surface fields. eccodes misses v-wind on isobaric
        # levels, but cfgrib (auto fallback) extracts it successfully. Missing: q, cloud,
        # dew_point. bgrd3d (441MB) has everything but is 2x the size.
        models['nam'] = ModelConfig(
            name='nam',
            full_name='North American Mesoscale',
            resolution='12km',
            file_types={
                'pressure': 'awphys',  # Has t, u, v (via cfgrib), r, w, gh — missing q, cloud, dew_point
                'surface': 'awphys',   # Same file has surface diagnostics
            },
            filename_pattern='nam.t{hour:02d}z.{file_type}{forecast_hour:02d}.tm00.grib2',
            download_sources=[
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nam/prod/nam.{date}/{filename}',
                'https://noaa-nam-pds.s3.amazonaws.com/nam.{date}/{filename}',
            ],
            forecast_cycles=[0, 6, 12, 18],
            max_forecast_hours={
                0: 84, 6: 84, 12: 84, 18: 84
            },
            grid_type='lambert_conformal',
            domain='conus'
        )

        # RAP 13km CONUS Configuration
        # NOTE: wrfprs has all fields but uses non-standard grid (ncep_32769) that eccodes can't decode.
        # awp130pgrb uses standard Lambert grid. eccodes misses v-wind, but cfgrib (auto fallback)
        # extracts it. Missing: q, cloud, dew_point. Wind styles now work.
        models['rap'] = ModelConfig(
            name='rap',
            full_name='Rapid Refresh',
            resolution='13km',
            file_types={
                'pressure': 'awp130pgrb',  # Standard Lambert grid, has t, u, v (via cfgrib), r, w, gh — missing q, cloud
                'surface': 'awp130pgrb',   # Surface data in same file
            },
            filename_pattern='rap.t{hour:02d}z.{file_type}f{forecast_hour:02d}.grib2',
            download_sources=[
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/rap/prod/rap.{date}/{filename}',
                'https://noaa-rap-pds.s3.amazonaws.com/rap.{date}/{filename}',
            ],
            forecast_cycles=list(range(24)),  # Every hour
            max_forecast_hours={
                # Extended cycles (03, 09, 15, 21) go to 51h
                3: 51, 9: 51, 15: 51, 21: 51,
                # All other hours go to 21h
                **{h: 21 for h in range(24) if h not in [3, 9, 15, 21]}
            },
            grid_type='lambert_conformal',
            domain='conus'
        )

        # NAM Nest 3km CONUS Configuration
        models['nam_nest'] = ModelConfig(
            name='nam_nest',
            full_name='NAM CONUS Nest',
            resolution='3km',
            file_types={
                'pressure': 'conusnest.hiresf',  # Pressure + surface combined
                'surface': 'conusnest.hiresf',
            },
            filename_pattern='nam.t{hour:02d}z.{file_type}{forecast_hour:02d}.tm00.grib2',
            download_sources=[
                'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nam/prod/nam.{date}/{filename}',
                'https://noaa-nam-pds.s3.amazonaws.com/nam.{date}/{filename}',
            ],
            forecast_cycles=[0, 6, 12, 18],
            max_forecast_hours={
                0: 60, 6: 60, 12: 60, 18: 60
            },
            grid_type='lambert_conformal',
            domain='conus'
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


def get_model_registry() -> ModelRegistry:
    """Get the global model registry instance"""
    return ModelRegistry()


if __name__ == "__main__":
    # Test the model configuration
    registry = get_model_registry()
    
    print("Available models:")
    for model_name in registry.list_models():
        info = registry.get_model_info(model_name)
        print(f"\n{model_name.upper()}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
    
    # Test URL generation
    print("\n\nTest URL generation:")
    
    # HRRR example
    hrrr = registry.get_model('hrrr')
    hrrr_urls = hrrr.get_download_urls('20250711', 12, 'pressure', 6)
    print("\nHRRR URLs for 2025-07-11 12Z F06:")
    for url in hrrr_urls:
        print(f"  {url}")
    
    # RRFS example
    rrfs = registry.get_model('rrfs')
    rrfs_urls = rrfs.get_download_urls('20250711', 12, 'pressure', 6)
    print("\nRRFS URLs for 2025-07-11 12Z F06:")
    for url in rrfs_urls:
        print(f"  {url}")