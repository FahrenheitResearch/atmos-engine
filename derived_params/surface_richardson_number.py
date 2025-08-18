from .common import *

def surface_richardson_number(temp_gradient: np.ndarray = None, wind_shear: np.ndarray = None,
                            temp_surface: np.ndarray = None, temp_profile: np.ndarray = None,
                            rh_profile: np.ndarray = None, pressure_profile: np.ndarray = None,
                            wind_speed_profile: np.ndarray = None, heights: np.ndarray = None) -> np.ndarray:
    """
    Compute Surface Richardson Number using virtual potential temperature
    
    NEW v2.2: Now uses virtual potential temperature (θᵥ) for improved accuracy
    in moist environments. Falls back to simple temperature when profiles unavailable.
    
    Args:
        temp_gradient: Temperature gradient near surface (K/m) - fallback method
        wind_shear: Wind shear near surface (s⁻¹) - fallback method
        temp_surface: Surface temperature (K) - fallback method
        temp_profile: Temperature profile (K), shape (..., levels) - preferred
        rh_profile: Relative humidity profile (%), shape (..., levels) - preferred
        pressure_profile: Pressure profile (Pa), shape (..., levels) - preferred
        wind_speed_profile: Wind speed profile (m/s), shape (..., levels) - preferred
        heights: Height levels (m), shape (levels,) - preferred
        
    Returns:
        Surface Richardson number (dimensionless)
        
    Formula:
        Ri = (g/θᵥ) × (∂θᵥ/∂z) / (∂u/∂z)²
        
    where θᵥ is virtual potential temperature accounting for moisture effects
        
    References:
        Stull, R.B. (1988): An Introduction to Boundary Layer Meteorology
        Businger et al. (1971): Flux-profile relationships in the atmospheric surface layer
    """
    
    # ========================================================================
    # METHOD 1: Virtual Potential Temperature (preferred)
    # ========================================================================
    if (temp_profile is not None and rh_profile is not None and 
        pressure_profile is not None and wind_speed_profile is not None and heights is not None):
        
        try:
            # Compute virtual potential temperature profile
            theta_v_profile = compute_virtual_potential_temperature_profile(
                temp_profile, rh_profile, pressure_profile, heights
            )
            
            # Compute gradients using finite differences
            # Use surface layer (typically first 100-200m)
            surface_layer_depth = 200.0  # meters
            surface_mask = heights <= surface_layer_depth
            
            if np.sum(surface_mask) < 2:
                raise ValueError("Insufficient surface layer data")
            
            # Extract surface layer data
            theta_v_surface = theta_v_profile[..., surface_mask]
            wind_surface = wind_speed_profile[..., surface_mask]
            heights_surface = heights[surface_mask]
            
            # Compute gradients using least squares fit (more robust than simple diff)
            dtheta_v_dz = compute_vertical_gradient(theta_v_surface, heights_surface)
            du_dz = compute_vertical_gradient(wind_surface, heights_surface)
            
            # Surface virtual potential temperature
            theta_v_sfc = theta_v_profile[..., 0]
            
            # Richardson number using virtual potential temperature
            g = 9.81  # m/s²
            du_dz_squared = np.maximum(du_dz**2, 1e-8)  # Avoid division by zero
            
            ri = (g / theta_v_sfc) * dtheta_v_dz / du_dz_squared
            
            print("🔍 Richardson: Using virtual potential temperature method")
            return np.clip(ri, -10, 10)  # Cap at physically reasonable values
            
        except Exception as e:
            print(f"⚠️ Richardson: Virtual θᵥ method failed ({e}), falling back to simple")
            # Fall through to simple method
    
    # ========================================================================
    # METHOD 2: Simple Temperature (fallback)
    # ========================================================================
    print("🔍 Richardson: Using simple temperature method (profiles unavailable)")
    
    if temp_gradient is None or wind_shear is None or temp_surface is None:
        raise ValueError("Either provide profiles or fallback parameters (temp_gradient, wind_shear, temp_surface)")
    
    # Richardson number = (g/T) * (dT/dz) / (du/dz)²
    g = 9.81  # m/s²
    
    # Avoid division by zero
    shear_squared = np.maximum(wind_shear**2, 1e-8)
    
    ri = (g / temp_surface) * temp_gradient / shear_squared
    
    return np.clip(ri, -10, 10)  # Cap at reasonable values


def compute_virtual_potential_temperature_profile(temp_profile: np.ndarray, 
                                                 rh_profile: np.ndarray,
                                                 pressure_profile: np.ndarray,
                                                 heights: np.ndarray) -> np.ndarray:
    """
    Compute virtual potential temperature profile
    
    θᵥ = θ(1 + 0.61q) where q is specific humidity
    θ = T(p₀/p)^(R/cp) where p₀ = 1000 hPa
    
    Args:
        temp_profile: Temperature profile (K)
        rh_profile: Relative humidity profile (%)
        pressure_profile: Pressure profile (Pa)
        heights: Height levels (m)
        
    Returns:
        Virtual potential temperature profile (K)
    """
    # Convert pressure to hPa if in Pa
    if np.mean(pressure_profile) > 2000:
        pressure_hpa = pressure_profile / 100.0
    else:
        pressure_hpa = pressure_profile
    
    # Constants
    p0 = 1000.0  # hPa reference pressure
    Rd = 287.0   # J/(kg·K) - dry air gas constant
    cp = 1005.0  # J/(kg·K) - specific heat at constant pressure
    
    # Compute potential temperature
    theta = temp_profile * (p0 / pressure_hpa)**(Rd/cp)
    
    # Compute specific humidity from RH
    # Saturation vapor pressure (Tetens formula)
    es = 6.112 * np.exp(17.67 * (temp_profile - 273.15) / (temp_profile - 29.65))  # hPa
    
    # Actual vapor pressure
    e = (rh_profile / 100.0) * es
    
    # Specific humidity
    q = 0.622 * e / (pressure_hpa - 0.378 * e)
    q = np.maximum(q, 0.0)  # Ensure non-negative
    
    # Virtual potential temperature
    theta_v = theta * (1 + 0.61 * q)
    
    return theta_v


def compute_vertical_gradient(field_profile: np.ndarray, heights: np.ndarray) -> np.ndarray:
    """
    Compute vertical gradient using least squares fit
    
    More robust than simple finite differences for noisy data
    
    Args:
        field_profile: Field values, shape (..., levels)
        heights: Height levels (m), shape (levels,)
        
    Returns:
        Vertical gradient (field_units/m)
    """
    if field_profile.ndim == 1:
        # Single profile
        if len(heights) < 2:
            return 0.0
        # Simple linear fit
        gradient = np.polyfit(heights, field_profile, 1)[0]
        return gradient
    else:
        # Multiple profiles
        batch_shape = field_profile.shape[:-1]
        gradients = np.zeros(batch_shape)
        
        for idx in np.ndindex(batch_shape):
            profile = field_profile[idx]
            if len(heights) >= 2:
                gradient = np.polyfit(heights, profile, 1)[0]
                gradients[idx] = gradient
                
        return gradients
