import uuid
from datetime import datetime,timezone
from sqlalchemy import DateTime,Float,ForeignKey,JSON,String,Text
from sqlalchemy.orm import Mapped,mapped_column,relationship
from .database import Base
def new_id(): return str(uuid.uuid4())
def now_utc(): return datetime.now(timezone.utc)
class Farm(Base):
    __tablename__="farms"
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=new_id)
    tenant_id:Mapped[str]=mapped_column(String(36),index=True)
    name:Mapped[str]=mapped_column(String(160))
    country_code:Mapped[str|None]=mapped_column(String(2),nullable=True)
    timezone:Mapped[str]=mapped_column(String(64),default="UTC")
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc)
    fields:Mapped[list["Field"]]=relationship(back_populates="farm",cascade="all, delete-orphan")
class Field(Base):
    __tablename__="fields"
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=new_id)
    tenant_id:Mapped[str]=mapped_column(String(36),index=True)
    farm_id:Mapped[str]=mapped_column(ForeignKey("farms.id"),index=True)
    name:Mapped[str]=mapped_column(String(160))
    geometry:Mapped[dict]=mapped_column(JSON)
    crs:Mapped[str]=mapped_column(String(32),default="EPSG:4326")
    area_hectares:Mapped[float|None]=mapped_column(Float,nullable=True)
    geometry_source:Mapped[str]=mapped_column(String(200))
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc)
    farm:Mapped[Farm]=relationship(back_populates="fields")
class Observation(Base):
    __tablename__="observations"
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=new_id)
    tenant_id:Mapped[str]=mapped_column(String(36),index=True)
    farm_id:Mapped[str]=mapped_column(ForeignKey("farms.id"),index=True)
    field_id:Mapped[str|None]=mapped_column(ForeignKey("fields.id"),nullable=True,index=True)
    source_id:Mapped[str]=mapped_column(String(160))
    metric:Mapped[str]=mapped_column(String(100),index=True)
    value:Mapped[float]=mapped_column(Float)
    unit:Mapped[str]=mapped_column(String(40))
    observed_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),index=True)
    quality:Mapped[str]=mapped_column(String(32),default="unverified")
    provenance:Mapped[str]=mapped_column(Text,default="{}")
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc)
