from io import BytesIO

from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image, UnidentifiedImageError

from app.services.detection_service import detect_road_damage


router = APIRouter(prefix="/detections", tags=["AI Detection"])


@router.post("/predict")
async def predict_road_damage(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a valid image."
        )

    contents = await file.read()

    if not contents:
        raise HTTPException(status_code=400, detail="Uploaded image is empty.")

    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail="Image size must be 10 MB or less."
        )

    try:
        image = Image.open(BytesIO(contents)).convert("RGB")
    except (UnidentifiedImageError, OSError):
        raise HTTPException(
            status_code=400,
            detail="Unable to read the uploaded image."
        )

    try:
        result = detect_road_damage(image)
        return {
            "status": "success",
            "message": "Road damage detection completed.",
            **result
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Detection failed: {str(exc)}"
        )
