# Traceability Matrix
| Requirement | Design | Implementation | Verification |
|---|---|---|---|
| SYS-001..005 | COMMON_DATA_MODEL, DIGITAL_TWIN_SCHEMA | API models | test_digital_farm.py |
| SYS-006..008 | INTERFACE_SPECIFICATIONS, MODULE_REQUIREMENTS | OpenAPI, schemas, module docs | contract review |
| SYS-009,019 | DEVELOPMENT_AND_CI | requirements, Compose, Actions | CI |
| SYS-010 | AGX-01 | farms/fields/observations API | vertical-slice test |
| SYS-011..012 | COMMON_DATA_MODEL | Pydantic validation | API tests |
| SYS-013..015 | ROS2_SIMULATION, mission contract | design only | future safety/fault tests |
| SYS-016..018 | architecture/governance | planned | future verification |
| AGX-01..15 | per-module specs | staged contracts | module tests to add |

Unimplemented requirements remain planned, never complete by assertion.
