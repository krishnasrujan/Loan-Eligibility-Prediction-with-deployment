# Loan-Prediction-with-deployment
Predict if you are eligible to take a loan by giving few details

https://loan-eligibility-prediction.herokuapp.com/

# Data Description
Loan_ID	:- Unique Loan ID

Gender:- 	Male/ Female

Married:- 	Applicant married (Y/N)

Dependents:-	Number of dependents

Education:- Applicant Education (Graduate/ Under Graduate)

Self_Employed:-	Self employed (Y/N)

ApplicantIncome:-	Applicant income 

CoapplicantIncome:-	Coapplicant income

LoanAmount:-	Loan amount in thousands

Loan_Amount_Term:-	Term of loan in months

Credit_History:-	credit history meets guidelines

Property_Area:-	Urban/ Semi Urban/ Rural

Loan_Status:-	(Target) Loan approved (Y/N)

# Data Wrangling

Categorical features in the dataset : Gender, Married, Dependents, Education, Self_Employed, Property_Area

Numercial features in the daraset: ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History

Exploring each categorical feature and understanding the relationship between each feature and Loan status.

Observations:

1) Loan approval is more for Males.

2) There are more married applicants and the percentage of approval seems to be more for married applicants.

3) Applicants with 0 dependents are more and the percentage of approval seems to be higher for applicants with 2 dependents.

4) Non graduate applicants are less compared to graduate applicants and percentage of approval is less for non graduate applicants.

5) Major fraction of the applicants are not self-employed.

6) More number of applicants are from semi-urban areas. Percentage of approval is highest for applicants from semi-urban areas and is least for appicants from rural areas.

Filling null values:

Categorical features are filled with mode of each feature.
Even though there are outliers in numerical features, it's better to fill nulls with mean rather than median. This would preserve the distribution on the data and would work perfectly fine even if a new input is an outlier. If we fill nulls with median the model would not work well for inputs which actually contain outliers.

The dataset is highly imbalanced. So I have used SMOTENC for handling the imbalanced dataset as dataset has both categorical and numerical features. I have set the sampling strategy to 'auto' so that the imbalance is automatically. I have tried using SMOTE but it converted descrete values in categorical columns into continuous which will affect the data integrity.

# Model Building Report :

I have tested the metrics using various algorithms. I have also used voting classifer and stacked classifier and of all stacked classifer gave better results. So I have choosen it as my final model.

<img width="296" alt="metrics_loan" src="https://user-images.githubusercontent.com/48923446/96589968-14385d80-1303-11eb-8c1d-3a1f6964f60d.PNG">

Below is the feature importance graph of random forest, xgboost, logistic regression models which i have used in stacked classifier.

Random Forest Classifier

<img width="609" alt="ran_fi_le" src="https://user-images.githubusercontent.com/48923446/96589989-18647b00-1303-11eb-908f-646d444d96ba.PNG">

XGBoost Classifier

<img width="607" alt="xgb_fi_le" src="https://user-images.githubusercontent.com/48923446/96589999-1ac6d500-1303-11eb-8d2d-8258ef1aa442.PNG">

Logistic Regression

<img width="435" alt="log fi" src="https://user-images.githubusercontent.com/48923446/96590018-21554c80-1303-11eb-96d3-bf6efadf29f1.PNG">


