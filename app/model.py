import pickle
import numpy as np

# Load your trained model
def load_model():
    with open('C:/Users/Users/Documents/ML Project/models/gradient_boosting_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Make a prediction
def predict(input_data):
    model = load_model()
    input_data = np.array(input_data).reshape(1, -1)  # Reshape if needed
    prediction = model.predict(input_data)
    return prediction

    
