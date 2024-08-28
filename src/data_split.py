import pandas as pd

def split_data(master_data, feature_columns, target_column):
    """ Split the master data based on date ranges and save training and test datasets """
    
    # Convert 'Date' column to datetime
    master_data['Date'] = pd.to_datetime(master_data['Date'])
    
    # Split the data into training and testing based on the date ranges
    training_data = master_data[(master_data['Date'] >= '2021-11-01') & (master_data['Date'] <= '2022-01-31')]
    test_data = master_data[(master_data['Date'] >= '2022-02-01') & (master_data['Date'] <= '2022-02-28')]
   
    # Save to CSV files
    training_data.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/training_data.csv', index=False)
    test_data.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/test_data.csv', index=False)
   
    # Prepare features (X) and target (y)
    X_train = training_data[feature_columns]
    y_train = training_data[target_column]
    
    X_test = test_data[feature_columns]
    y_test = test_data[target_column]
    
    # Save to CSV files
    X_train.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/split/X_train.csv', index=False)
    y_train.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/split/y_train.csv', index=False)
    X_test.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/split/X_test.csv', index=False)
    y_test.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/split/y_test.csv', index=False)

# Example usage
if __name__ == "__main__":
    # Load your master data here
    master_data = pd.read_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/master_data.csv')
    
    # Define your feature columns and target column
    feature_columns = ['Revenue', 'day_of_week', 'is_weekend', 'is_holiday', 'day_of_month', 
                       'is_month_start', 'is_month_end', 'Revenue_growth', 
                       'cumulative_Revenue', 'Revenue_per_day_of_week', 
                       'Previous_day_revenue', 'Revenue_from_7_days_ago', 
                       '7_day_rolling_average_of_revenue', 'Profile', 'Size']
    target_column = 'Quantity'
    
    split_data(master_data, feature_columns, target_column)
