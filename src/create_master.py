import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def create_master(input_file, output_file):
    # Load the training data
    master_data = pd.read_csv(input_file)
    
    # Convert 'Date' column to datetime format
    master_data['Date'] = pd.to_datetime(master_data['Date'])

    # Format float columns to two decimal places
    float_columns = master_data.select_dtypes(include=['float64']).columns
    master_data[float_columns] = master_data[float_columns].round(2)

    # Rename columns as specified
    master_data = master_data.rename(columns={
        'Revenue_lag_1': 'Previous_day_revenue',
        'Revenue_lag_7': 'Revenue_from_7_days_ago',
        'Revenue_7day_rolling': '7_day_rolling_average_of_revenue'
    })

    # Move 'Quantity' column to be the last column
    cols = [col for col in master_data.columns if col != 'Quantity'] + ['Quantity']
    master_data = master_data[cols]

    
    # Standardize numeric columns using MinMaxScaler
    # Identify numeric columns (excluding 'Date' and 'Quantity')
    numeric_columns = master_data.select_dtypes(include=[np.number]).columns.tolist()
    columns_to_scale = [col for col in numeric_columns if col not in ['Quantity']]

    # Initialize MinMaxScaler
    scaler = MinMaxScaler()

    # Apply the scaler to the selected columns
    master_data[columns_to_scale] = scaler.fit_transform(master_data[columns_to_scale])


    # Save the preprocessed data to CSV
    master_data.to_csv(output_file, index=False)
    
    return master_data

# Usage:

def main():
    # Path to the master table
    input_file = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/feature_output.csv'
    output_file = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/master_data.csv'

    
    # create master data
    create_master(input_file, output_file)

if __name__ == "__main__":
    main()
