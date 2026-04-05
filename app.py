from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]

        final_features = np.array([features])

        prediction = model.predict(final_features)

        result = "⚠️ High Chance of Heart Disease" if prediction[0] == 1 else "✅ Low Chance of Heart Disease"

        return render_template('index.html', result=result)

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)