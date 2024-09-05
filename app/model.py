import joblib
import numpy as np

# Load your trained model
def load_model():
    with open('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/models/gradient_boosting_model.pkl', 'rb') as f:
        model = joblib.load(f)
    return model

# Make a prediction
def predict(input_data):
    model = load_model()
    input_data = np.array(input_data).reshape(1, -1)  # Reshape if needed
    prediction = model.predict(input_data)
    return prediction

    
