def generate_report(
    fare_increase_percentage,
    distance_deviation_percentage,
    otp_verified,
    risk_level,
):
    report = f"""
Ride Investigation Report

Fare Increase: {fare_increase_percentage}%

Distance Deviation: {distance_deviation_percentage}%

OTP Verification:
{"Completed" if otp_verified else "Not Completed"}

Risk Level: {risk_level}

Summary:
The ride exceeded the estimated fare by
{fare_increase_percentage}% and deviated
from the expected distance by
{distance_deviation_percentage}%.
"""

    if not otp_verified:
        report += (
            " OTP verification was not completed "
            "before ride initiation."
        )

    if risk_level == "HIGH":
        report += (
            " This ride has been classified as "
            "HIGH RISK and should be reviewed."
        )
    elif risk_level == "MEDIUM":
        report += (
            " This ride shows moderate risk indicators."
        )
    else:
        report += (
            " No significant risk indicators detected."
        )

    return report