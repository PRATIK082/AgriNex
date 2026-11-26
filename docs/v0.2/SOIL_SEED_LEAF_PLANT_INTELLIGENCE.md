# Soil, Seed, Leaf & Plant Intelligence System
**Research and requirements proposal | 2026-11-26 | AgriNex V0.2 capability design**

## 1. Vision and system boundary

Build an integrated diagnostic and decision-support system spanning:
1. Soil sampling, portable field testing and accredited/competent laboratory analysis.
2. Seed-lot screening, germination/vigour testing and seedling establishment.
3. Leaf/tissue analysis and optical leaf scanning.
4. Plant identity, age, phenological stage and longitudinal growth monitoring.
5. Crop-, cultivar-, location-, soil-, water- and stage-aware nutrient planning.
6. Mobile app, web console, interoperable APIs, reports and subscription entitlements.

This is a cross-module capability, not a new isolated silo. AGX-04 owns soil diagnostics; AGX-06 owns seed/planting records; AGX-12 owns imagery and crop health; AGX-03 owns evidence synthesis/advisory; AGX-08 owns nutrient plans and application records; AGX-01 owns field/zone geometry and crop-cycle identity; AGX-02 owns sensor/lab ingestion and provenance.

**Critical distinction:** device readings, lab measurements, image-derived indicators, model estimates and agronomist conclusions are different evidence classes. Store and display them separately. A phone camera or low-cost probe must never be represented as a certified laboratory result.

## 2. Soil intelligence — full parameter catalogue

The Indian Soil Health Card programme provides a practical minimum reference set: available N, P, K, S; Zn, Fe, Cu, Mn, B; pH, EC and organic carbon. Government/ICAR sources describe these 12 parameters and crop-specific nutrient advice. AgriNex should support this baseline plus optional extended panels rather than stopping at NPK.

### 2.1 Chemical and fertility panel

| Group | Parameters | Notes |
|---|---|---|
| Core SHC nutrients | Available N, available P, available K, available S | Record extraction method and reporting basis; available fractions are not total elemental content |
| SHC micronutrients | Zn, Fe, Cu, Mn, B | Method- and soil-pH-dependent interpretation |
| Soil reaction/salinity | pH, electrical conductivity (EC) | Record soil:water ratio/extract method, temperature compensation and units |
| Carbon/organic matter | Organic carbon (OC), organic matter (OM) where method supports it | Do not assume OM = OC × universal factor without documenting method |
| Extended secondary nutrients | Ca, Mg, Na; exchangeable sodium percentage (ESP), sodium adsorption ratio (SAR) where relevant | Particularly useful for sodicity, irrigation and soil amendment assessment |
| Extended micronutrients | Mo, Cl, Ni and crop-specific elements | Enable only where crop, soil, deficiency or contamination context justifies |
| Exchange/buffering | Cation exchange capacity (CEC), exchangeable bases, base saturation, buffering capacity | Method-specific laboratory panel |
| Carbonate/alkalinity | CaCO3/free lime, bicarbonate/carbonate, gypsum requirement or lime requirement | Select based on soil diagnosis and method |
| Contamination/safety | Selected heavy metals/metalloids, pesticide residues, hydrocarbons or other contaminants | Separate environmental laboratory workflow; not a routine fertility scan |

### 2.2 Physical and hydrological panel

- Texture: sand, silt, clay fractions and textural class.
- Structure/aggregate stability, crusting, compaction and penetration resistance.
- Bulk density and particle density; porosity derived only with stated assumptions.
- Gravimetric and volumetric water content; field capacity, permanent wilting point and plant-available water where measured.
- Infiltration rate, saturated hydraulic conductivity, drainage/permeability and water-holding capacity.
- Soil temperature, profile moisture, depth/horizon, rooting depth and restrictive layers.
- Erosion indicators, slope, surface cover, runoff and waterlogging observations.

### 2.3 Biological and soil-health panel

- Soil respiration/basal respiration, microbial biomass carbon/nitrogen and selected enzyme activities.
- Potentially mineralizable nitrogen and other validated mineralization indicators.
- Earthworm abundance/biomass, root health and selected soil fauna indicators.
- Microbial community/functional assays only where validated, with clear method and interpretation limits.
- Organic residue, cover crop and biological management history.

Biological indicators are highly method-, season-, moisture- and temperature-sensitive. Do not collapse them into a single universal “soil score” without a documented model and local validation.

### 2.4 Device and laboratory architecture

Use a **hybrid instrument**, not a claim that one probe directly measures every parameter:

- Core electronic sensors: pH electrode, EC/conductivity, soil temperature and moisture; optional oxidation-reduction potential where justified.
- Selective electrochemical/ion-selective modules: candidate nitrate/ammonium/potassium sensors only after interference, drift, matrix and calibration validation. Phosphate and micronutrient measurement may require dedicated chemistry.
- Reagent/cartridge chemistry: controlled colorimetric or photometric assays for analytes where validated; record reagent lot, expiry, blank, calibration curve, sample mass, extraction ratio, reaction time and temperature.
- Optical spectroscopy: VIS-NIR/SWIR or other spectral modules can estimate selected properties only after calibration against reference laboratory data across soil types, moisture, texture, organic matter and geography.
- Physical field tools: penetrometer, infiltration ring, bulk-density core, soil thermometer/moisture probe and documented texture method.
- Laboratory pathway: reference methods for OC, available nutrients, micronutrients, CEC, texture, bulk density, contaminants and biological assays.

Every device result must include device model/serial, firmware, sensor/cartridge ID, calibration status, operator, sample preparation, temperature, timestamp, coordinates, depth, replicate readings, raw signal where possible, method ID, units, uncertainty/quality flags and reference-lab comparison status.

**Do not promise every parameter as instant in-situ measurement.** Soil sensors and smartphone colorimetry have calibration, matrix-interference, precision and reproducibility limits. The product should return “not supported by this device/method” rather than fabricate a value.

## 3. Seed intelligence and seed scanner

### 3.1 Seed lot registry
Capture crop/species, cultivar/hybrid, supplier, source, lot/batch, production/packing date, treatment/coating, label/claim, storage conditions, expiry/validity, certification/document references, purchase and field allocation.

### 3.2 Scanner / imaging capabilities
A controlled-light seed imaging chamber can screen and quantify:
- Count, size, length/width, shape, colour distribution and visible uniformity.
- Broken, shrivelled, discoloured, insect-damaged, visibly mouldy or foreign-material candidates.
- Image-derived seed grading/classification with confidence and manual correction.
- Lot-level variation and sample traceability.

Camera screening cannot reliably establish internal viability, genetic purity, pathogen freedom or certified germination. These require validated laboratory protocols.

### 3.3 Seed quality tests
- Representative sampling and sample identity/chain of custody.
- Physical purity and inert matter/other seed fractions.
- Moisture content.
- Standard germination: normal/abnormal seedlings, hard/fresh/dead seeds as method defines.
- Seed vigour: validated accelerated ageing, electrical conductivity, tetrazolium or crop-specific tests.
- Seed health/pathogen testing and insect damage.
- Cultivar/genuineness testing using suitable molecular or other accepted methods when needed.
- Seedling emergence and establishment in a field/controlled substrate.

Follow applicable Indian Seeds Act/Rules, notified crop standards and recognized ISTA methods where relevant. Do not issue a statutory certification or label claim unless the authorized process and laboratory requirements are met.

## 4. Leaf scanner and plant tissue intelligence

### 4.1 Optical leaf scanner
Provide a guided capture hood/clip or handheld scanner with fixed geometry, controlled illumination, white/dark reference and colour target. Start with RGB and a calibrated chlorophyll/SPAD-like sensor; evaluate multispectral/red-edge/NIR and fluorescence as separate research options.

Potential derived indicators:
- Colour/chlorosis/necrosis, lesion area, leaf area and shape.
- Chlorophyll-related indices and canopy greenness.
- Leaf temperature (if thermal sensor is included).
- Spectral indices correlated with pigment, water status or nutrient status.
- Disease/pest symptom candidates and stress signatures.

These are **indirect indicators**, not direct elemental assays. Spectral signals are affected by cultivar, leaf age, lighting, water stress, disease, temperature, dust, camera and growth stage. Train/validate against paired tissue laboratory chemistry and field observations. The model must return uncertainty or abstain for unsupported crops/devices/stages.

### 4.2 Laboratory leaf/tissue panel
Support crop-specific lab analysis of total N, P, K, Ca, Mg, S and micronutrients Fe, Mn, Zn, Cu, B, Mo, Cl and Ni where applicable. Store blade/petiole/whole-leaf basis, dry/fresh weight basis, digestion/extraction method, units and laboratory reference range.

Sampling protocol is essential: crop, cultivar, plant part, leaf position, phenological stage, time, recent foliar spray/rain, sample count, field/zone and symptomatic vs healthy comparison must be captured. Nutrient sufficiency ranges are crop-, cultivar-, tissue- and stage-specific. Never compare a random leaf image to a laboratory sufficiency range as if equivalent.

## 5. Plant age, growth and phenology intelligence

Track both chronological age and biological stage:
- Sowing/transplant date, emergence date, planting density and plant population.
- Crop, cultivar, rootstock (where relevant), seed lot and planting method.
- Days after sowing (DAS), days after transplanting (DAT), growing degree days (GDD) with base-temperature definition.
- BBCH or crop-specific phenological stage, flowering, fruit set, grain fill, maturity and harvest.
- Plant height, stem diameter, node/internode count, leaf count/area, canopy cover, biomass proxy, growth rate and stand gaps.
- Root-zone observations, water status, weather exposure, stress events and management operations.
- Repeated images linked to persistent plant/plot identity and location.

Age alone must not determine nutrient dose. Growth stage, crop/cultivar, soil test, tissue test, irrigation-water quality, weather, yield target, previous applications and local recommendations must be considered.

## 6. Integrated nutrition decision engine

### Inputs
1. Field/zone geometry, crop, cultivar, seed lot, sowing/transplant date and current stage.
2. Soil test results with sample depth, method, date, units and quality.
3. Irrigation-water quality and water/soil salinity context.
4. Leaf/tissue lab results and scanner-derived indicators kept as distinct evidence.
5. Weather, rainfall, temperature, GDD and forecast uncertainty.
6. Crop population, growth measurements, yield target and observed performance.
7. Previous fertilizer/manure/bio-input applications, product lots and nutrient credits.
8. Product catalogue, nutrient composition, legal status, label/crop/use restrictions and compatibility evidence.
9. Locally validated recommendation tables, STCR/target-yield equations or calibrated crop models.

### Decision workflow
- Validate sample freshness, method, units, crop and growth stage.
- Detect missing/conflicting/out-of-domain evidence and request resampling or lab confirmation.
- Diagnose probable limiting factors; distinguish nutrient deficiency from water stress, salinity, pH, disease, pest, root damage and weather.
- Calculate nutrient balance and crop-stage requirement using approved local equations/rules; expose all assumptions and nutrient credits.
- Generate candidate source/product plans with elemental nutrient conversions, split timing, application method and water/soil constraints.
- Check legal label, crop, geography, product status, compatibility, safety interval and maximum application constraints.
- Return alternatives, uncertainty, evidence references, confidence, expected response range and “why”.
- Require agronomist/user approval for consequential recommendations; log actual application and post-application response.

Use Soil Test Crop Response (STCR) and other ICAR/state agricultural-university recommendations where applicable and validated. Do not apply one universal NPK ratio or global fertilizer formula to all crops. Do not autonomously trigger fertigation, pesticide use or machinery actuation from an AI output.

## 7. Reports and mobile/API experience

### Farmer report
A single report should include:
- Field/zone map and sample locations/depths.
- Soil panel: parameter, measured value, unit, method, date, interpretation range/source and quality flag.
- Seed lot quality and test evidence, if linked to the crop cycle.
- Leaf/tissue results and scanner findings shown in separate sections.
- Crop age, DAS/DAT, stage, growth timeline and observations.
- Nutrition diagnosis, nutrient balance, recommended actions, product/quantity basis, timing and application method.
- Confidence/uncertainty, missing tests, warnings, next sampling date and expert review.
- QR/report ID, version, source provenance and downloadable PDF/shareable link.

### API design
- Versioned REST API documented with OpenAPI 3.1; JSON Schema for portable event/data contracts.
- Mobile-friendly endpoints and sync: upload batches, resumable media upload, offline drafts, idempotency keys, conflict resolution and notifications.
- Standard resources: `/v1/fields`, `/v1/crop-cycles`, `/v1/samples/soil`, `/v1/soil-results`, `/v1/seed-lots`, `/v1/seed-tests`, `/v1/plant-observations`, `/v1/leaf-scans`, `/v1/tissue-results`, `/v1/nutrition-plans`, `/v1/reports`, `/v1/devices`.
- Integrate with OGC API Features/GeoJSON for spatial resources; STAC for large imagery/raster assets; SensorThings mapping for observations where useful. Avoid inventing a proprietary replacement for established standards.
- Use OAuth2/OIDC-compatible identity, tenant-scoped authorization, signed upload URLs, device identity, audit and rate limits. Never put secrets in mobile apps.
- Mobile clients should support Android-first field workflows, local language labels, offline sample capture, GPS with accuracy metadata, camera calibration guidance and delayed sync.

## 8. Subscription and packaging model

Entitlements should be configurable in a billing/entitlement service, not hard-coded into agronomy logic. Pricing, quotas and package names require customer interviews and pilot economics; the following is a product hypothesis.

| Package | Intended user | Capability bundle |
|---|---|---|
| Starter / Free | Smallholder exploring the product | Farm profile, crop calendar, manual observations, basic report viewer, limited image capture and educational guidance |
| Soil Basic | Farmer needing periodic soil insight | Standard soil panel booking/entry, sample tracking, core soil report, basic crop-specific interpretation |
| Grower | Active crop-cycle management | Soil + seed lot records, plant age/stage tracking, scheduled leaf scans, growth timeline, basic nutrient plan |
| Precision | High-value/large/managed farms | Extended soil and tissue panels, device integration, repeated scans, zone-level maps, advanced nutrition scenarios, alerts and agronomist review allowance |
| Enterprise / Lab / Partner API | FPOs, labs, agribusinesses, service providers | Multi-farm/tenant administration, lab/device fleet, role-based workflows, bulk API, white-label reports, audit/export and SLA options |

Commercial controls:
- Define per-plan limits for farms, fields, active crop cycles, tests, device seats, image storage, API calls, reports and expert consultations.
- Offer pay-per-test, sample pickup, lab partner and device rental/purchase add-ons.
- Keep core safety alerts, result provenance, data export and access to a user's own historical results available; do not hide critical safety information behind a premium tier.
- Disclose whether advice is automated or reviewed by a qualified agronomist.
- Measure unit economics: device BOM, calibration/reagent cost, lab cost, logistics, support, cloud/image storage and expert time.
- Interview smallholders, progressive growers, FPOs, agronomists, labs, dealers and service operators before fixing tiers/prices. Test willingness-to-pay, frequency and decision value.

## 9. Core data contracts

Every test/result should share:
- `result_id`, `subject_type`, `subject_id`, `field_id`, `zone_id`, `crop_cycle_id`
- `sample_id`, `sampled_at`, `received_at`, `tested_at`, `reported_at`
- `collector_id`, `operator_id`, `lab_id`, `device_id`, `device_firmware`, `method_id`, `method_version`
- `parameter_code`, `value`, `unit_code`, `basis`, `detection_limit`, `uncertainty`, `replicate_count`
- `evidence_class`: `field_sensor`, `rapid_kit`, `laboratory`, `image_derived`, `model_estimate`, `expert_review`
- `quality_status`, `calibration_status`, `reference_range_id`, `provenance`, `attachments`, `review_status`
- Immutable result version, corrections as superseding records, audit actor and reason.

Keep separate domain entities: SoilSample/SoilTestResult, SeedLot/SeedSample/SeedTest, PlantTissueSample/TissueTestResult, LeafScan/ImageAsset, PlantObservation/GrowthMetric, NutritionDiagnosis/NutrientPlan/ApplicationRecord, Device/CalibrationRecord and SubscriptionEntitlement.

## 10. Validation and quality plan

- Build reference datasets covering major Indian soil groups, crops, cultivars, seasons, irrigation regimes and management practices.
- Compare device results with competent reference laboratories using blinded paired samples, replicates and independent sites.
- Predefine accuracy, repeatability, reproducibility, bias, detection/quantification limits, drift, interference and environmental operating range per analyte.
- Validate image models across phone/device models, lighting, backgrounds, cultivars, leaf age, seasons, disease and nutrient confounders.
- Split training/test data by farm/site/time, not random adjacent images, to avoid leakage.
- Validate seed image screening against manual/lab ground truth; germination/vigour claims require the prescribed test method.
- Validate nutrient recommendations with crop-specific trials, untreated/control comparisons where ethical, replicated plots, yield/quality, nutrient-use efficiency and environmental outcomes.
- Report calibration date, model/data version, uncertainty, known limitations and out-of-domain abstention.
- Establish field-service calibration, consumable shelf-life, cleaning, sensor replacement and device traceability.

## 11. Phased delivery

**Phase A — Requirements and partnerships:** interview farmers, agronomists, labs, device vendors and FPOs; define first target crop(s), geography, user jobs and willingness-to-pay. Map Indian SHC methods and lab partner capacity.

**Phase B — Digital workflows first:** implement sample protocols, soil/tissue/seed result registry, crop-cycle timeline, PDF report, manual lab result entry and nutrition-plan draft. No custom device required to prove value.

**Phase C — Soil device proof-of-concept:** pH/EC/moisture/temperature plus one validated reagent assay; design calibration/reference-lab study. Add analytes only after evidence.

**Phase D — Leaf/seed imaging prototypes:** controlled capture fixtures, RGB image pipeline and curated ground-truth datasets; compare against lab tests and manual seed grading.

**Phase E — Crop-stage nutrition engine:** start with one crop, one region and one season using local recommendations and reviewed rules; collect field outcome evidence.

**Phase F — Mobile subscriptions and partner API:** offline Android workflow, entitlement service, lab/device partner integrations, customer support and pricing experiments.

**Phase G — Expansion:** extended chemical/physical/biological soil panels, multispectral sensing, more crops/regions, model calibration, fleet analytics and research-grade trials.

## 12. Acceptance criteria for first release

- Soil sample protocol captures location, depth, zone, method, date, collector and chain of custody.
- Supports the full Indian SHC parameter set and extensible physical, chemical and biological panels.
- Each value has method, unit, basis, evidence class and quality/provenance.
- Device estimates and laboratory results are visually and programmatically distinguishable.
- Seed lot and seed test records cover purity, moisture, germination, vigour and health evidence.
- Leaf scan stores calibrated capture metadata and reports image-derived indicators separately from tissue chemistry.
- Plant age and phenological stage are recorded independently; growth observations form a timeline.
- Nutrition plan binds crop, cultivar, stage, soil, tissue, water, weather, prior applications and approved product rules.
- Report includes raw results, interpretation source, recommendations, uncertainty, missing evidence and history.
- API contracts are versioned; mobile offline sync is idempotent and auditable.
- Subscription entitlements enforce limits without suppressing safety warnings or user data access.
- Independent field/lab validation and expert approval gates are documented before claims or automated actuation.

## 13. Research references

1. Government of India, Soil Health Card parameters and programme: https://www.pib.gov.in/newsite/erelcontent.aspx?lang=2&reg=48&relid=267668
2. PIB, ICAR essential soil quality parameters and rapid soil testing kits: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1781433&lang=2&reg=48
3. PIB, soil fertility mapping and standard soil analyses: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2110419&lang=2&reg=48
4. FAO Global Soil Partnership / soil and plant analysis assessment: https://www.fao.org/global-soil-partnership/
5. IIRS, Earth observation for soil resource assessment (chemical, physical and biological indicators): https://science.iirs.gov.in/wp-content/uploads/2025/01/EO-Soil-Resource-Assessment.pdf
6. Smartphone analytical applications for agricultural soil analysis, Analytical and Bioanalytical Chemistry (2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC10328891/
7. Review of on-site soil and plant sensors, Agriculture (2026): https://www.mdpi.com/2077-0472/16/8/883
8. TNAU seed technology and seed testing: https://www.agritech.tnau.ac.in/seed_certification/seed%20tech%20agri%20index/Seed_seedtesting.html
9. National Horticulture Board, Handbook of Seed and Planting Material Testing Manuals: https://nhb.gov.in/guideline/handbook_of_seed_and_planting_material_testing_manuals.pdf
10. University of Minnesota Extension, foliar testing and crop-specific sampling: https://extension.umn.edu/agriculture/specialty-crops/foliar-testing-for-fruit-and-vegetable-crops
11. University of Minnesota Extension, plant tissue sampling strategy and timing: https://blog-crop-news.extension.umn.edu/2023/03/plant-tissue-analysis-what-to-know.html
12. NCDA&CS, Plant Tissue Analysis Guide: https://www.ncagr.gov/agronomic-services-plant-tissue-analysis-guide/open
13. PIB, STCR and DRIS concepts in balanced fertilizer recommendations: https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=3&NoteId=157129&lang=1&reg=3

Research note: standards, statutory seed testing, fertilizer labels, laboratory accreditation and state/crop-specific recommendation rules must be checked against current official editions and competent authorities before commercial release. This document is an engineering research baseline, not a certification, diagnosis or legal opinion.
