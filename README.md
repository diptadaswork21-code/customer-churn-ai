# Customer Churn Prediction AI

## Project Overview

An end-to-end machine learning project that predicts customer churn using XGBoost and explains predictions using SHAP.

The project includes:

- Data analysis
- Model training
- XGBoost prediction
- SHAP explainability
- Streamlit dashboard
- Customer retention recommendations


## Business Problem

Customer churn affects subscription businesses.

This project helps companies:

- Identify customers likely to leave
- Understand why customers churn
- Take action to improve retention

## Model Explainability with SHAP

The final XGBoost model was interpreted using SHAP (SHapley Additive exPlanations) to understand both global and customer-level churn factors.

### Key Churn Drivers Identified

SHAP analysis highlighted the following factors influencing churn predictions:

1. Month-to-month contracts
2. Customer tenure
3. Monthly charges
4. Lack of online security
5. Lack of technical support
6. Fiber optic internet service
7. Electronic check payment method

These insights help identify high-risk customers and support targeted retention strategies.

### Customer-Level Explanations

SHAP local explanations provide individual prediction insights by showing which features increase or reduce a customer's churn probability.

Example insights:

- Month-to-month contracts increase churn risk
- Short customer tenure is associated with higher churn probability
- Higher monthly charges can influence churn risk
- Lack of support services can increase retention risk


## Model Performance

| Model | ROC-AUC |
|---|---|
| Logistic Regression | 0.836 |
| Random Forest | 0.814 |
| XGBoost | 0.836 |


## Streamlit Dashboard

The application provides:

- Churn probability prediction
- Low / Medium / High risk classification
- SHAP explanations
- Feature impact visualization
- Retention recommendations


![Customer Churn Dashboard](image.png)


## Installation

Clone the repository: git clone https://github.com/diptadaswork21-code/customer-churn-ai


Install requirements: pip install -r requirements.txt


Run the application: streamlit run app/app.py


## Project Structure

customer-churn-ai/

app/
app.py

models/
xgb_churn_model.pkl
preprocessor.pkl

notebooks/
01_eda.ipynb

README.md
requirements.txt