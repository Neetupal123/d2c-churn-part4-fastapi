# Monitoring Plan

## Overview

This monitoring plan describes how the churn prediction API will be monitored after deployment to ensure model reliability, API stability, and responsible business usage.

---

# 1. Data Drift Monitoring

The incoming customer data should be continuously compared with the training data distribution.

Important features to monitor:

* recency_days
* frequency_180d
* monetary_180d
* sessions_30d
* ticket_count_90d
* campaign_clicks_30d

Potential risks:

* sudden changes in customer behaviour
* seasonal buying patterns
* changes in marketing campaigns
* new product launches

Action:

* retrain the model if major drift is detected.

---

# 2. Prediction Distribution Monitoring

The prediction outputs should be monitored regularly.

Track:

* percentage of high-risk customers
* percentage of low-risk customers
* average churn probability
* weekly prediction trends

Potential risks:

* prediction spikes
* unstable model behaviour
* biased predictions

Action:

* investigate abnormal prediction changes.

---

# 3. Business Outcome Monitoring

The retention team should compare model predictions with actual business outcomes.

Track:

* actual customer churn rate
* retention campaign success rate
* recovered customers
* revenue saved from retention efforts
* false positive rate
* false negative rate

Business risks:

* unnecessary discount spending
* missing real churn-risk customers

Action:
* adjust decision threshold if business impact becomes poor.

---

# 4. API Performance Monitoring

The deployed API service should be monitored for reliability.

Track:

* API uptime
* failed requests
* response latency
* timeout errors
* invalid payload errors
* server resource usage

Action:

* investigate repeated failures or slow responses.

---

# 5. Model Performance Monitoring

Model performance should be evaluated periodically using fresh labeled data.

Track:

* accuracy
* precision
* recall
* F1-score
* ROC-AUC

Potential risks:

* model degradation
* outdated customer behaviour patterns

Action:

* retrain and redeploy the model when performance drops significantly.

---

# 6. Retraining Triggers

The model should be retrained when:

* major data drift is detected
* business metrics decline
* customer behaviour changes
* new acquisition channels are introduced
* retention campaigns change significantly
* model recall drops below acceptable threshold

Recommended retraining frequency:

* every 3 to 6 months

---

# Responsible Use Note

This API is designed to support customer retention teams by identifying customers with elevated churn risk.

The API predictions should not be treated as final business decisions.

Human review is recommended before:

* offering large discounts
* changing loyalty status
* targeting sensitive customer groups

The model may generate:

* false positives
* false negatives

Retention actions should therefore combine:

* model predictions
* business rules
* customer relationship context

The API should not be used for:

* discriminatory targeting
* unfair pricing decisions
* automated punitive actions
