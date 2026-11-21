# Agronomy and AI Engineering

## Scientific model layer
Crop growth/phenology; ET0 and crop coefficients; soil-water/root-zone balance; nutrient budgets and uptake; disease/pest epidemiology; integrated pest management; yield and quality. Candidate models: FAO AquaCrop, FAO-56 Penman–Monteith, DSSAT, APSIM and PCSE. Evaluate crop coverage, license, calibration and local validity.

## AI/ML layer
Crop/weed/pest/disease detection and segmentation; emergence; canopy/biomass; stress/deficiency evidence; fruit count/maturity; yield forecast; irrigation demand; anomaly detection. Candidates: PyTorch, OpenCV, ONNX Runtime. Dataset cards document source/license/consent, crop/cultivar, geography, stage, label quality, bias and splits. Split by farm/time to prevent leakage.

## Agent layer
Farm Planning, Soil, Crop Selection, Weather, Irrigation, Nutrition, Disease, Pest, Weed, Drone Mission, Robot Fleet, Crop Growth, Harvest, Market, Profit Optimization, Safety/Compliance and Farm Supervisor.

## Guardrails
LLMs explain, retrieve and coordinate; they do not invent pesticide mixtures/doses, fertilizer quantities or irrigation volumes. Recommendations require evidence, assumptions, uncertainty, model version, contraindications, approval and outcome tracking. Abstain when evidence is insufficient. Require local trials, ground truth and qualified agronomy review.
