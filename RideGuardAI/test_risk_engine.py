from backend.services.risk_engine import calculate_risk_score


result = calculate_risk_score(
    estimated_fare=222,
    actual_fare=408,
    estimated_distance=5.2,
    actual_distance=8.7,
    otp_verified=False
)

print(result)