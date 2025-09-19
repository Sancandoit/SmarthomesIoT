import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.title("Company Readiness Heatmap")

data = pd.DataFrame({
    "Compliance":[9,8,6,5],
    "Ecosystem":[8,7,9,5],
    "Energy":[7,9,6,6],
    "Interoperability":[10,8,6,5],
    "Scalability":[8,7,9,4]
}, index=["Tuya","Ecobee","Xiaomi","iSmartHome"])

fig, ax = plt.subplots(figsize=(8,4))
sns.heatmap(data, annot=True, cmap="YlGnBu", ax=ax, cbar=True)
st.pyplot(fig)

st.markdown("Tuya and Ecobee show high readiness; Xiaomi is medium; iSmartHome is lower.")
