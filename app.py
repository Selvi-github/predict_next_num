import numpy as np
import streamlit as st
from tensorflow import keras

@st.cache_resource
def load_model():
    return keras.models.load_model("model.keras")

model = load_model()

st.title("🔢 LSTM: Predict Next Number")
st.write("Enter a sequence (e.g., 1,2,3,4):")

user_input = st.text_input("Sequence:")

if st.button("Predict"):
    try:
        data = [float(x.strip()) for x in user_input.split(',')]
        input_array = np.array(data).reshape(1, -1, 1)
        prediction = model.predict(input_array)
        st.success(f"🔮 Predicted Next Number: {prediction[0][0]:.4f}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
