import streamlit as st
import pickle
import numpy as np

with open("C:/Users/PC/diabetes_deploy/diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Diabetes Prediction App")

st.sidebar.header("Input Features")
pregnancies = st.sidebar.number_input("Number of Pregnancies", 0, 20, 1)
glucose = st.sidebar.number_input("Glucose Level", 0, 300, 120)
blood_pressure = st.sidebar.number_input("Blood Pressure", 0, 200, 70)
skin_thickness = st.sidebar.number_input("Skin Thickness", 0, 100, 20)
insulin = st.sidebar.number_input("Insulin Level", 0, 900, 30)
bmi = st.sidebar.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.sidebar.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.sidebar.number_input("Age", 0, 120, 25)

input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("The patient is likely to have diabetes.")
    else:
        st.success("The patient is not likely to have diabetes.")
