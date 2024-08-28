# src/outlet_features.py

import pandas as pd

def create_outlet_features(data):
    """Generate store-related features"""

    # Define the mappings for Profile and Size with numerical values
    profile_mapping = {
        'ABC': 1,  # Moderate
        'XYZ': 2,  # High
        # Add more store-profile mappings if needed
    }

    size_mapping = {
        'ABC': 1,  # Medium
        'XYZ': 2,  # Large
        # Add more store-size mappings if needed
    }

    # Create Profile and Size columns using the mappings
    data['Profile'] = data['Store'].map(profile_mapping)
    data['Size'] = data['Store'].map(size_mapping)

    return data

if __name__ == "__main__":
    # Define the file paths
    filepath = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/sales_features_data.csv'
    
    # Load the data
    data = pd.read_csv(filepath)
    
    # Process the data
    sales_features = create_outlet_features(data)
    
    # Save the preprocessed data to a new CSV file
    sales_features.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/outlet_features_data.csv', index=False)
    sales_features.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/feature_output.csv', index=False)

