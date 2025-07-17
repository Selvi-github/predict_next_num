import numpy as np
import streamlit as st
from tensorflow import keras

@st.cache_resource
def load_model():
    return keras.models.load_model("model.keras")

model = load_model()

st.title("🔢 LSTM: Predict Next Number")
st.write("Enter a sequence of numbers (e.g. 1, 2, 3, 4)")

user_input = st.text_input("Your sequence:")

if st.button("Predict"):
    try:
        sequence = [float(i.strip()) for i in user_input.split(",")]
        input_seq = np.array(sequence).reshape(1, -1, 1)
        prediction = model.predict(input_seq)
        st.success(f"🔮 Predicted next number: {prediction[0][0]:.4f}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
