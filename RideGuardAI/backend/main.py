from fastapi import FastAPI

from backend.routes.ride import router as ride_router
from backend.routes.driver import router as driver_router

app = FastAPI(
    title="RideGuard AI",
    version="1.0.0",
    description="AI-Powered Ride Safety & Fraud Detection Platform"
)

# Ride Analysis Routes
app.include_router(ride_router)

# Driver Analytics Routes
app.include_router(driver_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to RideGuard AI 🚖",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }