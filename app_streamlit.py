import streamlit as st
from simulate import run_scenario

st.title("New Verticals Ops ROI Simulator")

clat = st.slider("CLAT improvement (percentage points)", 0.0, 5.0, 0.0, 0.1) / 100
inv  = st.slider("Inventory accuracy boost (percentage points)", 0.0, 5.0, 0.0, 0.1) / 100

result = run_scenario(clat_boost=clat, inventory_boost=inv)
st.metric("On-time delivery rate", f"{result['on_time_rate']:.2%}")
st.metric("Monthly refund cost", f"${result['refund_cost']:,.0f}")
st.metric("Net GMV", f"${result['net_gmv']:,.0f}")
