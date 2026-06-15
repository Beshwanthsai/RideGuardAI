from pydantic import BaseModel
from typing import Optional


class RideRequest(BaseModel):
    ride_id: Optional[str] = None
    driver_id: Optional[str] = None
    estimated_fare: float
    actual_fare: float
    estimated_distance: float
    actual_distance: float
    otp_verified: bool