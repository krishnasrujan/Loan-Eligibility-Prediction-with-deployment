import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('ran_model.pkl', 'rb'))
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
    gender = int_features[5]
    education = int_features[6]
    marriage = int_features[7]
    self_employeed = int_features[8]
    dependents = int_features[9]
    property_area = int_features[10]
    

    final_features = np.array([dependents,education,applicant_income,co_applicant_income,
                                loan_amount,term,credit_history,property_area,gender,marriage,
                                self_employeed])
    
    x_final = scale.transform(final_features.reshape(1,-1))
    
    prediction = model.predict(x_final)

    if prediction == 1:
         return render_template('index.html', prediction_text='Hurray! You are eligible')
    else:
        return render_template('index.html', prediction_text='Sorry you are not eligible')

if __name__ == "__main__":
    app.run(debug=True)


