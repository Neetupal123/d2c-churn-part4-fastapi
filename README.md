## Project Overview
 D2C Churn Prediction API


This project provides a FastAPI-based machine learning API for predicting customer churn risk in a D2C (Direct-to-Consumer) business.

The API loads a trained churn prediction model and exposes endpoints that allow CRM systems or internal teams to:

* check API health
* predict churn probability for a single customer
* predict churn probability for multiple customers

The system helps retention teams identify customers at risk of churning within the next 60 days.

---

# Project Structure

```text id="tpr55r"
d2c-churn-part4-api/
│
├── app/
│   └── main.py
│
├── tests/
│   └── test_api.py
│
├── model.pkl
├── requirements.txt
├── monitoring_plan.md
├── README.md
```

---

# Model Information

The API uses a trained Random Forest churn prediction model.

The model was trained using customer behavioural and engagement features such as:

* recency_days
* frequency_180d
* monetary_180d
* sessions_30d
* ticket_count_90d
* campaign_clicks_30d
* loyalty_tier
* customer activity signals

The saved model file:

* model.pkl

---

# Installation

Install all required dependencies:

```bash id="j5d6o5"
pip install -r requirements.txt
```

---

# Run the API

Start the FastAPI server:

```bash id="w2s8ie"
uvicorn app.main:app --reload
```

API will run at:

```text id="78imx6"
http://127.0.0.1:8000
```

Swagger documentation:

```text id="x0ebg5"
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## 1. GET /health

Checks whether the API is running correctly.

### Example Response

```json id="xk2c8x"
{
  "status": "ok"
}
```

---

# 2. POST /predict

Predicts churn risk for one customer.

### Sample Request

```json id="u0k8h7"
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
```

### Sample Response

```json id="rgx17g"
{
  "churn_probability": 0.72,
  "predicted_class": 1,
  "risk_level": "high",
  "risk_explanation": "low app activity, customer inactive for long time"
}
```

---

# 3. POST /batch_predict

Predicts churn risk for multiple customers in one request.

### Example Response

```json id="xshwta"
{
  "predictions": [
    {
      "churn_probability": 0.72,
      "predicted_class": 1,
      "risk_level": "high"
    }
  ]
}
```

---

# Run API Tests

Run all API test cases:

```bash id="2t2r07"
pytest
```

---

# Reproducibility

The project includes:

* requirements.txt
* saved model artifact
* API test cases
* monitoring plan

This ensures the API can be reproduced and deployed consistently.

---

# Responsible Use

The API predictions are intended to support customer retention strategies.

Predictions should not be used as the sole basis for business decisions.

Human review is recommended before applying retention offers or interventions.

The model may produce false positives and false negatives.
