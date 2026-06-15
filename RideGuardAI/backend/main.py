from fastapi import FastAPI

from backend.routes.ride import router as ride_router

app = FastAPI(
    title="RideGuard AI",
    version="1.0.0"
)

app.include_router(ride_router)


@app.get("/")
def home():
    return {
        "message": "RideGuard AI Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }