from fastapi import APIRouter
from dal import get_top_customers, get_customers_without_orders, get_zero_credit_active_customers

router = APIRouter()

@router.get("/analytics/alerts-by-border-and-priority")
def alerts_by_border_and_priority():
    return get_alerts_by_border_and_priority()

@router.get("/analytics/top-urgent-zones")
def top_urgent_zones():
    return get_top_urgent_zones()

@router.get("/analytics/distance-distribution")
def distance_distribution():
    return get_distance_distribution()

@router.get("/analytics/low-visibility-high-activity")
def low_visibility_high_activity():
    return get_low_visibility_high_activity()

@router.get("/analytics/hot-zones")
def hot_zones():
    return get_hot_zones()
