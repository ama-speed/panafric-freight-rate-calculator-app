import streamlit as st

st.title("Panafric Logistics Cost Calculator")

weight = st.number_input("Enter Weight (kg)", min_value=0.0)
distance = st.number_input("Enter Distance (km)", min_value=0.0)
mode = st.selectbox("Select Transport Mode", ["Road", "Air", "Sea"])

if st.button("Calculate Cost"):
    if mode == "Road":
        rate = 0.5
    elif mode == "Air":
        rate = 2.0
    else:
        rate = 0.3

    cost = weight * distance * rate / 100
    st.success(f"Estimated Transport Cost: ${cost:.2f}")