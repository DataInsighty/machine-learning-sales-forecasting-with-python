import pandas as pd

def create_sales_features(data):
    """Generate sales-related features"""
    
    # Ensure 'Date' is datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Rename 'net_sales' to 'Revenue'
    data = data.rename(columns={'net_sales': 'Revenue'})
    
    # Revenue growth
    data['Revenue_growth'] = data['Revenue'].pct_change()
    
    # Cumulative Revenue
    data['cumulative_Revenue'] = data['Revenue'].cumsum()
    
    # Revenue per day of the week
    data['Revenue_per_day_of_week'] = data.groupby('day_of_week')['Revenue'].transform('mean')
    
    # Revenue lag features (1 day and 7 days)
    data['Revenue_lag_1'] = data['Revenue'].shift(1)
    data['Revenue_lag_7'] = data['Revenue'].shift(7)
    
    # Rolling average Revenue (7-day rolling)
    data['Revenue_7day_rolling'] = data['Revenue'].rolling(window=7).mean()
    
   
    return data


if __name__ == "__main__":
    # Define the file paths
    filepath = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/time_feature_data.csv'
    
    # Load the data
    data = pd.read_csv(filepath)
    
    # Process the data
    sales_features = create_sales_features(data)
    
    # Save the preprocessed data to a new CSV file
    sales_features.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/sales_features_data.csv', index=False)

