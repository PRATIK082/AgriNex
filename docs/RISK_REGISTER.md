# Initial Risk Register
| Risk | Impact | Mitigation |
|---|---|---|
| Wrong agronomic advice | Crop loss/unsafe inputs | Scientific rules, expert review, local trials, uncertainty/abstention |
| CV domain shift | Missed disease/weed | Diverse field data, ground truth, monitoring, human review |
| Sensor calibration | Wrong irrigation/nutrition | Calibration, lab checks, quality flags |
| GNSS loss/multipath | Unsafe robot path | Sensor fusion, operating limits, local safe stop |
| Person/animal collision | Severe injury | Independent protective systems, exclusion zones, supervised tests |
| Chemical drift/misapplication | Health/environment/crop harm | Labels, operator authorization, weather/buffer checks, audit |
| Connectivity loss | Interrupted missions | Edge autonomy, local safety, offline recovery |
| Battery/mechanical failure | Injury/property loss | Engineering analysis, BMS, inspection |
| Vendor lock-in | Limited adoption | Adapters, open formats, integration tests |
| License conflict | Legal/reputation | Provenance/license audit |
| Privacy breach | Loss of trust/legal exposure | Minimization, RBAC, encryption, retention |
| Market forecast error | Financial loss | Backtests, intervals, downside scenarios |
| Poor unit economics | Non-viable product | Pilot cost tracking, service model |
| Regulatory change | Non-compliance | Jurisdiction register and change monitoring |
| Simulation-to-field gap | Unsafe/ineffective operation | Calibration, HIL, staged field tests |

This is brainstorming, not a completed risk assessment. Assign owner, severity, likelihood, detectability and residual risk for each deployment.
