from .common import *
from .constants import CAPE_MIN_CONVECTION

def convective_velocity_scale(sensible_heat_flux: np.ndarray, 
                            boundary_layer_height: np.ndarray,
                            temp_surface: np.ndarray, surface_pressure: np.ndarray = None,
                            use_accurate_density: bool = True) -> np.ndarray:
    """
    Compute Convective Velocity Scale (w*) with improved physics
    
    NEW v2.2: Now uses accurate air density calculation and explicit
    thermodynamic constants for improved boundary layer physics.
    
    Args:
        sensible_heat_flux: Surface sensible heat flux (W/m²)
        boundary_layer_height: Boundary layer height (m)
        temp_surface: Surface temperature (K)
        surface_pressure: Surface pressure (Pa) - for accurate density
        use_accurate_density: Use pressure-dependent density calculation
        
    Returns:
        Convective velocity scale w* (m/s)
        
    Formula:
        w* = [g * H₀ * h / (ρ * cp * Tᵥ)]^(1/3)
        
    where:
        g = gravitational acceleration (9.81 m/s²)
        H₀ = surface sensible heat flux (W/m²)
        h = boundary layer height (m)
        ρ = air density (kg/m³)
        cp = specific heat at constant pressure (1005 J/(kg·K))
        Tᵥ = virtual temperature (≈ surface temperature for dry air)
        
    References:
        Stull, R.B. (1988): An Introduction to Boundary Layer Meteorology
        Garratt, J.R. (1992): The Atmospheric Boundary Layer
        Kaimal & Finnigan (1994): Atmospheric Boundary Layer Flows
    """
    
    # ========================================================================
    # PHYSICAL CONSTANTS (explicit for accuracy)
    # ========================================================================
    g = 9.80665     # m/s² - standard gravitational acceleration
    cp = 1005.0     # J/(kg·K) - specific heat of dry air at constant pressure
    Rd = 287.04     # J/(kg·K) - specific gas constant for dry air
    
    # ========================================================================
    # AIR DENSITY CALCULATION
    # ========================================================================
    if use_accurate_density and surface_pressure is not None:
        # Accurate density using ideal gas law: ρ = p/(Rd * T)
        # Convert pressure to Pa if needed
        if np.mean(surface_pressure) < 2000:
            pressure_pa = surface_pressure * 100.0  # hPa to Pa
        else:
            pressure_pa = surface_pressure
            
        rho = pressure_pa / (Rd * temp_surface)
        print("🔍 w*: Using pressure-dependent air density")
    else:
        # Standard sea level density (fallback)
        rho = 1.225  # kg/m³ at standard conditions
        print("🔍 w*: Using standard air density (pressure unavailable)")
    
    # ========================================================================
    # BUOYANCY FLUX CALCULATION
    # ========================================================================
    # Kinematic sensible heat flux: H₀/(ρ * cp)
    kinematic_heat_flux = sensible_heat_flux / (rho * cp)  # K·m/s
    
    # Buoyancy flux: B = g * H₀/(ρ * cp * T)
    buoyancy_flux = g * kinematic_heat_flux / temp_surface  # m²/s³
    
    # ========================================================================
    # CONVECTIVE VELOCITY SCALE
    # ========================================================================
    # w* = (B * h)^(1/3) where B is buoyancy flux and h is BL height
    convective_parameter = buoyancy_flux * boundary_layer_height
    
    # Only calculate w* for unstable conditions (positive buoyancy flux)
    unstable_mask = convective_parameter > 0
    
    w_star = np.where(
        unstable_mask,
        np.power(convective_parameter, 1.0/3.0),
        0.0  # Stable/neutral conditions → no convective scaling
    )
    
    # ========================================================================
    # QUALITY CONTROL
    # ========================================================================
    # Apply physically reasonable limits
    w_star = np.clip(w_star, 0.0, 15.0)  # Cap at 15 m/s (very strong convection)
    
    # Mask invalid inputs
    valid_mask = (
        np.isfinite(sensible_heat_flux) & 
        np.isfinite(boundary_layer_height) & (boundary_layer_height > 0) &
        np.isfinite(temp_surface) & (temp_surface > 200)  # Reasonable temperature
    )
    
    w_star = np.where(valid_mask, w_star, 0.0)
    
    # Log convective conditions
    strong_convection = np.any(w_star > 3.0)
    if strong_convection:
        max_w_star = np.nanmax(w_star)
        print(f"🔍 w*: Strong convection detected, max w* = {max_w_star:.1f} m/s")
    
    return w_star
