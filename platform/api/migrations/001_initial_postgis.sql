-- PostgreSQL/PostGIS target schema; production must use reviewed migrations.
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE TABLE tenants(id uuid PRIMARY KEY,name text NOT NULL,created_at timestamptz NOT NULL DEFAULT now());
CREATE TABLE farms(id uuid PRIMARY KEY,tenant_id uuid NOT NULL REFERENCES tenants(id),name text NOT NULL,country_code char(2),timezone text NOT NULL,created_at timestamptz NOT NULL DEFAULT now());
CREATE INDEX farms_tenant_idx ON farms(tenant_id);
CREATE TABLE fields(id uuid PRIMARY KEY,tenant_id uuid NOT NULL REFERENCES tenants(id),farm_id uuid NOT NULL REFERENCES farms(id),name text NOT NULL,boundary geometry(Polygon,4326) NOT NULL,source_crs text NOT NULL,geometry_source text NOT NULL,area_hectares numeric,created_at timestamptz NOT NULL DEFAULT now());
CREATE INDEX fields_tenant_idx ON fields(tenant_id);
CREATE INDEX fields_boundary_gix ON fields USING GIST(boundary);
CREATE TABLE zones(id uuid PRIMARY KEY,tenant_id uuid NOT NULL REFERENCES tenants(id),field_id uuid NOT NULL REFERENCES fields(id),name text NOT NULL,boundary geometry(Polygon,4326) NOT NULL);
CREATE INDEX zones_boundary_gix ON zones USING GIST(boundary);
CREATE TABLE assets(id uuid PRIMARY KEY,tenant_id uuid NOT NULL REFERENCES tenants(id),farm_id uuid NOT NULL REFERENCES farms(id),asset_type text NOT NULL,name text NOT NULL,capability_profile jsonb NOT NULL DEFAULT '{}',status text NOT NULL);
CREATE TABLE crop_cycles(id uuid PRIMARY KEY,tenant_id uuid NOT NULL REFERENCES tenants(id),field_id uuid NOT NULL REFERENCES fields(id),crop_code text NOT NULL,variety text,season text,planted_at timestamptz,expected_harvest_at timestamptz,status text NOT NULL);
CREATE TABLE observations(id uuid PRIMARY KEY,tenant_id uuid NOT NULL REFERENCES tenants(id),farm_id uuid NOT NULL REFERENCES farms(id),field_id uuid REFERENCES fields(id),asset_id uuid REFERENCES assets(id),metric text NOT NULL,value double precision NOT NULL,unit text NOT NULL,observed_at timestamptz NOT NULL,ingested_at timestamptz NOT NULL DEFAULT now(),quality text NOT NULL,provenance jsonb NOT NULL DEFAULT '{}',raw_reference text,schema_version text NOT NULL DEFAULT '1.0');
CREATE INDEX observations_farm_time_idx ON observations(tenant_id,farm_id,observed_at DESC);
