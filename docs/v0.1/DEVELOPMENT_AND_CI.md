# Development Environment and CI
Prerequisites: Git, Python 3.11+, Docker Compose; optional ROS 2 Jazzy/Gazebo Harmonic on supported Ubuntu.

API: cd platform/api; python -m venv .venv; activate; pip install -r requirements-dev.txt; uvicorn app.main:app --reload; pytest -q. Browse /docs. Compose: docker compose up -d db starts PostgreSQL/PostGIS.

CI installs pinned API requirements, runs Python compile and pytest. Add lint/type/security/container scanning and ROS build matrix after runner/container validation. Use feature branches and PRs; require requirement IDs, schema/API impact, tests, safety/privacy/security review and migration plan. Never commit secrets.

SQLite is demonstrator mode. Before production: Alembic migrations, PostGIS persistence, authN/authZ, tenant isolation, audit, rate limiting, observability, backups/restore, threat model and deployment hardening.
