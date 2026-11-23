import json
from fastapi import Depends,FastAPI,HTTPException,Query
from sqlalchemy.orm import Session
from .database import Base,engine,get_db
from . import models,schemas
Base.metadata.create_all(bind=engine)
app=FastAPI(title="AgriNex Digital Farm API",version="0.1.0",description="Development demonstrator; not production farm-control software.")
@app.get("/health")
def health(): return {"status":"ok","service":"agrinex-api","version":"0.1.0"}
@app.post("/api/v1/farms",response_model=schemas.FarmRead,status_code=201)
def create_farm(payload:schemas.FarmCreate,db:Session=Depends(get_db)):
    x=models.Farm(**payload.model_dump()); db.add(x); db.commit(); db.refresh(x); return x
@app.get("/api/v1/farms",response_model=list[schemas.FarmRead])
def list_farms(tenant_id:str=Query(min_length=1),db:Session=Depends(get_db)):
    return db.query(models.Farm).filter(models.Farm.tenant_id==tenant_id).all()
@app.post("/api/v1/farms/{farm_id}/fields",response_model=schemas.FieldRead,status_code=201)
def create_field(farm_id:str,payload:schemas.FieldCreate,db:Session=Depends(get_db)):
    farm=db.query(models.Farm).filter(models.Farm.id==farm_id,models.Farm.tenant_id==payload.tenant_id).first()
    if farm is None: raise HTTPException(status_code=404,detail="Farm not found for tenant")
    d=payload.model_dump(exclude={"geometry"}); d["geometry"]=payload.geometry.model_dump()
    x=models.Field(farm_id=farm_id,**d); db.add(x); db.commit(); db.refresh(x); return x
@app.get("/api/v1/farms/{farm_id}/fields",response_model=list[schemas.FieldRead])
def list_fields(farm_id:str,tenant_id:str=Query(min_length=1),db:Session=Depends(get_db)):
    return db.query(models.Field).filter(models.Field.farm_id==farm_id,models.Field.tenant_id==tenant_id).all()
@app.post("/api/v1/observations",response_model=schemas.ObservationRead,status_code=201)
def create_observation(payload:schemas.ObservationCreate,db:Session=Depends(get_db)):
    farm=db.query(models.Farm).filter(models.Farm.id==payload.farm_id,models.Farm.tenant_id==payload.tenant_id).first()
    if farm is None: raise HTTPException(status_code=404,detail="Farm not found for tenant")
    if payload.field_id and db.query(models.Field).filter(models.Field.id==payload.field_id,models.Field.farm_id==payload.farm_id,models.Field.tenant_id==payload.tenant_id).first() is None: raise HTTPException(status_code=404,detail="Field not found")
    d=payload.model_dump(); d["provenance"]=json.dumps(d["provenance"],sort_keys=True)
    x=models.Observation(**d); db.add(x); db.commit(); db.refresh(x)
    out={c.name:getattr(x,c.name) for c in x.__table__.columns}; out["provenance"]=json.loads(x.provenance); return out
@app.get("/api/v1/observations",response_model=list[schemas.ObservationRead])
def list_observations(farm_id:str,tenant_id:str,limit:int=Query(default=100,ge=1,le=500),db:Session=Depends(get_db)):
    rows=db.query(models.Observation).filter(models.Observation.farm_id==farm_id,models.Observation.tenant_id==tenant_id).order_by(models.Observation.observed_at.desc()).limit(limit).all()
    out=[]
    for x in rows:
        d={c.name:getattr(x,c.name) for c in x.__table__.columns}; d["provenance"]=json.loads(x.provenance); out.append(d)
    return out
