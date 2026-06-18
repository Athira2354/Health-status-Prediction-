import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title(" HEALTHY DIET & CALORIE INTAKE BASED HEALTH STATUS PREDICTION")


Age = st.number_input("Enter your Age:")

Gender = st.selectbox(
    "Select Gender",
    ["Male", "Female"]
)

Height_cm = st.number_input("Enter your Height (cm):")

Weight_kg = st.number_input("Enter your Weight (kg):")

BMI = st.number_input("Enter BMI:")

Activity_Level = st.selectbox(
    "Select Activity Level",
    [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active"
    ]
)


Daily_Calorie_Requirement = st.number_input(
    "Enter Daily Calorie Requirement:")

Daily_Calorie_Consumed = st.number_input(
    "Enter Daily Calorie Consumed:")

Protein_Intake_g = st.number_input(
    "Enter Protein Intake (g):")

Carbohydrate_Intake_g = st.number_input(
    "Enter Carbohydrate Intake (g):")

Fat_Intake_g = st.number_input(
    "Enter Fat Intake (g):")

Water_Intake_Liters = st.number_input(
    "Enter Water Intake (Liters):")

Diet_Type = st.selectbox(
    "Select Diet Type",
    [
        "Vegetarian",
        "Non-Vegetarian",
        "Vegan",
        "Keto"
    ]
)



gender_map = {
        "Female": 0,
        "Male": 1
    }

activity_map = {
        "Lightly Active": 0,
        "Moderately Active": 1,
        "Sedentary": 2,
        "Very Active": 3
    }
diet_map = {
        "Keto": 0,
        "Non-Vegetarian": 1,
        "Vegan": 2,
        "Vegetarian": 3
    }

gender_encoded = gender_map[Gender]
activity_encoded = activity_map[Activity_Level]
diet_encoded = diet_map[Diet_Type]

df = pd.DataFrame({
        "Age": [Age],
        "Gender": [gender_encoded],
        "Height_cm": [Height_cm],
        "Weight_kg": [Weight_kg],
        "BMI": [BMI],
        "Activity_Level": [activity_encoded],
        "Daily_Calorie_Requirement": [Daily_Calorie_Requirement],
        "Daily_Calorie_Consumed": [Daily_Calorie_Consumed],
        "Protein_Intake_g": [Protein_Intake_g],
        "Carbohydrate_Intake_g": [Carbohydrate_Intake_g],
        "Fat_Intake_g": [Fat_Intake_g],
        "Water_Intake_Liters": [Water_Intake_Liters],
        "Diet_Type": [diet_encoded]
    })


if st.button("PREDICT"):
    scaled_data = scaler.transform(df)
    result = model.predict(scaled_data)

    status_map = {
        0: "Healthy",
        1: "Unhealthy",
        2: "Overweight"
    }

    st.success(f"Health Status: {status_map[result[0]]}")