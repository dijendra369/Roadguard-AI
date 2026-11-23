from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.api.v1.users import router as users_router
from app.api.v1.auth import router as auth_router
from app.api.v1.road_reports import router as road_reports_router
from app.api.v1.detections import router as detections_router

app = FastAPI(
    title="RoadGuard AI",
    description="AI-Powered Road Damage Detection Platform",
    version="1.0.0"
)

app.include_router(users_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
app.include_router(road_reports_router, prefix="/api/v1")
app.include_router(detections_router, prefix="/api/v1")


@app.get("/", include_in_schema=False)
def home():
    frontend = Path(__file__).parent / "static" / "index.html"
    return FileResponse(frontend)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "RoadGuard AI Backend"
    }
