import streamlit as st

st.title("Business Model Transformation")

models = {
    "Certification-as-a-Service (Tuya)": "Turning compliance into subscription service.",
    "AI Energy Subscriptions (Ecobee, Xiaomi)": "Recurring revenue from efficiency optimization.",
    "Plug-and-play kits (iSmartHome)": "Targeting rentals and B2B installs.",
    "Cross-ecosystem API monetization (Tuya)": "Charging for interoperability.",
    "Community smart bundles (Xiaomi)": "Integration with smart city services."
}

option = st.selectbox("Choose a model to explore", list(models.keys()))
st.write(models[option])
