# Diabetes Prediction App 🩺

## Description  
A simple web application built using **Streamlit** to predict whether a patient is likely to have diabetes. The prediction is based on user-inputted medical features such as glucose level, blood pressure, BMI, and more.  

## Features  
- User-friendly interface for inputting medical data.  
- Real-time prediction using a pre-trained machine learning model.  
- Displays results clearly with success or error messages.  

## Installation  
To run the application locally, follow these steps:  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/diabetes-prediction-app.git
   cd diabetes-prediction-app
Install the required dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

Input Features
The app requires the following inputs:

Number of Pregnancies: Number of times the patient has been pregnant.
Glucose Level: Blood glucose level (mg/dL).
Blood Pressure: Diastolic blood pressure (mm Hg).
Skin Thickness: Triceps skinfold thickness (mm).
Insulin Level: Serum insulin level (μU/ml).
BMI: Body Mass Index (weight in kg/(height in m)^2).
Diabetes Pedigree Function: A measure of diabetes hereditary risk.
Age: Age of the patient (years).
Example
Enter the required medical data in the sidebar.
Click the "Predict" button.
The app will display either:
🚨 "The patient is likely to have diabetes."
✅ "The patient is not likely to have diabetes."
Files
app.py: Main application file for the Streamlit app.
diabetes_model.pkl: Pre-trained machine learning model.
requirements.txt: List of Python dependencies.
Model Details
The model was trained using the Pima Indians Diabetes Database.
It predicts diabetes likelihood based on medical features.
Dependencies
Streamlit
Numpy
Pickle
Install them using:
pip install streamlit numpy
Screenshots
Here’s how the app looks:

Author
👨‍💻 Nader Nageh Mansour

Email: nadernageh22508@gmail.com
GitHub: [Your GitHub Profile](https://github.com/nader108)
License
This project is licensed under the MIT License.
Feel free to use it, modify it, and share it.

