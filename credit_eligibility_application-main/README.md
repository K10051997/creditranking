# credit_eligibility_application
This app has been built using Streamlit and deployed with Streamlit community cloud

[Visit the app here](https://credit-eligibility.streamlit.app/)

password - streamlit

This application predicts whether someone is eligible for a loan based on inputs derived from the German Credit Risk dataset. The model aims to help users assess loan eligibility by leveraging machine learning predictions.

## Features
- User-friendly interface powered by Streamlit.
- Input form to enter details such as credit history, loan amount, income, and other relevant factors.
- Real-time prediction of loan eligibility based on the trained model.
- Accessible via Streamlit Community Cloud.

## Dataset
The application is trained on the **German Credit Risk dataset**, a widely used dataset for evaluating creditworthiness. It includes features like:
- Age
- Job
- Housing status
- Credit amount
- Duration of credit
- Purpose of loan
- And other factors influencing credit risk.

## Technologies Used
- **Streamlit**: For building the web application.
- **Scikit-learn**: For model training and evaluation.
- **Pandas** and **NumPy**: For data preprocessing and manipulation.
- **Matplotlib** and **Seaborn**: For exploratory data analysis and visualization (if applicable).

## Model
The predictive model is trained using the German Credit Risk dataset. It applies preprocessing steps like encoding categorical variables and scaling numerical features. The classification model used may include algorithms such as Logistic Regression, Random Forest, or XGBoost.

## Future Enhancements
* Adding support for multiple datasets.
* Incorporating explainability tools like SHAP to provide insights into predictions.
* Adding visualizations to better represent user input and model predictions.

## Installation (for local deployment)
If you want to run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/credit_eligibility_application.git
   cd credit_eligibility_application

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\\Scripts\\activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit application:
   ```bash
   streamlit run app.py

#### Thank you for using the Credit Eligibility Application! Feel free to share your feedback.
