# AI Agent Architecture
Agents: Farm Planner, Crop Selector, Soil Analyst, Weather Analyst, Irrigation Planner, Nutrition Analyst, Disease/Pest/Weed Scout, Drone Mission Planner, Robot Fleet Planner, Crop Growth Analyst, Harvest Planner, Market Analyst, Profit Scenario Analyst, Safety/Compliance Checker, Farm Supervisor.

Every agent declares purpose, allowed/forbidden tools, input/output schema, evidence, abstention behavior, timeout, audit fields and version. Use least-privilege capabilities.

Flow: retrieve verified observations → validate freshness/provenance → invoke scientific model/rules → structured candidate → contraindication/regulatory checks → human approval where required → authorized task intent → edge validation → local execution → outcome verification.

Agents cannot command motor PWM, defeat E-stops, change safety limits, unlock geofences, issue unreviewed chemical doses, fabricate observations or commit finances. Do not allow self-approval of high-risk outputs.

Maintain model cards, dataset cards, training versions, evaluation, calibration, domain-shift monitoring, rollback and approval. Show explanation, evidence, uncertainty, affected area, cost, alternatives and stop/recovery controls.
