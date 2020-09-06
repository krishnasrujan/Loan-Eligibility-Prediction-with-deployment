import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('loan_eligibility.pkl', 'rb'))
scale = pickle.load(open('scale.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    applicant_income = int_features[0]/100
    co_applicant_income = int_features[1]/100
    loan_amount = int_features[2]/10000
    term = int_features[3]
    credit_history = int_features[4]
    education = int_features[5]
    total_income = applicant_income+co_applicant_income
    dependents = int_features[6]
    property_area = int_features[7]
    
    loan_amount = np.log(loan_amount)
    
    

    final_features = np.array([applicant_income,co_applicant_income,
                                loan_amount,term,credit_history,education,
                                total_income,dependents,property_area])
    
    x_final = scale.transform(final_features.reshape(1,-1))
    
    prediction = model.predict(x_final)

    if prediction == 1:
         return render_template('index.html', prediction_text='Hurray! You are eligible')
    else:
        return render_template('index.html', prediction_text='Sorry you are not eligible')

if __name__ == "__main__":
    app.run(debug=True)


