import streamlit as st
import joblib
import numpy as np

st.title("Anxiety Prediction App")

model = joblib.load("anxiety_model.pkl")

st.write("Fill the information below:")

age = st.number_input("Age", 10, 100)
sleep = st.number_input("Sleep hours per day", 0, 24)
stress = st.slider("Stress level (1-10)", 1, 10)

if st.button("Predict"):
    input_data = np.array([[age, sleep, stress]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Anxiety Level")
    else:
        st.success("Low Anxiety Level")
