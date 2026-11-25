# Farm Digital Twin Database Schema
Target: PostgreSQL/PostGIS. Reference SQL: platform/api/migrations/001_initial_postgis.sql. API demo uses SQLite for local ease only.

Tables: tenants → farms → fields → zones; farms → assets; fields → crop_cycles; assets/fields → observations. Future tables: samples, recommendations, missions, commands, acknowledgements, outcomes, audit_events, attachments, consents.

Fields store Polygon geometry with SRID 4326 and GiST index, plus source CRS and geometry provenance. Validate polygon topology and coordinates; area must declare calculation method. Observations include tenant/farm/field/asset, metric, value, unit, observed_at, ingested_at, quality, provenance and schema_version. Consider TimescaleDB only after workload evidence. Production must enforce tenant scoping at service and database policy layers.
