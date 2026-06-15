import pandas as pd


def get_driver_stats(driver_id: str):

    df = pd.read_csv("data/rides.csv")

    driver_rides = df[
        df["driver_id"] == driver_id
    ]

    if len(driver_rides) == 0:
        return None

    total_rides = len(driver_rides)

    complaints = int(
        driver_rides["complaint"].sum()
    )

    suspicious_rides = int(
        driver_rides["fraud_label"].sum()
    )

    otp_violations = int(
        (~driver_rides["otp_verified"]).sum()
    )

    complaint_rate = complaints / total_rides

    suspicious_rate = (
        suspicious_rides / total_rides
    )

    otp_violation_rate = (
        otp_violations / total_rides
    )

    trust_score = 100

    trust_score -= complaint_rate * 30
    trust_score -= suspicious_rate * 50
    trust_score -= otp_violation_rate * 20

    trust_score = round(
        max(trust_score, 0),
        2
    )

    if trust_score >= 85:
        driver_rating = "TRUSTED"

    elif trust_score >= 60:
        driver_rating = "MODERATE"

    else:
        driver_rating = "HIGH RISK"

    return {
        "driver_id": driver_id,
        "total_rides": total_rides,
        "complaints": complaints,
        "suspicious_rides": suspicious_rides,
        "otp_violations": otp_violations,
        "complaint_rate": round(
            complaint_rate * 100,
            2
        ),
        "suspicious_rate": round(
            suspicious_rate * 100,
            2
        ),
        "otp_violation_rate": round(
            otp_violation_rate * 100,
            2
        ),
        "trust_score": trust_score,
        "driver_rating": driver_rating,
    }