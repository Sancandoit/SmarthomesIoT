import streamlit as st
import plotly.graph_objects as go

st.title("Value Curve Visualizer")

dimensions = ["Affordability","Energy Savings","Security","Interoperability","Ecosystem Breadth","Personalization"]

companies = {
    "Xiaomi": [9, 6, 5, 6, 9, 5],
    "Ecobee": [6, 9, 7, 8, 7, 8],
    "iSmartHome": [7, 7, 6, 5, 6, 7],
    "Tuya": [8, 8, 7, 10, 8, 7]
}

st.sidebar.header("Select companies")
selected = [c for c in companies if st.sidebar.checkbox(c, True)]

colors = {
    "Xiaomi": {"fill": "rgba(47,128,237,0.3)", "line": "#2F80ED"},
    "Ecobee": {"fill": "rgba(39,174,96,0.3)", "line": "#27AE60"},
    "iSmartHome": {"fill": "rgba(242,201,76,0.3)", "line": "#F2C94C"},
    "Tuya": {"fill": "rgba(235,87,87,0.3)", "line": "#EB5757"}
}

fig = go.Figure()
for company in selected:
    fig.add_trace(go.Scatterpolar(
        r=companies[company] + [companies[company][0]],
        theta=dimensions + [dimensions[0]],
        fill='toself',
        fillcolor=colors[company]["fill"],
        line=dict(color=colors[company]["line"], width=3),
        name=company
    ))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
    showlegend=True,
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("This chart compares the benefit dimensions across the four companies.")
