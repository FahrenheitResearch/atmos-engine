from .common import *

def detect_effective_inflow_layer(cape_profile: np.ndarray, cin_profile: np.ndarray, 
                                 heights: np.ndarray, cape_threshold: float = 100.0,
                                 cin_threshold: float = -250.0) -> tuple:
    """
    Detect effective inflow layer using contiguous layer algorithm
    
    The effective inflow layer is defined as the layer through which a parcel 
    must be lifted in order to reach its level of free convection (LFC),
    based on CAPE and CIN thresholds applied to a contiguous layer.
    
    Args:
        cape_profile: CAPE values at each level (J/kg), shape (..., levels)
        cin_profile: CIN values at each level (J/kg, negative), shape (..., levels)  
        heights: Height values for each level (m AGL), shape (levels,)
        cape_threshold: Minimum CAPE for effective layer (J/kg)
        cin_threshold: Maximum CIN for effective layer (J/kg, negative)
        
    Returns:
        tuple: (effective_bottom_idx, effective_top_idx, effective_depth)
        - effective_bottom_idx: Bottom level indices of effective layer
        - effective_top_idx: Top level indices of effective layer  
        - effective_depth: Depth of effective layer (m)
        
    Algorithm:
        1. Find all levels meeting CAPE/CIN criteria
        2. Identify largest contiguous layer meeting criteria
        3. Return layer boundaries and depth
        
    References:
        Thompson et al. (2007): "Close Proximity Soundings within Supercell Environments"
        SPC Effective Layer methodology
    """
    # Ensure inputs are numpy arrays
    cape_profile = np.asarray(cape_profile)
    cin_profile = np.asarray(cin_profile)
    heights = np.asarray(heights)
    
    # Get spatial dimensions
    if cape_profile.ndim == 1:
        # Single profile case
        cape_profile = cape_profile[np.newaxis, :]
        cin_profile = cin_profile[np.newaxis, :]
        squeeze_output = True
    else:
        squeeze_output = False
        
    batch_shape = cape_profile.shape[:-1]
    n_levels = cape_profile.shape[-1]
    
    # Initialize outputs
    bottom_idx = np.full(batch_shape, -1, dtype=int)
    top_idx = np.full(batch_shape, -1, dtype=int)
    depth = np.zeros(batch_shape, dtype=float)
    
    # Apply criteria to find valid levels
    # Level is valid if CAPE >= threshold AND CIN >= threshold (less negative)
    valid_levels = (cape_profile >= cape_threshold) & (cin_profile >= cin_threshold)
    
    # Process each horizontal grid point
    for idx in np.ndindex(batch_shape):
        valid_at_point = valid_levels[idx]
        
        if not np.any(valid_at_point):
            # No valid levels - keep defaults (-1, -1, 0)
            continue
            
        # Find contiguous segments of valid levels
        # Using diff to find where valid levels start/stop
        valid_diff = np.diff(np.concatenate(([False], valid_at_point, [False])).astype(int))
        segment_starts = np.where(valid_diff == 1)[0]
        segment_ends = np.where(valid_diff == -1)[0]
        
        if len(segment_starts) == 0:
            continue
            
        # Find the largest contiguous segment
        segment_lengths = segment_ends - segment_starts
        max_segment_idx = np.argmax(segment_lengths)
        
        # Get bottom and top of largest segment
        segment_bottom = segment_starts[max_segment_idx]
        segment_top = segment_ends[max_segment_idx] - 1  # End is exclusive, so subtract 1
        
        # Store results
        bottom_idx[idx] = segment_bottom
        top_idx[idx] = segment_top
        depth[idx] = heights[segment_top] - heights[segment_bottom]
    
    if squeeze_output:
        bottom_idx = bottom_idx.item()
        top_idx = top_idx.item()
        depth = depth.item()
        
    return bottom_idx, top_idx, depth


def compute_effective_layer_wind_shear(u_profile: np.ndarray, v_profile: np.ndarray,
                                     bottom_idx: np.ndarray, top_idx: np.ndarray) -> np.ndarray:
    """
    Compute bulk wind difference over effective layer
    
    Args:
        u_profile: U-wind component profile (m/s), shape (..., levels)
        v_profile: V-wind component profile (m/s), shape (..., levels)
        bottom_idx: Bottom level indices of effective layer
        top_idx: Top level indices of effective layer
        
    Returns:
        Effective bulk wind difference magnitude (m/s)
    """
    u_profile = np.asarray(u_profile)
    v_profile = np.asarray(v_profile)
    bottom_idx = np.asarray(bottom_idx)
    top_idx = np.asarray(top_idx)
    
    batch_shape = u_profile.shape[:-1]
    ebwd = np.zeros(batch_shape, dtype=float)
    
    # Process each grid point
    for idx in np.ndindex(batch_shape):
        bot = bottom_idx[idx] if bottom_idx.ndim > 0 else bottom_idx
        top = top_idx[idx] if top_idx.ndim > 0 else top_idx
        
        if bot == -1 or top == -1 or bot > top:
            # Invalid layer - leave as 0
            continue
            
        # Compute bulk wind difference
        u_bot = u_profile[idx][bot] if u_profile.ndim > 1 else u_profile[bot]
        v_bot = v_profile[idx][bot] if v_profile.ndim > 1 else v_profile[bot]
        u_top = u_profile[idx][top] if u_profile.ndim > 1 else u_profile[top]
        v_top = v_profile[idx][top] if v_profile.ndim > 1 else v_profile[top]
        
        du = u_top - u_bot
        dv = v_top - v_bot
        
        if u_profile.ndim > 1:
            ebwd[idx] = np.sqrt(du**2 + dv**2)
        else:
            ebwd = np.sqrt(du**2 + dv**2)
            
    return ebwd


def compute_effective_layer_srh(u_profile: np.ndarray, v_profile: np.ndarray,
                               storm_motion_u: np.ndarray, storm_motion_v: np.ndarray,
                               bottom_idx: np.ndarray, top_idx: np.ndarray,
                               heights: np.ndarray) -> np.ndarray:
    """
    Compute storm-relative helicity over effective layer
    
    Args:
        u_profile: U-wind component profile (m/s), shape (..., levels)
        v_profile: V-wind component profile (m/s), shape (..., levels)
        storm_motion_u: Storm motion U-component (m/s)
        storm_motion_v: Storm motion V-component (m/s)
        bottom_idx: Bottom level indices of effective layer
        top_idx: Top level indices of effective layer
        heights: Height values for each level (m AGL)
        
    Returns:
        Effective storm-relative helicity (m²/s²)
    """
    u_profile = np.asarray(u_profile)
    v_profile = np.asarray(v_profile)
    heights = np.asarray(heights)
    
    batch_shape = u_profile.shape[:-1]
    esrh = np.zeros(batch_shape, dtype=float)
    
    # Process each grid point
    for idx in np.ndindex(batch_shape):
        bot = bottom_idx[idx] if bottom_idx.ndim > 0 else bottom_idx
        top = top_idx[idx] if top_idx.ndim > 0 else top_idx
        
        if bot == -1 or top == -1 or bot >= top:
            # Invalid layer - leave as 0
            continue
            
        # Extract layer winds
        layer_u = u_profile[idx][bot:top+1] if u_profile.ndim > 1 else u_profile[bot:top+1]
        layer_v = v_profile[idx][bot:top+1] if v_profile.ndim > 1 else v_profile[bot:top+1]
        layer_heights = heights[bot:top+1]
        
        # Convert to storm-relative winds
        sr_u = layer_u - storm_motion_u
        sr_v = layer_v - storm_motion_v
        
        # Compute SRH using trapezoidal integration
        # SRH = ∫(v⃗ₛᵣ × dv⃗/dz) dz
        if len(layer_heights) < 2:
            continue
            
        srh_sum = 0.0
        for i in range(len(layer_heights) - 1):
            # Height difference
            dz = layer_heights[i+1] - layer_heights[i]
            if dz <= 0:
                continue
                
            # Wind shear vector
            du_dz = (sr_u[i+1] - sr_u[i]) / dz
            dv_dz = (sr_v[i+1] - sr_v[i]) / dz
            
            # Average storm-relative wind in layer
            avg_sr_u = 0.5 * (sr_u[i] + sr_u[i+1])
            avg_sr_v = 0.5 * (sr_v[i] + sr_v[i+1])
            
            # Cross product: v⃗ₛᵣ × (dv⃗/dz)
            cross_product = avg_sr_u * dv_dz - avg_sr_v * du_dz
            
            # Integrate
            srh_sum += cross_product * dz
            
        if u_profile.ndim > 1:
            esrh[idx] = srh_sum
        else:
            esrh = srh_sum
            
    return esrh