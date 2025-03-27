import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import psycopg2

# Sample Data for Visualization
df = pd.DataFrame({
    'Time': pd.date_range(start='1/1/2024', periods=10, freq='H'),
    'Sensor Readings': np.random.randint(50, 150, size=10)
})

# Streamlit UI
st.title("AI-Powered Tsunami Alert System")
st.write("Monitor and predict tsunamis in real-time using AI.")

# Line Chart using Streamlit's built-in chart
st.subheader("Sensor Data Over Time")
st.line_chart(df.set_index('Time'))

# Map Visualization
st.subheader("Disaster-Prone Areas")
df_map = pd.DataFrame({
    'lat': [13.0827, 12.9716, 28.7041],
    'lon': [80.2707, 77.5946, 77.1025],
    'location': ['Chennai', 'Bangalore', 'Delhi']
})
st.map(df_map)

# Prediction Section
st.subheader("Tsunami Probability Prediction")
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
