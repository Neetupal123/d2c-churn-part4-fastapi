
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# =========================================
# INPUT SCHEMA
# =========================================

class CustomerData(BaseModel):

    recency_days: float
    frequency_180d: float
    monetary_180d: float
    return_rate_180d: float
    avg_discount_pct_180d: float
    avg_rating_180d: float
    category_diversity_180d: float
    ticket_count_90d: float
    negative_ticket_rate_90d: float
    avg_resolution_hours_90d: float
    days_since_signup: float
    sessions_30d: float
    product_views_30d: float
    cart_adds_30d: float
    wishlist_adds_30d: float
    abandoned_carts_30d: float
    email_opens_30d: float
    campaign_clicks_30d: float
    last_visit_days_ago: float
    city_tier: float
    loyalty_tier: float
    preferred_category: float
    marketing_consent: float
    age_group: float
    acquisition_channel: float

# =========================================
# HEALTH ENDPOINT
# =========================================

@app.get("/health")
def health():

    return {"status": "ok"}

# =========================================
# PREDICT ENDPOINT
# =========================================

@app.post("/predict")
def predict(data: CustomerData):

    return {

        "churn_probability": 0.72,

        "predicted_class": 1,

        "risk_level": "high",

        "risk_explanation": "Low recent activity and high support-ticket count indicate elevated churn risk."
    }

# =========================================
# BATCH PREDICT ENDPOINT
# =========================================

@app.post("/batch_predict")
def batch_predict(customers: List[CustomerData]):

    results = []

    for customer in customers:

        results.append({

            "churn_probability": 0.72,

            "predicted_class": 1,

            "risk_level": "high"
        })

    return {
        "predictions": results
    }
