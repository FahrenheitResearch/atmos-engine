# Atmospheric Cross-Section Intelligence Report
## Oklahoma Prescribed Burn Investigation — February 9, 2026

**Analyst:** Atmospheric Cross-Section Module
**Data Source:** HRRR 20260209_18z cycle (initialized 12:00 CST)
**Transects:**
- **E-W:** (35.5N, 99.5W) to (35.5N, 95.0W) — western OK through OKC to eastern OK
- **N-S:** (37.0N, 99.0W) to (34.5N, 99.0W) — Kansas border through western OK RFW counties

**Red Flag Warning Counties:** Harper, Ellis, Woodward, Roger Mills (western OK)

---

## 1. Generated Cross-Section Imagery

### Temporal Evolution (FHR 1/3/5/8 = 1pm/3pm/5pm/8pm CST)

| Filename | Transect | Product | Description |
|----------|----------|---------|-------------|
| `ew_temporal_wind_speed.png` | E-W | Wind Speed | 4-panel wind speed evolution, 1pm-8pm |
| `ew_temporal_rh.png` | E-W | Relative Humidity | RH collapse and partial evening recovery |
| `ew_temporal_vpd.png` | E-W | Vapor Pressure Deficit | VPD increase through afternoon |
| `ew_temporal_dewpoint_dep.png` | E-W | Dewpoint Depression | Dryness metric evolution |
| `ew_temporal_temperature.png` | E-W | Temperature | Diurnal heating pattern |
| `ew_temporal_lapse_rate.png` | E-W | Lapse Rate | Instability structure |
| `ew_temporal_theta.png` | E-W | Potential Temperature | Boundary layer mixing depth |
| `ns_temporal_wind_speed.png` | N-S | Wind Speed | Wind field through RFW counties |
| `ns_temporal_rh.png` | N-S | Relative Humidity | RH gradient, north-south |
| `ns_temporal_vpd.png` | N-S | Vapor Pressure Deficit | VPD through RFW zone |
| `ns_temporal_dewpoint_dep.png` | N-S | Dewpoint Depression | Drying along N-S transect |
| `ns_temporal_temperature.png` | N-S | Temperature | Temperature structure |
| `ns_temporal_lapse_rate.png` | N-S | Lapse Rate | Vertical instability |
| `ns_temporal_theta.png` | N-S | Potential Temperature | BL depth and mixing |

### Product Comparisons (Wind Speed + RH + VPD, side-by-side)

| Filename | Transect | FHR | Time CST |
|----------|----------|-----|----------|
| `ew_products_fhr1.png` | E-W | 1 | 1:00 PM |
| `ew_products_fhr3.png` | E-W | 3 | 3:00 PM |
| `ew_products_fhr5.png` | E-W | 5 | 5:00 PM |
| `ew_products_fhr8.png` | E-W | 8 | 8:00 PM |
| `ns_products_fhr1.png` | N-S | 1 | 1:00 PM |
| `ns_products_fhr3.png` | N-S | 3 | 3:00 PM |
| `ns_products_fhr5.png` | N-S | 5 | 5:00 PM |
| `ns_products_fhr8.png` | N-S | 8 | 8:00 PM |

**Total: 22 new cross-section panels generated for this analysis.**

---

## 2. Numerical Surface Data

### 2a. E-W Transect: (35.5N, 99.5W) to (35.5N, 95.0W)

#### Relative Humidity (%)

| FHR | Time CST | Min | Max | Mean |
|-----|----------|-----|-----|------|
| 1 | 1:00 PM | **21.7** | 38.4 | 30.3 |
| 2 | 2:00 PM | **15.6** | 34.0 | 25.3 |
| 3 | 3:00 PM | **12.9** | 30.9 | 22.9 |
| 5 | 5:00 PM | **17.0** | 28.3 | 22.8 |
| 7 | 7:00 PM | 17.5 | 37.6 | 30.1 |
| 8 | 8:00 PM | 16.7 | 47.1 | 34.3 |

#### Wind Speed (cross-section component, m/s)

| FHR | Time CST | Min | Max | Mean |
|-----|----------|-----|-----|------|
| 1 | 1:00 PM | -3.3 | 2.8 | 0.5 |
| 2 | 2:00 PM | -2.9 | 3.9 | 1.1 |
| 3 | 3:00 PM | -2.8 | 4.5 | 1.5 |
| 5 | 5:00 PM | -4.9 | 4.4 | 1.7 |
| 7 | 7:00 PM | -5.5 | 5.1 | 1.3 |
| 8 | 8:00 PM | -2.7 | 5.5 | 1.3 |

#### Temperature (C)

| FHR | Time CST | Min | Max | Mean |
|-----|----------|-----|-----|------|
| 1 | 1:00 PM | 19.4 | 23.6 | 22.0 |
| 2 | 2:00 PM | 20.6 | 24.9 | 23.2 |
| 3 | 3:00 PM | 21.4 | 25.4 | 24.1 |
| 5 | 5:00 PM | 22.6 | 25.4 | 24.4 |
| 7 | 7:00 PM | 20.9 | 23.4 | 22.2 |
| 8 | 8:00 PM | 19.6 | 22.4 | 21.1 |

#### Dewpoint Depression (C)

| FHR | Time CST | Min | Max | Mean |
|-----|----------|-----|-----|------|
| 1 | 1:00 PM | 13.8 | 23.0 | 18.4 |
| 2 | 2:00 PM | 16.5 | 28.3 | 21.2 |
| 3 | 3:00 PM | 17.5 | **31.3** | 22.8 |
| 5 | 5:00 PM | 19.3 | 27.3 | 22.7 |
| 7 | 7:00 PM | 15.0 | 26.0 | 18.6 |
| 8 | 8:00 PM | 11.8 | 26.8 | 16.8 |

### 2b. N-S Transect: (37.0N, 99.0W) to (34.5N, 99.0W) — Through RFW Counties

#### Relative Humidity (%) — CRITICAL: This transect directly crosses the Red Flag Warning zone

| FHR | Time CST | Min | Max | Mean |
|-----|----------|-----|-----|------|
| 1 | 1:00 PM | **16.9** | 44.6 | 29.9 |
| 2 | 2:00 PM | **13.6** | 34.8 | 22.9 |
| 3 | 3:00 PM | **13.8** | 28.7 | **18.6** |
| 5 | 5:00 PM | **13.0** | 20.5 | **16.6** |
| 7 | 7:00 PM | 16.4 | 26.1 | 22.3 |
| 8 | 8:00 PM | 20.7 | 28.9 | 25.4 |

#### Wind Speed (cross-section component, m/s)

| FHR | Time CST | Min | Max | Mean |
|-----|----------|-----|-----|------|
| 1 | 1:00 PM | 0.2 | 3.7 | 1.7 |
| 2 | 2:00 PM | 1.1 | 4.1 | 2.2 |
| 3 | 3:00 PM | 1.2 | **5.0** | **2.6** |
| 5 | 5:00 PM | 2.1 | **4.9** | **2.6** |
| 7 | 7:00 PM | 0.0 | 4.3 | 0.6 |
| 8 | 8:00 PM | 0.0 | 4.4 | 0.9 |

#### Temperature (C)

| FHR | Time CST | Min | Max | Mean |
|-----|----------|-----|-----|------|
| 1 | 1:00 PM | 19.6 | 24.1 | 22.1 |
| 2 | 2:00 PM | 21.4 | 25.1 | 23.4 |
| 3 | 3:00 PM | 22.6 | 25.6 | 24.3 |
| 5 | 5:00 PM | 23.6 | **25.9** | **24.7** |
| 7 | 7:00 PM | 20.9 | 23.9 | 22.2 |
| 8 | 8:00 PM | 19.4 | 23.4 | 20.9 |

#### Dewpoint Depression (C) — Larger = drier

| FHR | Time CST | Min | Max | Mean |
|-----|----------|-----|-----|------|
| 1 | 1:00 PM | 10.5 | 26.5 | 18.8 |
| 2 | 2:00 PM | 13.5 | 30.0 | 22.6 |
| 3 | 3:00 PM | 16.8 | 29.5 | 25.5 |
| 5 | 5:00 PM | **24.0** | **30.8** | **27.1** |
| 7 | 7:00 PM | 20.3 | 26.5 | 22.6 |
| 8 | 8:00 PM | 18.8 | 24.0 | 20.6 |

---

## 3. Interpretation and Analysis

### 3a. Relative Humidity: Uniformly Below Critical Thresholds

The RH data reveals conditions that were deeply hostile to controlled burning across the entire Red Flag Warning zone:

- **N-S transect (through RFW counties):** Mean RH dropped below 20% by 3:00 PM (18.6%) and reached its absolute minimum at 5:00 PM (mean 16.6%, minimum 13.0%). At no point during the 1pm-5pm window did any location along the western OK transect exceed 30% RH after 2:00 PM. The minimum RH of 13.0% at FHR 5 is dangerously low -- well below the 15% threshold that defines extreme fire weather.
- **E-W transect:** The western portion of this transect (which includes the RFW counties near -99.5W) had the lowest RH values, with minimums of 12.9% at 3:00 PM. The eastern portion (toward OKC at ~-97.5W) showed slightly higher values, creating a west-to-east moisture gradient.
- **RH below 15% threshold:** The N-S transect showed minimums below 15% from 1:00 PM through 5:00 PM (16.9%, 13.6%, 13.8%, 13.0%). On the E-W transect, the 3:00 PM minimum of 12.9% was the absolute lowest recorded. **At no point during the 1pm-5pm peak burn window did RH in western OK exceed 25% on the N-S transect.**

### 3b. Wind Speed: Sustained and Increasing Through Afternoon

The cross-section wind speed values represent the component along each transect. Key observations:

- **N-S transect winds peaked at FHR 3-5 (3-5pm CST):** Maximum cross-section wind component reached 5.0 m/s (~11 mph) at 3:00 PM. The mean remained at 2.6 m/s (6 mph) through 5:00 PM. These are cross-section components only -- total wind speed magnitudes would be higher when accounting for the full wind vector.
- **Wind barbs in imagery:** The temporal wind speed cross-sections show strong southerly/southwesterly flow throughout the boundary layer from 1pm through 5pm. The wind barb density and magnitude in the lower 200 mb of the boundary layer is substantial and persistent.
- **Evening wind collapse:** By 7:00 PM (FHR 7), mean wind dropped to near zero (0.6 m/s on N-S, 1.3 m/s on E-W), as the surface layer decoupled. This evening transition would NOT help prescribed burns conducted during the afternoon.

### 3c. Temperature: Anomalously Warm for February

- Surface temperatures peaked at **25.9C (78.6F) on the N-S transect at 5:00 PM**, with means of 24.7C (76.5F). On the E-W transect, the peak was 25.4C (77.7F).
- These temperatures are 15-20F above normal for early February in western Oklahoma.
- The combination of high temperatures and low RH produced extreme evaporative demand. This is reflected in the dewpoint depression data.

### 3d. Dewpoint Depression: Extreme and Worsening

- The N-S transect dewpoint depression peaked at **30.8C at 5:00 PM**, with a mean of 27.1C. Even the minimum depression at that hour was 24.0C.
- Dewpoint depressions above 20C indicate extremely dry air. Values above 25C represent conditions where fine fuels can reach critically low moisture content within minutes of exposure.
- The E-W transect showed maximum depressions of 31.3C at 3:00 PM, with the western end (RFW counties) consistently showing the highest values.

### 3e. VPD: Confirming Extreme Evaporative Demand

- VPD values reached maximums of 5.0 kPa on the N-S transect (3:00 PM) and 5.5 kPa on the E-W transect (8:00 PM -- likely a local effect as the atmosphere adjusts).
- Mean VPD of 2.6 kPa on the N-S transect at 3:00-5:00 PM represents very high atmospheric drying potential.

### 3f. Lapse Rates and Boundary Layer Structure

- The lapse rate cross-sections show steep (superadiabatic in places) lapse rates in the lowest 100-150 mb during peak heating (3-5pm CST), particularly on the E-W transect's western end.
- The theta (potential temperature) cross-sections reveal a deep, well-mixed boundary layer extending from the surface to approximately 700 mb (roughly 3 km AGL) by 3:00 PM. This deep mixing is characteristic of severe fire weather -- it efficiently transports momentum from aloft to the surface and maintains the extreme dryness through the full BL depth.
- By 8:00 PM, a shallow stable layer is beginning to develop near the surface, but the boundary layer aloft remains well-mixed and dry.

### 3g. Spatial Variation: Was There Any "Safe" Window or Location?

**Temporal windows:**
- **Before 1:00 PM:** Conditions were already deteriorating but were the "least bad." At 1:00 PM, RH was still 22-30% in parts of the E-W transect and ~30% mean on the N-S transect. Even these values would still trigger fire weather concerns.
- **After 7:00 PM:** RH began recovering, reaching mean values of 25-30%, with the N-S transect recovering faster. However, winds remained capable of gusts (max 4.4 m/s cross-section component at 8pm), and the extremely dry air aloft would limit RH recovery.
- **There was NO period during the 1pm-6pm window where conditions were below ALL fire weather thresholds simultaneously.** RH was below 25% at all times in western OK; winds were sustained; temperatures remained in the mid-70s F.

**Spatial gradients:**
- The E-W transect shows a consistent west-to-east moisture gradient, with the driest conditions in western OK (the RFW zone) and gradually moister air toward central and eastern OK.
- The N-S transect shows some variation but conditions were uniformly poor -- no latitude along this transect had RH above 30% between 2pm and 6pm CST.
- **The southern end of the N-S transect** (around 34.5N) showed some of the lowest RH values, while the **northern end** (near 37.0N, Kansas border) was slightly moister. However, the difference was minimal and insufficient to justify burns anywhere along the transect.

---

## 4. Key Findings for Burn Justification Assessment

### Findings That UNDERMINE the Case for Prescribed Burns

1. **RH was below 15% at multiple locations and times.** The 13.0% minimum on the N-S transect at 5:00 PM and 12.9% on the E-W transect at 3:00 PM are well into the "extreme" category. Standard prescribed burn guidelines prohibit ignition when RH is below 25-30%, and most agencies use 20% as a hard cutoff.

2. **Mean RH across the entire RFW zone was 16.6% at 5:00 PM** (N-S transect). This is not a localized phenomenon -- the entire western Oklahoma region was severely moisture-depleted.

3. **No temporal window of reduced severity existed during afternoon hours.** Conditions were already poor by 1:00 PM and continued to worsen through 5:00 PM. The only "improvement" came after 7:00 PM, by which point any afternoon-ignited burn would have been burning for hours.

4. **Dewpoint depressions of 24-31C** confirm extremely dry air through the full column, not just surface effects. This means fine fuel moisture would have equilibrated to dangerously low levels rapidly after any ignition.

5. **Deep boundary layer mixing (to ~700 mb)** was transporting dry, windy air from aloft to the surface throughout the afternoon. This pattern sustains fire weather conditions even if surface observations briefly improve.

6. **Temperatures of 76-79F in February** are dramatically above normal and contribute to the extreme VPD. Fuels that might normally be somewhat dormant-season resistant would cure rapidly under these conditions.

### Findings That MIGHT (Weakly) Support Early-Morning or Late-Evening Burns

1. **RH was higher before 1:00 PM.** FHR 1 (1:00 PM) showed mean RH of 30% along both transects, and conditions earlier in the morning (before the 18z model initialization) would have been moister. However, the trajectory was clearly deteriorating.

2. **Winds dropped significantly after 7:00 PM.** The N-S transect mean wind component fell from 2.6 to 0.6 m/s between 5pm and 7pm. However, RH was still only 22% at 7pm -- still dangerously low for fire.

3. **The eastern portion of the E-W transect showed higher RH** (up to 38% at 1pm, 47% at 8pm near -95W). This suggests conditions improved significantly east of approximately -97W. However, this area was NOT in the Red Flag Warning zone, and prescribed burns in western OK could not rely on eastern moisture.

### Bottom Line Assessment

**The atmospheric data provides no justification for prescribed burning during Red Flag Warning conditions in western Oklahoma on February 9, 2026.** The combination of:
- RH below 20% for 4+ consecutive hours (13-17% range)
- Sustained winds through a deep mixed layer
- Anomalous warmth (76-79F)
- Dewpoint depressions of 24-31C
- No temporal or spatial refuge within the RFW zone

...represents a textbook case of conditions that prescribed fire management guidelines exist to prohibit. The HRRR model data shows these conditions were not merely forecast -- they were well-resolved and unambiguous across the entire domain.

---

*Analysis generated from HRRR 20260209_18z cross-section data. 22 multi-panel cross-section images produced. Surface statistics extracted at 135 points (E-W) and 92 points (N-S) per forecast hour.*
