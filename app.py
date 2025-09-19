import streamlit as st
import plotly.graph_objects as go
import io

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Smart Homes Value Curve", layout="wide")

# -------------------------------
# Title & Group Info
# -------------------------------
st.title("Smart Homes & IoT: Value Curve Visualizer")

st.markdown(
    """
    ### Group 6 – MGB Feb 25 Cohort  
    **Members:**  
    - Sanchit Singh Thapa  
    - Pritish Kumar Dhal  
    - Soniya Arunkumar  
    - Chandraveer Singh  

    ---
    Compare **Xiaomi, Ecobee, iSmartHome, and Tuya** across six customer benefit dimensions.  
    Toggle companies in the sidebar, switch scenarios (2024 vs. 2030), and download the chart.
    """
)

# -------------------------------
# Dimensions
# -------------------------------
dimensions = [
    "Affordability",
    "Energy Savings",
    "Security",
    "Interoperability",
    "Ecosystem Breadth",
    "Personalization"
]

# -------------------------------
# Company Scores (2024 vs. 2030)
# -------------------------------
scores_2024 = {
    "Xiaomi": [9, 6, 5, 6, 9, 5],
    "Ecobee": [6, 9, 7, 8, 7, 8],
    "iSmartHome": [7, 7, 6, 5, 6, 7],
    "Tuya": [8, 8, 7, 10, 8, 7]
}

scores_2030 = {
    "Xiaomi": [8, 7, 6, 7, 9, 6],      # more balanced but hardware-heavy
    "Ecobee": [6, 10, 8, 9, 8, 9],     # stronger in energy + personalization
    "iSmartHome": [7, 8, 7, 6, 7, 8],  # small growth
    "Tuya": [8, 9, 8, 10, 9, 9]        # dominant interoperability
}

# -------------------------------
# Sidebar Controls
# -------------------------------
st.sidebar.header("Dashboard Controls")

scenario = st.sidebar.radio("Select Scenario:", ["2024", "2030"])
scores = scores_2024 if scenario == "2024" else scores_2030

selected_companies = [c for c in scores if st.sidebar.checkbox(c, True)]

# -------------------------------
# Colors
# -------------------------------
colors = {
    "Xiaomi": {"fill": "rgba(47,128,237,0.3)", "line": "#2F80ED"},       # Blue
    "Ecobee": {"fill": "rgba(39,174,96,0.3)", "line": "#27AE60"},        # Green
    "iSmartHome": {"fill": "rgba(242,201,76,0.3)", "line": "#F2C94C"},   # Yellow
    "Tuya": {"fill": "rgba(235,87,87,0.3)", "line": "#EB5757"}           # Red
}

# -------------------------------
# Radar Chart
# -------------------------------
fig = go.Figure()

for company in selected_companies:
    fig.add_trace(go.Scatterpolar(
        r=scores[company] + [scores[company][0]],  # close loop
        theta=dimensions + [dimensions[0]],
        fill='toself',
        fillcolor=colors[company]["fill"],
        line=dict(color=colors[company]["line"], width=3),
        name=company
    ))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
    showlegend=True,
    template="plotly_white",
    title=f"Value Curve Comparison ({scenario})"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Insights Panel
# -------------------------------
insights = {
    "Xiaomi": "Excels in affordability and ecosystem breadth, but lags in security.",
    "Ecobee": "Strongest in energy savings and growing in personalization; service-led.",
    "iSmartHome": "Localized convenience player in UAE, but scalability is limited.",
    "Tuya": "Leads interoperability and acts as a neutral platform enabler for 8,400+ brands."
}

if selected_companies:
    st.subheader("Company Insights")
    for company in selected_companies:
        st.markdown(f"**{company}:** {insights[company]}")

# -------------------------------
# Export Options
# -------------------------------
st.subheader("Export Options")

# Export as HTML (interactive)
fig_json = fig.to_json()
st.download_button(
    label="📥 Download Radar Chart (Interactive HTML)",
    data=fig_json,
    file_name=f"value_curve_{scenario}.html",
    mime="application/json"
)

# Export as CSV (scores)
import pandas as pd
if selected_companies:
    export_data = pd.DataFrame({c: scores[c] for c in selected_companies}, index=dimensions)
    csv = export_data.to_csv().encode("utf-8")
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name=f"value_curve_scores_{scenario}.csv",
        mime="text/csv"
    )

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    "Built with ❤️ by **Group 6 – MGB Feb 25 Cohort** using [Streamlit](https://streamlit.io/) & [Plotly](https://plotly.com/python/)."
)
