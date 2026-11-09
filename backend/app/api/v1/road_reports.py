from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.road_report import RoadReport
from app.schemas.road_report import RoadReportCreate, RoadReportResponse
from app.api.v1.dependencies import get_current_user

router = APIRouter(prefix="/road-reports", tags=["Road Reports"])


@router.post("/", response_model=RoadReportResponse, status_code=201)
def create_road_report(
    report_data: RoadReportCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_report = RoadReport(
        user_id=current_user.id,
        latitude=report_data.latitude,
        longitude=report_data.longitude,
        damage_type=report_data.damage_type,
        severity=report_data.severity,
        image_path=report_data.image_path
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return new_report


@router.get("/", response_model=list[RoadReportResponse])
def get_my_road_reports(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return (
        db.query(RoadReport)
        .filter(RoadReport.user_id == current_user.id)
        .all()
    )