from datetime import datetime
from pydantic import BaseModel, ConfigDict


class RoadReportCreate(BaseModel):
    latitude: float
    longitude: float
    damage_type: str
    severity: str
    image_path: str


class RoadReportResponse(BaseModel):
    id: int
    user_id: int
    latitude: float
    longitude: float
    damage_type: str
    severity: str
    image_path: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
