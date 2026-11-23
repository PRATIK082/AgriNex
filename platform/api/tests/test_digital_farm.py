from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
TENANT="tenant-v01-test"
def test_health():
    r=client.get("/health"); assert r.status_code==200 and r.json()["status"]=="ok"
def test_farm_field_observation_vertical_slice():
    r=client.post("/api/v1/farms",json={"tenant_id":TENANT,"name":"Demo Farm","country_code":"IN","timezone":"Asia/Kolkata"})
    assert r.status_code==201,r.text
    farm=r.json()
    poly={"type":"Polygon","coordinates":[[[77,12],[77.001,12],[77.001,12.001],[77,12.001],[77,12]]]}
    r=client.post(f"/api/v1/farms/{farm['id']}/fields",json={"tenant_id":TENANT,"name":"Field A","geometry":poly,"geometry_source":"synthetic fixture"})
    assert r.status_code==201,r.text
    field=r.json()
    r=client.post("/api/v1/observations",json={"tenant_id":TENANT,"farm_id":farm["id"],"field_id":field["id"],"source_id":"synthetic-sensor-01","metric":"soil_moisture","value":23.5,"unit":"%","observed_at":"2026-11-20T10:00:00Z","quality":"valid","provenance":{"synthetic":True}})
    assert r.status_code==201,r.text
    assert r.json()["unit"]=="%"
    r=client.get("/api/v1/observations",params={"farm_id":farm["id"],"tenant_id":TENANT})
    assert r.status_code==200 and len(r.json())==1
def test_invalid_polygon_rejected():
    p={"tenant_id":TENANT,"name":"Bad","geometry":{"type":"Polygon","coordinates":[[[200,12],[200,13],[201,13],[200,12]]]},"geometry_source":"test"}
    assert client.post("/api/v1/farms/unknown/fields",json=p).status_code==422
