# Repository Structure and Module Ownership
AgriNex is designed as one coherent repository with domain-owned packages. Directories may begin as documentation/specification; do not create empty production services without requirements and a vertical slice.

```text
AgriNex/
├── README.md LICENSE NOTICE CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md GOVERNANCE.md ROADMAP.md
├── docs/
│   ├── vision/ research/ architecture/ requirements/ modules/
│   ├── agronomy/ robotics/ drones/ hardware/ simulation/
│   ├── standards/ safety/ validation/ operations/ market/
│   ├── assets/ diagrams/ decisions/
├── platform/
│   ├── web/ mobile/ api/ domain/ ingestion/ edge-gateway/ device-management/
├── agronomy/
│   ├── soil/ crop-models/ irrigation/ nutrition/ diseases/ pests/ weeds/ yield/
├── intelligence/
│   ├── agents/ computer-vision/ forecasting/ optimization/ model-registry/
├── robotics/
│   ├── ros2/ navigation/ perception/ mission-control/ fleet/ safety-interface/ hardware-abstraction/
├── drones/
│   ├── mapping/ scouting/ application-adapters/ mission-planning/ integrations/
├── hardware/
│   ├── controllers/ sensors/ actuators/ power/ irrigation/ robot-platforms/ reference-designs/
├── simulation/
│   ├── virtual-farm/ crop-simulation/ robot-simulation/ weather-scenarios/ hardware-in-loop/
├── integrations/
│   ├── farmos/ isobus/ weather/ satellite/ market-data/ equipment-oem/
├── datasets/
│   ├── schemas/ samples/ metadata/ dataset-cards/
├── tests/
│   ├── unit/ component/ integration/ system/ simulation/ safety/ hil/ field-validation/
├── tools/
│   ├── cli/ dataset-tools/ calibration/ developer-tools/
├── skills/
│   ├── agronomy/ ai-ml/ geospatial/ robotics/ embedded/ hardware/ safety/ testing/
└── .github/
    ├── workflows/ ISSUE_TEMPLATE/ PULL_REQUEST_TEMPLATE.md CODEOWNERS
```

## Required engineering lifecycle
Stakeholder needs → system requirements → architecture → detailed design → implementation → static analysis/review → unit → integration → system → simulation → HIL → controlled field validation → release/maintenance.

Every requirement links to design, implementation and test evidence. Each module declares owner, APIs/events, dependencies, licenses, data contracts, safety/security impacts and acceptance criteria.
