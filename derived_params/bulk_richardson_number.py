from .common import *

def bulk_richardson_number(cape: np.ndarray, wind_shear: np.ndarray) -> np.ndarray:
    """
    Compute Bulk Richardson Number (BRN) with explicit shear definition
    
    BRN = CAPE / (0.5 × |ΔV|²)
    
    NEW v2.2: Enhanced documentation clarifies shear definition and provides
    comprehensive operational guidance for storm-type forecasting.
    
    Args:
        cape: CAPE (J/kg) - convective available potential energy
        wind_shear: Bulk wind shear MAGNITUDE (m/s) - see definition below
        
    Returns:
        BRN values (dimensionless)
        
    Shear Definition (CRITICAL):
        wind_shear = |ΔV| = |V(top) - V(bottom)| 
        
        Where V is the wind vector at specified levels:
        - Standard: 0-6 km bulk wind difference magnitude
        - Alternative: 0-3 km for low-topped convection
        - Alternative: Effective layer wind difference (preferred when available)
        
        INPUT REQUIREMENT: Provide the MAGNITUDE of the wind vector difference,
        not the scalar difference of wind speeds.
        
        Example calculation:
            u_6km = 20 m/s, v_6km = 10 m/s  (wind at 6 km)
            u_sfc = 5 m/s,  v_sfc = 3 m/s   (surface wind)
            
            ΔU = u_6km - u_sfc = 15 m/s
            ΔV = v_6km - v_sfc = 7 m/s
            
            wind_shear = √(ΔU² + ΔV²) = √(15² + 7²) = 16.6 m/s
    
    Physical Interpretation:
        BRN represents the ratio of buoyant energy to kinetic energy in the shear flow.
        It determines the balance between updraft strength and shear-induced rotation.
        
    Operational Thresholds:
        BRN < 10:    Extreme shear environment
                     - May disrupt updraft development  
                     - Linear storm modes favored
                     - Squall lines, bow echoes possible
                     
        BRN 10-45:   Optimal supercell environment
                     - Balance of instability and shear
                     - Rotating updrafts favored
                     - Classic supercell potential
                     - Tornado risk enhanced
                     
        BRN > 50:    Weak shear environment
                     - High instability, low organization
                     - Pulse thunderstorms favored
                     - Multicell clusters possible
                     - Limited tornado threat
                     
        BRN > 100:   Very weak shear
                     - Air mass thunderstorms
                     - Minimal organization
                     - Flash flood potential from training
    
    References:
        Weisman & Klemp (1982): Supercell morphology and propagation
        Rasmussen & Blanchard (1998): Severe storm parameter climatology
        Thompson et al. (2003): Effective bulk shear and supercells
        
    Notes:
        - Originally developed for idealized supercell simulations
        - Most effective when combined with CAPE, SRH, and LCL height
        - Consider effective layer shear when available for improved accuracy
    """
    
    # ========================================================================
    # BRN CALCULATION WITH EXPLICIT SHEAR HANDLING
    # ========================================================================
    # BRN formula: CAPE / (0.5 × |ΔV|²)
    # Where |ΔV| is the bulk wind shear vector MAGNITUDE (not scalar difference)
    
    # Validate shear input
    if np.any(wind_shear < 0):
        print("⚠️ BRN: Negative shear values detected - using absolute values")
        wind_shear = np.abs(wind_shear)
    
    # Kinetic energy term: KE = 0.5 × |ΔV|²
    # Apply minimum shear threshold to prevent unrealistic BRN values
    min_shear = 1.0  # m/s - below this is essentially no-shear environment
    shear_magnitude = np.maximum(wind_shear, min_shear)
    kinetic_energy_term = 0.5 * shear_magnitude**2
    
    # BRN calculation
    brn = cape / kinetic_energy_term
    
    # ========================================================================
    # QUALITY CONTROL AND PHYSICAL CONSTRAINTS
    # ========================================================================
    
    # No CAPE = no convection = BRN irrelevant
    brn = np.where(cape <= 0, 0.0, brn)
    
    # Cap at 999 for display purposes (BRN > 100 all indicates weak shear)
    # This prevents numerical artifacts from near-zero shear
    brn = np.minimum(brn, 999.0)
    
    # Mask invalid input data
    valid_mask = (
        np.isfinite(cape) & (cape >= 0) &
        np.isfinite(wind_shear) & (wind_shear >= 0)
    )
    brn = np.where(valid_mask, brn, np.nan)
    
    # ========================================================================
    # DIAGNOSTIC OUTPUT
    # ========================================================================
    
    # Log extreme values for quality monitoring
    extreme_shear = np.any(wind_shear > 40)  # Very high shear
    extreme_cape = np.any(cape > 4000)       # Very high CAPE
    
    if extreme_shear:
        max_shear = np.nanmax(wind_shear)
        print(f"🔍 BRN: Extreme shear detected, max = {max_shear:.1f} m/s")
    
    if extreme_cape:
        max_cape = np.nanmax(cape)
        print(f"🔍 BRN: Extreme CAPE detected, max = {max_cape:.0f} J/kg")
    
    return brn
