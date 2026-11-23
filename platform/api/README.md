# Digital Farm API — V0.1 Vertical Slice
Run: cd platform/api; python -m venv .venv; activate; pip install -r requirements-dev.txt; uvicorn app.main:app --reload. Browse http://127.0.0.1:8000/docs.

Endpoints: GET /health; POST/GET /api/v1/farms; POST/GET /api/v1/farms/{farm_id}/fields; POST/GET /api/v1/observations. SQLite local DB defaults to agrinex.db. Set AGRINEX_DATABASE_URL to override.

Field geometry is GeoJSON Polygon EPSG:4326. Observations require unit, timezone-aware observed_at, source and quality. Run pytest -q.

Demo limitations: no authentication/authorization, production tenant isolation, PostGIS ORM persistence, migrations, audit, rate limiting, full UCUM validation or sensor signature verification. Do not expose publicly or use to control machines.
