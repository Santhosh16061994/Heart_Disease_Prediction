# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/Santhosh T N/OneDrive/Desktop/Deploy/Heart Disease/heart_disease_model.sav', 'rb'))

# creating a function for Prediction

# creating a function for Prediction

def heart_disease_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person does not have heart disease.'
    else:
        return 'The person has heart disease.'

  
def main():
    # giving a title
    st.title('Heart Disease Prediction Web App')

    # getting the input data from the user
    age = st.text_input('Age of the person')
    sex = st.selectbox('Sex', ['Male', 'Female'])
    cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Cholesterol level')
    fbs = st.selectbox('Fasting Blood Sugar', ['< 120 mg/dl', '> 120 mg/dl'])
    restecg = st.selectbox('Resting ECG', ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'])
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
    oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest')
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
    ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', ['0', '1', '2', '3'])
    thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        # Mapping categorical variables to numerical values
        sex_mapping = {'Male': 1, 'Female': 0}
        cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
        fbs_mapping = {'< 120 mg/dl': 0, '> 120 mg/dl': 1}
        restecg_mapping = {'Normal': 0, 'ST-T wave abnormality': 1, 'Probable or definite left ventricular hypertrophy': 2}
        exang_mapping = {'No': 0, 'Yes': 1}
        slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
        ca_mapping = {'0': 0, '1': 1, '2': 2, '3': 3}
        thal_mapping = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}

        # Converting input data to numerical format
        input_data = [
            int(age),
            sex_mapping[sex],
            cp_mapping[cp],
            int(trestbps),
            int(chol),
            fbs_mapping[fbs],
            restecg_mapping[restecg],
            int(thalach),
            exang_mapping[exang],
            float(oldpeak),
            slope_mapping[slope],
            ca_mapping[ca],
            thal_mapping[thal]
        ]

        diagnosis = heart_disease_prediction(input_data)
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
