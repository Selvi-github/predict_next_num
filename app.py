import numpy as np
import streamlit as st
from tensorflow import keras

# Load the model
@st.cache_resource
def load_model():
    return keras.models.load_model("model.keras")

model = load_model()

# Streamlit App Title
st.title("Keras Model Predictor")

# Description
st.write("Enter comma-separated input values (e.g. `1.2, 3.4, 5.6`) for prediction.")

# User input
user_input = st.text_input("Input values:")

# Predict on button click
if st.button("Predict"):
    try:
        input_array = np.array([float(x.strip()) for x in user_input.split(',')])
        input_array = input_array.reshape(1, -1)
        prediction = model.predict(input_array)
        st.success(f"Prediction: {prediction.tolist()}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
