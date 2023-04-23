from flask import Flask, render_template, request
import pickle
import sklearn
import pandas as pd
import numpy as np


app = Flask(__name__)
model = pickle.load(open('ckd.pk1', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict.html', methods=['POST', 'GET'])
def prediction():
    return render_template('predict.html')


@app.route('/home.html', methods=['POST', 'GET'])
def my_home():
    return render_template('home.html')


@app.route('/output.html', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ['blood_urea', 'blood_glucose_random', 'aanemia', 'coronary_artery_disease',
                     'pus_cell', 'red_blood_cells', 'diabetesmellitus', 'Pedal_edema']
    df = pd.DataFrame(features_value, columns=features_name)

    model.predict(df)
    if output == 1:
        return render_template('output.html', prediction_text="Great! you don't have CKD ")
    else:
        return render_template('output.html', prediction_text="You have CKD")


if __name__ == '__main__':
    app.run(debug=True)
