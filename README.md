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
