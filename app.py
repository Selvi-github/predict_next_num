import numpy as np
import streamlit as st
from tensorflow import keras

# Load model
@st.cache_resource
def load_model():
    return keras.models.load_model("model.keras")

model = load_model()

st.title("Keras Model Predictor")
st.write("Enter comma-separated numbers for prediction (e.g., 1.0, 2.0, 3.0)")

user_input = st.text_input("Input values:")

if st.button("Predict"):
    try:
        input_values = [float(x.strip()) for x in user_input.split(',')]
        input_array = np.array(input_values).reshape(1, -1)
        prediction = model.predict(input_array)
        st.success(f"Prediction: {prediction.tolist()}")
    except Exception as e:
        st.error(f"Error: {e}")
