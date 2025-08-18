from .common import *
from .effective_layer_detection import detect_effective_inflow_layer, compute_effective_layer_srh

def effective_srh(srh_data: np.ndarray, cape: np.ndarray, cin: np.ndarray,
                 lcl_height: np.ndarray, cape_profile: np.ndarray = None,
                 cin_profile: np.ndarray = None, u_profile: np.ndarray = None,
                 v_profile: np.ndarray = None, heights: np.ndarray = None,
                 storm_motion_u: float = 7.5, storm_motion_v: float = 7.5) -> np.ndarray:
    """
    Compute Effective Storm Relative Helicity using contiguous layer method
    
    NEW v2.2: Now uses proper contiguous effective layer algorithm when profile
    data is available, falls back to threshold-based method when profiles unavailable.
    
    Args:
        srh_data: Storm relative helicity (m²/s²) - fallback (e.g., 0-3km SRH)
        cape: CAPE (J/kg) - for threshold criteria
        cin: CIN (J/kg, negative values) - for threshold criteria
        lcl_height: LCL height (m) - for threshold criteria
        cape_profile: CAPE profile (J/kg), shape (..., levels) - optional
        cin_profile: CIN profile (J/kg), shape (..., levels) - optional
        u_profile: U-wind profile (m/s), shape (..., levels) - optional
        v_profile: V-wind profile (m/s), shape (..., levels) - optional
        heights: Height levels (m AGL), shape (levels,) - optional
        storm_motion_u: Storm motion U-component (m/s) - default Bunkers right
        storm_motion_v: Storm motion V-component (m/s) - default Bunkers right
        
    Returns:
        Effective SRH (m²/s²)
        
    Method:
        1. If profiles available: Use contiguous effective layer algorithm
        2. Otherwise: Use threshold-based masking (legacy method)
        
    References:
        Thompson et al. (2007): Effective layer methodology
        Bunkers et al. (2000): Storm motion calculation
        SPC Mesoanalysis: Operational effective SRH calculations
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
            
            # Compute SRH over effective layer
            effective_srh = compute_effective_layer_srh(
                u_profile, v_profile, storm_motion_u, storm_motion_v,
                bottom_idx, top_idx, heights
            )
            
            # Apply minimum depth filter (effective layer should be substantial)
            min_depth = 500.0  # meters
            depth_mask = depth >= min_depth
            effective_srh = np.where(depth_mask, effective_srh, 0.0)
            
            print("🔍 ESRH: Using contiguous effective layer method")
            return effective_srh
            
        except Exception as e:
            print(f"⚠️ ESRH: Contiguous method failed ({e}), falling back to threshold")
            # Fall through to legacy method
    
    # ========================================================================
    # METHOD 2: Threshold-based Masking (fallback)
    # ========================================================================
    print("🔍 ESRH: Using threshold-based method (profiles unavailable)")
    
    # Effective layer criteria (simplified)
    effective_mask = (
        (cape >= 100) &           # Minimum CAPE for convection
        (cin >= -250) &           # Not too much CIN (less negative)  
        (lcl_height <= 2500)      # Reasonable LCL height for inflow
    )
    
    return np.where(effective_mask, srh_data, 0.0)
