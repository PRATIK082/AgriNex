# ADR-0001 Modular Monolith
Accepted for V0.1. Fifteen domains exist but scale/deployment boundaries are unproven. Use one modular API with explicit domain packages, stable contracts and domain-owned persistence; keep ROS 2/edge runtime separate. Extract services only when measured scaling, ownership, availability or isolation requires it.
