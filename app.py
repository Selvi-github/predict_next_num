import streamlit as st
import numpy as np
from tensorflow import keras

st.title("📈 LSTM Model: Next Number Predictor")

@st.cache_resource
def load_model():
    return keras.models.load_model("model.keras")

model = load_model()

st.markdown("### 🔢 Enter numbers (comma-separated):")
user_input = st.text_input("Example: `1, 2, 3`")

if st.button("Predict"):
    try:
        values = np.array([float(x.strip()) for x in user_input.split(',')])
        input_array = values.reshape(1, -1, 1)  # LSTM expects 3D input: (batch, timesteps, features)
        prediction = model.predict(input_array)
        st.success(f"✅ Prediction: {prediction[0][0]}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
