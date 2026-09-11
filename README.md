# Customer Churn Prediction AI

![Python](https://img.shields.io/badge/Python-3.10+-blue)

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-orange)

![Explainability](https://img.shields.io/badge/Explainability-Feature%20Importance-green)

![Deployment](https://img.shields.io/badge/App-Streamlit-red)


## Project Overview

An end-to-end machine learning application that predicts customer churn risk using XGBoost and provides actionable retention insights through a Streamlit dashboard.


The project includes:

- Exploratory Data Analysis
- Data preprocessing
- Model training and evaluation
- XGBoost prediction
- Feature importance explainability
- Streamlit deployment
- Customer retention recommendations


---

---

# Live Demo

🚀 Streamlit Application:

https://customer-churn-ai-mqwtfcvugrnpmus53nz7ta.streamlit.app/

# Business Problem

Customer churn is a major challenge for subscription-based businesses.

This project helps organizations:

- Identify customers likely to leave
- Understand important churn factors
- Prioritize retention strategies


---

# Machine Learning Workflow

## Data Analysis

Performed:

- Data exploration
- Feature analysis
- Churn pattern investigation


## Data Processing

Implemented:

- Numerical feature scaling
- Categorical encoding
- Preprocessing pipeline


## Model Training

Models evaluated:

| Model | ROC-AUC |
|---|---|
| Logistic Regression | 0.836 |
| Random Forest | 0.814 |
| XGBoost | 0.836 |


Final Production Model:

**XGBoost Classifier**


---

# Model Explainability

Feature importance analysis was used to understand the main factors influencing churn predictions.

## Key Churn Drivers

Important churn factors identified:

1. Month-to-month contracts
2. Customer tenure
3. Monthly charges
4. Lack of online security
5. Lack of technical support
6. Fiber optic internet service
7. Electronic check payment method


These insights help businesses design targeted retention strategies.


---

# Streamlit Dashboard

The application provides:

- Churn probability prediction
- Low / Medium / High risk classification
- Feature impact visualization
- Retention recommendations
- PDF customer churn report


![Customer Churn Dashboard](image.png)


---

# Technology Stack

- Python
- Pandas
- Scikit-learn
- XGBoost
- Streamlit
- Plotly
- ReportLab


---

# Installation

Clone repository:

```bash
git clone https://github.com/diptadaswork21-code/customer-churn-ai.git

cd customer-churn-ai

pip install -r requirements.txt

streamlit run app/app.py


---

# Future Improvements

- Add automated model retraining pipeline
- Add model monitoring
- Integrate real-time customer databases
- Deploy with Docker and cloud infrastructure