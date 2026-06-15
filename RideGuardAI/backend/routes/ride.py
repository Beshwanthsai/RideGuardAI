from fastapi import APIRouter

from backend.schemas.ride import RideRequest
from backend.services.risk_engine import calculate_risk_score
from backend.services.report_generator import generate_report

router = APIRouter()


@router.post("/analyze-ride")
def analyze_ride(ride: RideRequest):

    result = calculate_risk_score(
        estimated_fare=ride.estimated_fare,
        actual_fare=ride.actual_fare,
        estimated_distance=ride.estimated_distance,
        actual_distance=ride.actual_distance,
        otp_verified=ride.otp_verified,
    )

    score = result["risk_score"]

    if score >= 70:
        risk_level = "HIGH"
    elif score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    result["risk_level"] = risk_level

    report = generate_report(
        fare_increase_percentage=result["fare_increase_percentage"],
        distance_deviation_percentage=result["distance_deviation_percentage"],
        otp_verified=ride.otp_verified,
        risk_level=risk_level,
    )

    result["investigation_report"] = report

    return result