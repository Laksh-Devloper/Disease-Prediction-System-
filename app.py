import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu(
        menu_title="Disease Prediction System by Laksh",
        options=["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        icons=["activity", "heart", "person"],
        default_index=0,
    )

# Diabetes Prediction Interface
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")
    
    pregnancies = st.number_input("Pregnancies", min_value=0)
    glucose = st.number_input("Glucose", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    age = st.number_input("Age", min_value=0)
    
    
    if st.button("Predict Diabetes"):
        input_data = np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age])
        input_data = input_data.reshape(1, -1)
        prediction = diabetes_model.predict(input_data)
        if prediction[0] == 0:
            st.success("The person is Healthy!")
        else:
            st.error("The person has Diabetes.")

# Heart Disease Prediction Interface
elif selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")
    
    age = st.number_input("Age", min_value=0)
    sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    cp = st.number_input("Chest Pain Type (CP)", min_value=0, max_value=3)
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=0)
    chol = st.number_input("Cholesterol (chol)", min_value=0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    restecg = st.number_input("Resting Electrocardiographic Results (restecg)", min_value=0, max_value=2)
    thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=0)
    exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", min_value=0.0, format="%.1f")
    slope = st.number_input("Slope of the Peak Exercise ST Segment (slope)", min_value=0, max_value=2)
    ca = st.number_input("Number of Major Vessels (ca)", min_value=0, max_value=4)
    thal = st.number_input("Thalassemia (thal)", min_value=0, max_value=3)
    
    if st.button("Predict Heart Disease"):
        input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        input_data = input_data.reshape(1, -1)
        prediction = heart_model.predict(input_data)
        if prediction[0] == 0:
            st.success("The person is Healthy!")
        else:
            st.error("The person has Heart Disease.")

# Parkinson's Prediction Interface
elif selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction")
    
    mdvp_fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0, format="%.2f")
    mdvp_fhi = st.number_input("MDVP:Fhi(Hz)", min_value=0.0, format="%.2f")
    mdvp_flo = st.number_input("MDVP:Flo(Hz)", min_value=0.0, format="%.2f")
    mdvp_jitter_percent = st.number_input("MDVP:Jitter(%)", min_value=0.0, format="%.5f")
    mdvp_jitter_abs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0, format="%.5f")
    mdvp_rap = st.number_input("MDVP:RAP", min_value=0.0, format="%.5f")
    mdvp_ppq = st.number_input("MDVP:PPQ", min_value=0.0, format="%.5f")
    jitter_ddp = st.number_input("Jitter:DDP", min_value=0.0, format="%.5f")
    mdvp_shimmer = st.number_input("MDVP:Shimmer", min_value=0.0, format="%.5f")
    mdvp_shimmer_db = st.number_input("MDVP:Shimmer(dB)", min_value=0.0, format="%.5f")
    shimmer_apq3 = st.number_input("Shimmer:APQ3", min_value=0.0, format="%.5f")
    shimmer_apq5 = st.number_input("Shimmer:APQ5", min_value=0.0, format="%.5f")
    mdvp_apq = st.number_input("MDVP:APQ", min_value=0.0, format="%.5f")
    shimmer_dda = st.number_input("Shimmer:DDA", min_value=0.0, format="%.5f")
    nhr = st.number_input("NHR", min_value=0.0, format="%.5f")
    hnr = st.number_input("HNR", min_value=0.0, format="%.2f")
    rpde = st.number_input("RPDE", min_value=0.0, format="%.5f")
    dfa = st.number_input("DFA", min_value=0.0, format="%.5f")
    spread1 = st.number_input("Spread1", format="%.5f")
    spread2 = st.number_input("Spread2", format="%.5f")
    d2 = st.number_input("D2", min_value=0.0, format="%.5f")
    ppe = st.number_input("PPE", min_value=0.0, format="%.5f")
    
    if st.button("Predict Parkinson's"):
        input_data = np.array([mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitter_percent, mdvp_jitter_abs, mdvp_rap,
                               mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, shimmer_apq3, shimmer_apq5,
                               mdvp_apq, shimmer_dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe])
        input_data = input_data.reshape(1, -1)
        prediction = parkinsons_model.predict(input_data)
        if prediction[0] == 0:
            st.success("The person is Healthy!")
        else:
            st.error("The person has Parkinson's Disease.")
