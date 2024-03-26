import numpy as np
from flask import Flask, request, jsonify , render_template , app
import pickle

app = Flask(__name__)
classifier = pickle.load(open('classifier.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    output = classifier.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = classifier.predict(final_features)
    output = prediction[0]
    if output == 1:
        return render_template("home.html", prediction_text="The person is likely to have diabetes.")
    else:
        return render_template("home.html",prediction_text="The person is not likely to have diabetes.")
if __name__ == "__main__":
    app.run(debug=True)
    