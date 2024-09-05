from flask import request, jsonify
from app import create_app
import joblib
import numpy as np

# Load the model
def load_model():
    with open('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/models/gradient_boosting_model.pkl', 'rb') as f:
        model = joblib.load(f)
    return model

model = load_model()

app = create_app()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract features from the JSON payload
    features = np.array(data['features']).reshape(1, -1)

    # Make a prediction
    prediction = model.predict(features)

    return jsonify({'prediction': prediction.tolist()})
