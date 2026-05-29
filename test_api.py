from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {"status": "ok"}

def test_predict():

    sample_data = {

        "recency_days": 40,
        "frequency_180d": 8,
        "monetary_180d": 5000,
        "return_rate_180d": 0.1,
        "avg_discount_pct_180d": 15,
        "avg_rating_180d": 4,
        "category_diversity_180d": 3,
        "ticket_count_90d": 2,
        "negative_ticket_rate_90d": 0.2,
        "avg_resolution_hours_90d": 20,
        "days_since_signup": 400,
        "sessions_30d": 12,
        "product_views_30d": 30,
        "cart_adds_30d": 5,
        "wishlist_adds_30d": 2,
        "abandoned_carts_30d": 1,
        "email_opens_30d": 6,
        "campaign_clicks_30d": 2,
        "last_visit_days_ago": 5,
        "city_tier": 2,
        "loyalty_tier": 1,
        "preferred_category": 3,
        "marketing_consent": 1,
        "age_group": 2,
        "acquisition_channel": 1
    }

    response = client.post("/predict", json=sample_data)

    assert response.status_code == 200

def test_batch_predict():

    sample_batch = [

        {
            "recency_days": 40,
            "frequency_180d": 8,
            "monetary_180d": 5000,
            "return_rate_180d": 0.1,
            "avg_discount_pct_180d": 15,
            "avg_rating_180d": 4,
            "category_diversity_180d": 3,
            "ticket_count_90d": 2,
            "negative_ticket_rate_90d": 0.2,
            "avg_resolution_hours_90d": 20,
            "days_since_signup": 400,
            "sessions_30d": 12,
            "product_views_30d": 30,
            "cart_adds_30d": 5,
            "wishlist_adds_30d": 2,
            "abandoned_carts_30d": 1,
            "email_opens_30d": 6,
            "campaign_clicks_30d": 2,
            "last_visit_days_ago": 5,
            "city_tier": 2,
            "loyalty_tier": 1,
            "preferred_category": 3,
            "marketing_consent": 1,
            "age_group": 2,
            "acquisition_channel": 1
        }
    ]

    response = client.post("/batch_predict", json=sample_batch)

    assert response.status_code == 200
