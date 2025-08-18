from .common import *
from .effective_layer_detection import detect_effective_inflow_layer, compute_effective_layer_wind_shear

def effective_shear(wind_shear_06km: np.ndarray, mlcape: np.ndarray, mlcin: np.ndarray,
                   cape_profile: np.ndarray = None, cin_profile: np.ndarray = None,
                   u_profile: np.ndarray = None, v_profile: np.ndarray = None,
                   heights: np.ndarray = None) -> np.ndarray:
    """
    Compute Effective Bulk Wind Difference (EBWD) using contiguous layer method
    
    NEW v2.2: Now uses proper contiguous effective layer algorithm when profile
    data is available, falls back to 0-6km proxy when profiles unavailable.
    
    Args:
        wind_shear_06km: 0-6km bulk wind shear magnitude (m/s) - fallback
        mlcape: Mixed-layer CAPE (J/kg) - for CIN gating
        mlcin: Mixed-layer CIN (J/kg) - for CIN gating
        cape_profile: CAPE profile (J/kg), shape (..., levels) - optional
        cin_profile: CIN profile (J/kg), shape (..., levels) - optional  
        u_profile: U-wind profile (m/s), shape (..., levels) - optional
        v_profile: V-wind profile (m/s), shape (..., levels) - optional
        heights: Height levels (m AGL), shape (levels,) - optional
        
    Returns:
        Effective bulk wind difference (m/s)
        
    Method:
        1. If profiles available: Use contiguous effective layer algorithm
        2. Otherwise: Use 0-6km shear with CIN gating (legacy method)
        
    References:
        Thompson et al. (2007): Effective layer methodology
        SPC Mesoanalysis: Operational effective layer calculations
    """
    
    # ========================================================================
    # METHOD 1: Contiguous Effective Layer (preferred)
    # ========================================================================
    if (cape_profile is not None and cin_profile is not None and 
        u_profile is not None and v_profile is not None and heights is not None):
        
        try:
            # Detect effective inflow layer using contiguous algorithm
            bottom_idx, top_idx, depth = detect_effective_inflow_layer(
                cape_profile, cin_profile, heights, 
                cape_threshold=100.0, cin_threshold=-250.0
            )
            
            # Compute bulk wind difference over effective layer
            effective_shear = compute_effective_layer_wind_shear(
                u_profile, v_profile, bottom_idx, top_idx
            )
            
            # Apply minimum depth filter (effective layer should be substantial)
            min_depth = 500.0  # meters
            depth_mask = depth >= min_depth
            effective_shear = np.where(depth_mask, effective_shear, 0.0)
            
            print("🔍 EBWD: Using contiguous effective layer method")
            return effective_shear
            
        except Exception as e:
            print(f"⚠️ EBWD: Contiguous method failed ({e}), falling back to proxy")
            # Fall through to legacy method
    
    # ========================================================================
    # METHOD 2: 0-6km Proxy with CIN Gating (fallback)
    # ========================================================================
    print("🔍 EBWD: Using 0-6km proxy method (profiles unavailable)")
    
    # Use 0-6km shear as effective shear proxy
    effective_shear = wind_shear_06km
    
    # Apply CIN gate to reduce noise where inhibition is strong
    # Effective shear should be reduced where CIN < -100 J/kg
    cin_weight = cin_gate(mlcin, hi=-50.0, lo=-100.0)
    effective_shear = effective_shear * cin_weight
    
    # Ensure positive values
    effective_shear = np.maximum(effective_shear, 0.0)
    
    # Mask invalid data
    effective_shear = np.where((mlcape < 0) | (np.isnan(mlcape)) | 
                              (np.isnan(wind_shear_06km)), np.nan, effective_shear)
    
    return effective_shear
