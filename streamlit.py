import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import psycopg2

# Streamlit UI
st.title("🌊 AI-Powered Tsunami Alert System")
st.write("Monitor and predict tsunamis in real-time using AI.")

# Visual Appeal: Tsunami Warning Image
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Tsunami_Hazard_Sign.svg/1200px-Tsunami_Hazard_Sign.svg.png", caption="Tsunami Hazard Warning", use_column_width=True)

# Emergency Response Information
st.subheader("🚨 What to Do in Case of a Tsunami?")
st.markdown("""
- Move to **higher ground** immediately.
- Follow **official alerts and warnings**.
- Do not return until authorities declare it safe.
- Stay informed via **emergency broadcast systems**.
- Have a **disaster preparedness kit** ready.
""")

# Alert Banners
st.warning("⚠️ Tsunami-prone region detected! Stay alert.")
st.info("ℹ️ Keep an emergency plan in place.")

# Prediction Section
st.subheader("🌊 Tsunami Probability Prediction")
sensor_data = st.text_area("Enter Sensor Data (comma-separated values)")
location = st.text_input("Enter Location")

def predict_tsunami(sensor_data):
    features = np.array(sensor_data).reshape(1, -1)
    prediction = np.random.rand()  # Placeholder for actual AI model prediction
    if prediction > 0.8:
        return f"🚨 Tsunami Warning at {location}! Probability: {prediction:.2f}"
    return f"✅ No Tsunami Risk at {location}. Probability: {prediction:.2f}"

if st.button("Predict Tsunami"):
    if sensor_data and location:
        try:
            sensor_values = list(map(float, sensor_data.split(',')))
            result = predict_tsunami(sensor_values)
            st.success(result)
        except ValueError:
            st.error("Please enter valid numerical sensor data.")
    else:
        st.error("Please enter valid sensor data and location.")
