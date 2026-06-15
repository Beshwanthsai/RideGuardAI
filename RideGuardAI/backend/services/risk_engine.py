def calculate_risk_score(
    estimated_fare: float,
    actual_fare: float,
    estimated_distance: float,
    actual_distance: float,
    otp_verified: bool
):
    risk_score = 0

    fare_increase_percentage = ((actual_fare - estimated_fare)/ estimated_fare) * 100

    distance_deviation_percentage = ((actual_distance - estimated_distance) / estimated_distance) * 100

    if fare_increase_percentage > 50:
        risk_score += 40
    elif fare_increase_percentage > 20:
        risk_score += 20

    if distance_deviation_percentage > 40:
        risk_score += 35
    elif distance_deviation_percentage > 20:
        risk_score += 15

    if not otp_verified:
        risk_score += 25

    return {
        "risk_score": min(risk_score, 100),
        "fare_increase_percentage": round(
            fare_increase_percentage, 2
        ),
        "distance_deviation_percentage": round(
            distance_deviation_percentage, 2
        ),
    }