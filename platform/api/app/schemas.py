from datetime import datetime
from typing import Any,Literal
import math
from pydantic import BaseModel,ConfigDict,Field,field_validator
class FarmCreate(BaseModel):
    tenant_id:str
    name:str=Field(min_length=1,max_length=160)
    country_code:str|None=Field(default=None,min_length=2,max_length=2)
    timezone:str="UTC"
class FarmRead(FarmCreate):
    id:str
    created_at:datetime
    model_config=ConfigDict(from_attributes=True)
class Geometry(BaseModel):
    type:Literal["Polygon"]
    coordinates:list[list[list[float]]]
    @field_validator("coordinates")
    @classmethod
    def valid_polygon(cls,rings):
        if not rings or len(rings[0])<4: raise ValueError("Exterior ring needs four positions")
        for ring in rings:
            if ring[0]!=ring[-1]: raise ValueError("Polygon rings must be closed")
            for p in ring:
                if len(p)!=2 or not all(math.isfinite(v) for v in p): raise ValueError("Finite [longitude, latitude] pairs required")
                if not -180<=p[0]<=180 or not -90<=p[1]<=90: raise ValueError("Coordinates must be WGS84")
        return rings
class FieldCreate(BaseModel):
    tenant_id:str
    name:str=Field(min_length=1,max_length=160)
    geometry:Geometry
    crs:Literal["EPSG:4326"]="EPSG:4326"
    geometry_source:str=Field(min_length=1,max_length=200)
    area_hectares:float|None=Field(default=None,gt=0)
class FieldRead(BaseModel):
    id:str; tenant_id:str; farm_id:str; name:str; geometry:dict[str,Any]; crs:str; geometry_source:str
    area_hectares:float|None; created_at:datetime
    model_config=ConfigDict(from_attributes=True)
class ObservationCreate(BaseModel):
    tenant_id:str; farm_id:str; field_id:str|None=None
    source_id:str=Field(min_length=1,max_length=160)
    metric:str=Field(min_length=1,max_length=100)
    value:float
    unit:str=Field(min_length=1,max_length=40)
    observed_at:datetime
    quality:Literal["unverified","valid","suspect","invalid"]="unverified"
    provenance:dict[str,Any]=Field(default_factory=dict)
    @field_validator("value")
    @classmethod
    def finite(cls,v):
        if not math.isfinite(v): raise ValueError("Value must be finite")
        return v
    @field_validator("observed_at")
    @classmethod
    def tz_required(cls,v):
        if v.tzinfo is None: raise ValueError("observed_at must include timezone")
        return v
class ObservationRead(BaseModel):
    id:str; tenant_id:str; farm_id:str; field_id:str|None; source_id:str; metric:str
    value:float; unit:str; observed_at:datetime; quality:str; provenance:dict[str,Any]; created_at:datetime
