import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import io

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="Customer Churn AI",
    page_icon="📉",
    layout="wide"
)


# ==========================
# Load ML Artifacts
# ==========================

model = joblib.load(
    "models/xgb_churn_model.pkl"
)

preprocessor = joblib.load(
    "models/preprocessor.pkl"
)

feature_names = joblib.load(
    "models/feature_names.pkl"
)

import shap

explainer = shap.TreeExplainer(model)

# ==========================
# Feature Name Cleaner
# ==========================

def clean_feature_name(feature):

    mapping = {

        "cat__Contract_Month-to-month":
            "Month-to-Month Contract",

        "cat__OnlineSecurity_No":
            "No Online Security",

        "cat__InternetService_Fiber optic":
            "Fiber Optic Internet Service",

        "num__MonthlyCharges":
            "Monthly Charges",

        "cat__TechSupport_No":
            "No Technical Support",

        "cat__OnlineBackup_No":
            "No Online Backup",

        "cat__MultipleLines_No":
            "No Multiple Lines",

        "num__TotalCharges":
            "Total Charges",

        "num__tenure":
            "Customer Tenure"
    }


    if feature in mapping:

        return mapping[feature]


    feature = feature.replace(
        "cat__",
        ""
    )

    feature = feature.replace(
        "num__",
        ""
    )

    feature = feature.replace(
        "_",
        " "
    )

    return feature.title()



# ==========================
# PDF Generator
# ==========================

def create_pdf_report(
        probability,
        risk,
        drivers,
        recommendations
):

    buffer = io.BytesIO()


    pdf = canvas.Canvas(
        buffer,
        pagesize=letter
    )


    pdf.setFont(
        "Helvetica-Bold",
        18
    )

    pdf.drawString(
        50,
        750,
        "Customer Churn Analysis Report"
    )


    pdf.setFont(
        "Helvetica",
        12
    )


    pdf.drawString(
        50,
        710,
        f"Prediction: {risk}"
    )


    pdf.drawString(
        50,
        690,
        f"Churn Probability: {probability:.2%}"
    )


    y = 640


    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        y,
        "Top Churn Drivers"
    )


    y -= 30


    pdf.setFont(
        "Helvetica",
        12
    )


    for driver in drivers:

        pdf.drawString(
            70,
            y,
            "- " + driver
        )

        y -= 20



    y -= 20


    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        y,
        "Recommended Actions"
    )


    y -= 30


    pdf.setFont(
        "Helvetica",
        12
    )


    for action in recommendations:

        pdf.drawString(
            70,
            y,
            "- " + action
        )

        y -= 20


    pdf.save()


    buffer.seek(0)


    return buffer



# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.title(
        "📉 Customer Churn AI"
    )

    st.write(
        """
        XGBoost based churn prediction system.

        Includes:
        - SHAP Explainability
        - Risk Scoring
        - Business Recommendations
        """
    )



# ==========================
# Main Title
# ==========================

st.title(
    "Customer Churn Prediction Dashboard"
)


st.write(
    "Predict customer churn risk and understand the reasons behind it."
)


st.divider()



# ==========================
# Inputs
# ==========================

st.subheader(
    "Customer Information"
)


col1, col2, col3 = st.columns(3)



with col1:

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )


    senior = st.selectbox(
        "Senior Citizen",
        ["No","Yes"]
    )


    partner = st.selectbox(
        "Partner",
        ["Yes","No"]
    )


    dependents = st.selectbox(
        "Dependents",
        ["Yes","No"]
    )


    tenure = st.number_input(
        "Tenure Months",
        0,
        100,
        12
    )



with col2:

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes","No"]
    )


    multiple_lines = st.selectbox(
        "Multiple Lines",
        [
            "Yes",
            "No",
            "No phone service"
        ]
    )


    internet = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )


    online_security = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


    online_backup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )



with col3:

    device_protection = st.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


    tech_support = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )



st.divider()



contract = st.selectbox(
    "Contract",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)


paperless = st.selectbox(
    "Paperless Billing",
    [
        "Yes",
        "No"
    ]
)


payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)


monthly_charges = st.number_input(
    "Monthly Charges",
    value=70.0
)


total_charges = st.number_input(
    "Total Charges",
    value=500.0
)



# ==========================
# Prediction
# ==========================

if st.button(
    "🚀 Predict Churn"
):


    customer = {

        "gender": gender,

        "SeniorCitizen":
            1 if senior=="Yes" else 0,

        "Partner": partner,

        "Dependents": dependents,

        "tenure": tenure,

        "PhoneService": phone_service,

        "MultipleLines": multiple_lines,

        "InternetService": internet,

        "OnlineSecurity": online_security,

        "OnlineBackup": online_backup,

        "DeviceProtection": device_protection,

        "TechSupport": tech_support,

        "StreamingTV": streaming_tv,

        "StreamingMovies": streaming_movies,

        "Contract": contract,

        "PaperlessBilling": paperless,

        "PaymentMethod": payment,

        "MonthlyCharges": monthly_charges,

        "TotalCharges": total_charges
    }



    df = pd.DataFrame(
        [customer]
    )


    processed = preprocessor.transform(
        df
    )


    probability = model.predict_proba(
        processed
    )[0][1]



    if probability >= 0.7:

        risk="HIGH RISK"

    elif probability >=0.4:

        risk="MEDIUM RISK"

    else:

        risk="LOW RISK"



    st.divider()


    st.subheader(
        "Prediction Result"
    )


    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=probability*100,

            title={
                "text":
                "Churn Probability (%)"
            },

            gauge={

                "axis":{
                    "range":[0,100]
                }

            }
        )
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    if risk=="HIGH RISK":

        st.error(
            "🚨 HIGH RISK"
        )

    elif risk=="MEDIUM RISK":

        st.warning(
            "⚠️ MEDIUM RISK"
        )

    else:

        st.success(
            "✅ LOW RISK"
        )



    # ======================
    # SHAP
    # ======================

    shap_output = explainer(
        processed
    )


    shap_values = shap_output.values[0]


    explanation = pd.DataFrame({

        "Feature":feature_names,

        "Impact":shap_values

    })


    explanation["Importance"] = (
        explanation["Impact"].abs()
    )


    top_features = explanation.sort_values(
        "Importance",
        ascending=False
    ).head(5)


    top_features["Feature"] = (
        top_features["Feature"]
        .apply(clean_feature_name)
    )



    st.divider()


    st.subheader(
        "Churn Drivers"
    )


    for _,row in top_features.iterrows():

        if row["Impact"] > 0:

            st.error(
                f"🔴 {row['Feature']} increases churn risk"
            )

        else:

            st.success(
                f"🟢 {row['Feature']} reduces churn risk"
            )



    st.subheader(
        "Feature Impact"
    )


    st.bar_chart(
        top_features.set_index(
            "Feature"
        )["Impact"]
    )



    # ======================
    # Recommendations
    # ======================

    recommendations=[]


    for feature in top_features["Feature"]:

        if "Contract" in feature:

            recommendations.append(
                "Offer long term contract discounts"
            )

        if "Charges" in feature:

            recommendations.append(
                "Review pricing strategy"
            )

        if "Security" in feature:

            recommendations.append(
                "Offer security packages"
            )

        if "Technical" in feature:

            recommendations.append(
                "Improve support engagement"
            )



    st.divider()


    st.subheader(
        "Recommended Actions"
    )


    for item in recommendations:

        st.write(
            "✅",
            item
        )



    # ======================
    # PDF Download
    # ======================


    pdf = create_pdf_report(

        probability,

        risk,

        top_features["Feature"].tolist(),

        recommendations

    )


    st.download_button(

        "📄 Download Churn Report",

        pdf,

        file_name="customer_churn_report.pdf",

        mime="application/pdf"

    )



st.divider()


st.caption(
    "Built with Python | XGBoost | SHAP | Streamlit"
)