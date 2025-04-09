import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import streamlit as st

# Set the page title and description
st.title("Credit Loan Eligibility Predictor")
st.write("""
This app predicts whether a loan applicant is eligible for a loan 
based on various personal and financial characteristics.
""")

# Optional password protection (remove if not needed)
#password_guess = st.text_input("Please enter your password?")
# this password is stores in streamlit secrets
#if password_guess != st.secrets["password"]:
#    st.stop()

# Load the pre-trained model
rf_pickle = open("random_forest_credit.pickle", "rb")
rf_model = pickle.load(rf_pickle)
rf_pickle.close()


# Prepare the form for individual predictions
with st.form("user_inputs"):
    st.subheader("Loan Applicant Details")
    
    # Gender input
    Gender = st.selectbox("Gender", options=["Male", "Female"])
    
    # Marital Status
    Married = st.selectbox("Marital Status", options=["Yes", "No"])
    
    # Dependents
    Dependents = st.selectbox("Number of Dependents", 
                               options=["0", "1", "2", "3+"])
    
    # Education
    Education = st.selectbox("Education Level", 
                              options=["Graduate", "Not Graduate"])
    
    # Self Employment
    Self_Employed = st.selectbox("Self Employed", options=["Yes", "No"])
    
    # Applicant Income
    ApplicantIncome = st.number_input("Applicant Monthly Income", 
                                       min_value=0, 
                                       step=1000)
    
    # Coapplicant Income
    CoapplicantIncome = st.number_input("Coapplicant Monthly Income", 
                                         min_value=0, 
                                         step=1000)
    
    # Loan Amount
    LoanAmount = st.number_input("Loan Amount", 
                                  min_value=0, 
                                  step=1000)
    
    # Loan Amount Term
    Loan_Amount_Term = st.selectbox("Loan Amount Term (Months)", 
                                    options=["360", "180", "240", "120", "60"])
    
    # Credit History
    Credit_History = st.selectbox("Credit History", 
                                  options=["1", "0"])
    
    # Property Area
    Property_Area = st.selectbox("Property Area", 
                                 options=["Urban", "Semiurban", "Rural"])
    
    # Submit button
    submitted = st.form_submit_button("Predict Loan Eligibility")




Gender_Male = 0
if Gender == "Male":
    Gender_Male = 1
elif Gender == "Female":
    Gender_Male = 0

Married_Yes = 0
if Married == "Yes":
    Married_Yes = 1
elif Married == "No":
    Married_Yes = 0

Dependents_1,Dependents_2,Dependents_3 = 0,0,0
if Dependents == 1:
    Dependents_1 = 1
elif Dependents == 2:
    Dependents_2 = 1
elif Dependents == 3:
    Dependents_3 = 1

Education_Not_Graduate = 0
if Education == "Graduate":
    Education_Not_Graduate = 0
elif Education == "Not_Graduate":
    Education_Not_Graduate = 1

Self_Employed_Yes = 0
if Self_Employed == "Yes":
    Self_Employed_Yes = 1
elif Self_Employed == "No":
    Self_Employed_Yes = 0


Property_Area_Semiurban, Property_Area_Urban = 0,0
if Property_Area == "Semiurban":
    Property_Area_Semiurban = 1
elif Property_Area == "Urban":
    Property_Area_Urban == 1
    

new_prediction = rf_model.predict(
    [[ Dependents, ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History, Gender_Male, Married_Yes,
       Education_Not_Graduate, Self_Employed_Yes,
       Property_Area_Semiurban, Property_Area_Urban
     ]]
)

st.subheader("Predicting the outcome:")
# predicted_outcome = new_prediction[0]
if new_prediction[0] == 1:
    st.write("You are eligible")
elif new_prediction[0] == 0:
    st.write("Sorry, you are not eligible for loan")



st.write(
    """We used a machine learning (Random Forest) model to predict your eligibility, the features used in this prediction are ranked by relative
    importance below."""
)
st.image("feature_importance.png")
