import pandas as pd
from utils import is_holiday  # Import the utility function

def create_time_features(data):
    """Generate time-related features"""
    # Convert date column to datetime
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Day of the week (0 = Monday, 6 = Sunday)
    data['day_of_week'] = data['Date'].dt.dayofweek
    
    # Is weekend
    data['is_weekend'] = data['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
    
    # Holiday indicator using is_holiday function and converting to 1/0
    data['is_holiday'] = data['Date'].apply(is_holiday).astype(int)
       
    # Day of the month (1 to 31)
    data['day_of_month'] = data['Date'].dt.day
      
    # Is the date the start/end of the month
    data['is_month_start'] = data['Date'].dt.is_month_start.astype(int)
    data['is_month_end'] = data['Date'].dt.is_month_end.astype(int)
     
    return data


if __name__ == "__main__":
    # Assuming the CSV file is named 'data.csv' and is in the current directory
    filepath = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/define_target_data.csv'
    
    # Load the data
    data = pd.read_csv(filepath)
    
    # Apply the function
    data = create_time_features(data)
    
    # Save the preprocessed data to a new CSV file
    data.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/time_feature_data.csv', index=False)
