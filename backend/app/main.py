from fastapi import FastAPI
from app.api.v1.users import router as users_router
from app.api.v1.auth import router as auth_router
from app.api.v1.road_reports import router as road_reports_router

# Initialize FastAPI application
app = FastAPI(
    title="RoadGuard AI",
    description="AI-Powered Road Damage Detection Platform",
    version="1.0.0"
)
app.include_router(users_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
app.include_router(road_reports_router, prefix="/api/v1")

# Root endpoint
@app.get("/")
def home():
    return {
        "project": "RoadGuard AI",
        "message": "Backend is running successfully",
        "status": "success"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "RoadGuard AI Backend"
    }
