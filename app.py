import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model

@st.cache_data(show_spinner="Loading model...")
def get_model():
    return load_model("model.keras")

model = get_model()

st.title("🔢 LSTM Number Predictor")

user_input = st.text_input("Enter a sequence of numbers separated by commas (e.g., 1,2,3,4):")

if st.button("Predict"):
    try:
        numbers = [float(x.strip()) for x in user_input.split(',')]
        input_data = np.array(numbers).reshape(1, -1, 1)
        prediction = model.predict(input_data)
        st.success(f"🔮 Predicted Next Number: {prediction[0][0]:.4f}")
    except Exception as e:
        st.error(f"Error: {e}")
