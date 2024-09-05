from flask import request, jsonify, current_app
from . import app
from model import predict

@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        # Extract features from request data
        data = request.json  # Expecting a JSON payload
        features = data['features']

        # Make prediction using the model
        prediction = predict(features)

        # Return the prediction as JSON
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        # Handle exceptions
        current_app.logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500
