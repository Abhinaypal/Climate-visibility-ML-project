import streamlit as st

# 🔥 MUST BE FIRST
st.set_page_config(page_title="Climate Visibility", layout="centered")

import sys
import os

# fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.predict import predict_all

# ==============================
# UI START
# ==============================

st.title("🌫️ CLIMATE VISIBILITY SYSTEM")

st.markdown("""
### 🔍 Enter Weather Conditions

- 🌡️ Temperature in **°F**
- 💧 Humidity in **%**
- 🌬️ Wind Speed in **mph**
- 🌫️ Fog likely when **Temp ≈ Dew Point**
""")

st.divider()

# ==============================
# INPUT SECTION
# ==============================

col1, col2 = st.columns(2)

with col1:
    humidity = st.slider("💧 Relative Humidity (%)", 0, 100, 50)
    temp = st.number_input("🌡️ Dry Bulb Temperature (°F)", value=70.0)

with col2:
    dew = st.number_input("🌫️ Dew Point Temperature (°F)", value=60.0)
    wind = st.number_input("🌬️ Wind Speed (mph)", value=5.0)

# 🔥 ADD HOUR (important feature)
hour = st.slider("🕒 Hour of Day", 0, 23, 12)

# ==============================
# DERIVED FEATURE
# ==============================

dew_diff = temp - dew

st.info(f"📊 Dew Point Depression: {dew_diff:.2f}")

# ==============================
# INPUT DICTIONARY
# ==============================

user_input = {
    "RelativeHumidity": humidity,
    "DRYBULBTEMPF": temp,
    "DewPointTempF": dew,
    "WindSpeed": wind,
    "hour": hour,
    "dew_point_depression": dew_diff
}

# ==============================
# PREDICTION
# ==============================

st.divider()

if st.button("🚀 Predict Fog"):

    fog_result, visibility = predict_all(user_input)

    # Fog Output
    if "RED" in fog_result:
        st.error("🚨 " + fog_result)
    elif "YELLOW" in fog_result:
        st.warning("⚠️ " + fog_result)
    else:
        st.success("✅ " + fog_result)

    # Visibility Output
    st.info(f"👁️ Visibility: {visibility:.2f} km")

# ==============================
# FOOTER
# ==============================

st.markdown("---")
st.caption("Built using Machine Learning (XGBoost) • Fog Prediction System")