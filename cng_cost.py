import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("cng_savings_model.pkl")

st.set_page_config(page_title="CNG Savings Predictor")
st.title("CNG Cost Savings Predictor")
st.write("Fill in the details below to predict how much you can save using CNG compared to petrol.")

# Input form
engine_size = st.number_input("Engine Size (L)", min_value=0.5, step=0.1)
cylinder_capacity = st.number_input("CNG Cylinder Capacity (L)", min_value=10)
distance_covered = st.number_input("Distance Covered (km)", min_value=0)
installation_cost = st.number_input("Cost of Installation (₦)", min_value=0)
cost_per_scm = st.number_input("Cost per SCM of CNG (₦)", min_value=0)
cng_quantity = st.number_input("CNG Quantity (SCM)", min_value=0.0)
cost_per_fill = st.number_input("Cost per Fill (₦)", min_value=0.0)
petrol_price = st.number_input("Cost of Petrol per Litre (₦)", min_value=0)
petrol_qty = st.number_input("Quantity of Petrol Used per Distance (L)", min_value=0.0)
petrol_cost_per_distance = st.number_input("Cost of Petrol per Distance (₦)", min_value=0.0)

# Predict button
if st.button("Predict Savings"):
    input_data = np.array([[engine_size, cylinder_capacity, distance_covered,
                            installation_cost, cost_per_scm, cng_quantity, cost_per_fill,
                            petrol_price, petrol_qty, petrol_cost_per_distance]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Savings: ₦{prediction:,.2f}")
