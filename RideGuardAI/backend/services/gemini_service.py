import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_ai_report(
    fare_increase_percentage,
    distance_deviation_percentage,
    otp_verified,
    risk_score,
    risk_level,
):

    prompt = f"""
You are an intelligent ride safety analyst.

Analyze the ride information below and generate
a professional investigation report.

Ride Information:

Fare Increase Percentage:
{fare_increase_percentage}

Distance Deviation Percentage:
{distance_deviation_percentage}

OTP Verified:
{otp_verified}

Risk Score:
{risk_score}

Risk Level:
{risk_level}

Generate:
1. Summary
2. Risk Factors
3. Recommendation

Keep the report under 150 words.
"""

    response = model.generate_content(
        prompt
    )

    return response.text