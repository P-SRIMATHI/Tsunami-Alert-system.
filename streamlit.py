import streamlit as st
import numpy as np
import pandas as pd

st.title("AI-Powered Disaster Alert System")
st.write("Monitor and predict disasters in real-time.")

# Generate Fake Data
df = pd.DataFrame({
    'Time': range(1, 11),
    'Sensor Readings': np.random.randint(50, 150, size=10)
})

# Line Chart (Using Streamlit’s built-in feature)
st.subheader("Sensor Data Over Time")
st.line_chart(df.set_index('Time'))

# Map Visualization
st.subheader("Disaster-Prone Areas")
df_map = pd.DataFrame({'lat': [13.0827, 12.9716], 'lon': [80.2707, 77.5946]})
st.map(df_map)

# Prediction Input
st.subheader("Disaster Prediction")
sensor_data = st.text_input("Enter Sensor Data (comma-separated values)")
location = st.text_input("Enter Location")

if st.button("Predict Disaster"):
    if sensor_data and location:
        probability = np.random.rand()  # Fake Probability
        st.success(f"Prediction at {location}: {probability:.2f} probability of disaster.")
    else:
        st.error("Please enter valid sensor data and location.")
