# RoadGuard AI

AI-powered road damage detection and reporting platform using YOLO, FastAPI, and PostgreSQL.

## Overview

RoadGuard AI is a computer vision-based application designed to identify road surface damage from uploaded images. It provides an API and web dashboard for running detections and managing road damage reports.

## Key Features

- AI-based road damage detection using YOLO
- Detection of four damage categories:
  - Longitudinal cracks
  - Transverse cracks
  - Alligator cracks
  - Potholes
- Image upload and annotated detection results
- Confidence scores and bounding boxes
- User registration and JWT-based authentication
- Role-based access control
- Road damage report creation and retrieval
- PostgreSQL database integration
- Interactive FastAPI Swagger documentation

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Backend | FastAPI |
| AI model | Ultralytics YOLO |
| Deep learning | PyTorch |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Authentication | JWT |
| Frontend | HTML, CSS, JavaScript |
| API documentation | Swagger / OpenAPI |

## Project Structure

```text
RoadGuard-AI/
├── ai-model/
├── backend/
│   ├── alembic/
│   ├── app/
│   │   ├── api/v1/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── static/
│   ├── requirements.txt
│   └── alembic.ini
├── runs/
└── README.md
