# Agronomy and AI Engineering
## Scientific model layer
Crop growth/phenology; ET0 and crop coefficients; soil-water/root-zone balance; nutrient budgets and uptake; disease/pest epidemiology; IPM; yield and quality. Candidate models: FAO AquaCrop, FAO-56 Penman–Monteith, DSSAT, APSIM, PCSE. Evaluate crop coverage, license, calibration and local validity.

## AI/ML layer
Crop/weed/pest/disease detection; segmentation; plant emergence; canopy and biomass; stress and deficiency evidence; fruit count/maturity; yield forecast; irrigation demand; anomaly detection. Use PyTorch, OpenCV and ONNX Runtime. Dataset cards must document source/license/consent, crop/cultivar, geography, stage, label quality, bias and train/validation/test split. Split by farm/time to prevent leakage.

## Agent layer
Farm Planning, Soil, Crop Selection, Weather, Irrigation, Nutrition, Disease, Pest, Weed, Drone Mission, Robot Fleet, Crop Growth, Harvest, Market, Profit Optimization, Safety/Compliance and Farm Supervisor.

## Guardrails
LLMs explain, retrieve and coordinate; they do not invent pesticide mixtures/doses, fertilizer quantities or irrigation volumes. Recommendations require evidence, assumptions, confidence/uncertainty, model version, contraindications, approval state and outcome tracking. Abstain when evidence is insufficient. Agronomy requires local trials, lab/field ground truth and qualified review.
