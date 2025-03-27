import streamlit as st  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
import pydeck as pdk  

# Title  
st.title("🌍 AI-Powered Disaster Alert System")  
st.write("Monitor and visualize disaster risks with AI.")  

# User Input  
location = st.text_input("📍 Enter Location")  
sensor_data = st.text_area("📊 Enter Sensor Data (comma-separated values)")  

if st.button("Analyze"):  
    if location and sensor_data:  
        sensor_values = list(map(float, sensor_data.split(',')))  
        prediction = np.random.rand()  # Mock AI prediction  

        # Display Prediction  
        if prediction > 0.7:  
            st.error(f"🚨 High disaster risk detected at {location}! Probability: {prediction:.2f}")  
        else:  
            st.success(f"✅ No significant disaster risk at {location}. Probability: {prediction:.2f}")  

        # Bar Chart  
        st.write("📊 **Sensor Data Distribution**")  
        fig, ax = plt.subplots()  
        ax.bar(range(len(sensor_values)), sensor_values, color='skyblue')  
        ax.set_xlabel("Sensor Index")  
        ax.set_ylabel("Value")  
        ax.set_title("Sensor Data Visualization")  
        st.pyplot(fig)  

        # Line Chart (Sensor Trends)  
        st.write("📈 **Sensor Data Trends**")  
        df = pd.DataFrame({"Time": range(1, len(sensor_values) + 1), "Sensor Value": sensor_values})  
        st.line_chart(df.set_index("Time"))  

        # Map Visualization  
        st.write("🗺️ **Disaster Risk Location Map**")  
        map_data = pd.DataFrame({"lat": [13.0827], "lon": [80.2707]})  # Example: Chennai  
        st.map(map_data)  

    else:  
        st.error("⚠️ Please enter valid inputs.")  
