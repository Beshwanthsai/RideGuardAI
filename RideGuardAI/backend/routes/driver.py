from fastapi import APIRouter

from backend.services.driver_service import (
    get_driver_stats
)

router = APIRouter()


@router.get("/driver/{driver_id}")
def driver_details(driver_id: str):

    result = get_driver_stats(driver_id)

    if result is None:
        return {
            "message": "Driver not found"
        }

    return result