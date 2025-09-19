import streamlit as st
import plotly.graph_objects as go

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
    """
)

st.markdown(
    """
    This interactive tool compares **Xiaomi, Ecobee, iSmartHome, and Tuya**  
    across six benefit dimensions customers care about:  
    - Affordability  
    - Energy Savings  
    - Security  
    - Interoperability  
    - Ecosystem Breadth  
    - Personalization  
    """
)

# -------------------------------
# Dimensions & Scores
# -------------------------------
dimensions = [
    "Affordability", 
    "Energy Savings", 
    "Security", 
    "Interoperability", 
    "Ecosystem Breadth", 
    "Personalization"
]

# Example scores (scale 1–10)
companies = {
    "Xiaomi": [9, 6, 5, 6, 9, 5],
    "Ecobee": [6, 9, 7, 8, 7, 8],
    "iSmartHome": [7, 7, 6, 5, 6, 7],
    "Tuya": [8, 8, 7, 10, 8, 7]
}

# -------------------------------
# Sidebar: Company selection
# -------------------------------
st.sidebar.header("Choose companies to compare:")
selected_companies = [c for c in companies if st.sidebar.checkbox(c, True)]

# -------------------------------
# Radar Chart with Custom Colors
# -------------------------------
colors = {
    "Xiaomi": "#2F80ED",        # Blue
    "Ecobee": "#27AE60",        # Green
    "iSmartHome": "#BDBDBD",    # Grey
    "Tuya": "#000000"           # Black
}

fig = go.Figure()

for company in selected_companies:
    fig.add_trace(go.Scatterpolar(
        r=companies[company] + [companies[company][0]],  # close loop
        theta=dimensions + [dimensions[0]],
        fill='toself',
        name=company,
        line=dict(color=colors[company], width=3)
    ))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
    showlegend=True,
    template="plotly_white",
    title="Value Curve Comparison"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    "Built with ❤️ by **Group 6 – MGB Feb 25 Cohort** using [Streamlit](https://streamlit.io/) & [Plotly](https://plotly.com/python/)."
)
