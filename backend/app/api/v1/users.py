from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_current_user
from app.api.v1.dependencies import get_current_admin

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=UserResponse, status_code=201)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db, user_data)
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))
@router.get("/me", response_model=UserResponse)
def get_my_profile(
    current_user = Depends(get_current_user)
):
    return current_user
@router.get("/admin/dashboard")
def admin_dashboard(
    current_admin = Depends(get_current_admin)
):
    return {
        "message": "Welcome to RoadGuard AI Admin Dashboard",
        "admin": current_admin.full_name,
        "role": current_admin.role
    }
