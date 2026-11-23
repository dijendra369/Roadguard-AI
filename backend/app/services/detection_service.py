from functools import lru_cache
from pathlib import Path
from io import BytesIO
import base64

from PIL import Image
from ultralytics import YOLO

MODEL_PATH = (
    Path(__file__).resolve().parents[3]
    / "runs" / "detect" / "train" / "weights" / "best.pt"
)


@lru_cache(maxsize=1)
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"YOLO model not found: {MODEL_PATH}")
    return YOLO(str(MODEL_PATH))


def detect_road_damage(image: Image.Image):
    model = load_model()

    results = model.predict(
        source=image,
        conf=0.05,
        device="cpu",
        verbose=False
    )

    result = results[0]
    detections = []

    if result.boxes is not None and len(result.boxes) > 0:
        raw_boxes = result.boxes.data.cpu().tolist()

        for row in raw_boxes:
            x1, y1, x2, y2, confidence, class_id = row[:6]
            class_id = int(class_id)

            detections.append({
                "damage_type": model.names[class_id],
                "confidence": round(confidence, 4),
                "confidence_percent": round(confidence * 100, 2),
                "bounding_box": {
                    "x1": round(x1, 2),
                    "y1": round(y1, 2),
                    "x2": round(x2, 2),
                    "y2": round(y2, 2)
                }
            })

    annotated = result.plot()
    annotated_image = Image.fromarray(annotated[:, :, ::-1])

    buffer = BytesIO()
    annotated_image.save(buffer, format="JPEG", quality=85)

    encoded_image = base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")

    return {
        "total_detections": len(detections),
        "detections": detections,
        "annotated_image": encoded_image
    }
