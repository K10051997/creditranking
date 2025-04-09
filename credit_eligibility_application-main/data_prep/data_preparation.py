import pandas as pd


def data_prep(df):
    # convert columns to object type
    df['Credit_History'] = df['Credit_History'].astype('object')
    df['Loan_Amount_Term'] = df['Loan_Amount_Term'].astype('object')

    # impute all missing values in all the features
    #Categorical variables
    df['Gender'].fillna('Male', inplace=True)
    df['Married'].fillna(df['Married'].mode()[0], inplace=True)
    df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
    df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
    df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

    #Numerical variable
    df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)

    # Data Prep
    # drop 'Loan_ID' variable from the data. We won't need it.
    df = df.drop('Loan_ID', axis=1)

    # replace values in Loan_approved column
    df['Loan_Approved'] = df['Loan_Approved'].replace({'Y':1, 'N':0})

    # Convert categorical variables into dummy/indicator variables
    df = pd.get_dummies(df, drop_first=True)

    return df
