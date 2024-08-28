import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import mean_absolute_percentage_error
import joblib

# Define the feature columns
feature_columns = [
    'Revenue', 'day_of_week', 'is_weekend', 'is_holiday', 'day_of_month', 
    'is_month_start', 'is_month_end', 'Revenue_growth', 'cumulative_Revenue', 
    'Revenue_per_day_of_week', 'Previous_day_revenue', 'Revenue_from_7_days_ago', 
    '7_day_rolling_average_of_revenue', 'Profile', 'Size'
]

def forecast_and_validate(test_data):
    """ Forecast and validate the time series model """
    
    # Load the trained model
    model = joblib.load('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/models/gradient_boosting_model.pkl')
    
    # Check if the necessary columns are present in test_data
    if not set(feature_columns).issubset(test_data.columns):
        missing_columns = set(feature_columns) - set(test_data.columns)
        raise ValueError(f"Missing feature columns in the test data: {missing_columns}")

    # Prepare features for prediction
    X_test = test_data[feature_columns]
    
    # Forecasting
    test_data['forecast'] = model.predict(X_test)
    
    # Ensure 'Quantity' is in the dataset for validation
    if 'Quantity' not in test_data.columns:
        raise ValueError("'Quantity' column is missing in the test data for validation.")

    # Calculate MAPE for overall
    mape = mean_absolute_percentage_error(test_data['Quantity'], test_data['forecast']) * 100
    print(f"Overall MAPE: {mape:.2f}%")
    
    # Granularity A: Store | Department
    mape_by_store_dept = (
        test_data.groupby(['Store', 'Department'])
        .apply(lambda x: mean_absolute_percentage_error(x['Quantity'], x['forecast']) * 100)
        .reset_index(name='MAPE')
    )
    
    print("MAPE by Store | Department:")
    print(mape_by_store_dept)
    
    # Granularity B: Store
    mape_by_store = (
        test_data.groupby(['Store'])
        .apply(lambda x: mean_absolute_percentage_error(x['Quantity'], x['forecast']) * 100)
        .reset_index(name='MAPE')
    )
    
    print("MAPE by Store:")
    print(mape_by_store)

    # Granularity C: Department
    mape_by_department = (
        test_data.groupby(['Department'])
        .apply(lambda x: mean_absolute_percentage_error(x['Quantity'], x['forecast']) * 100)
        .reset_index(name='MAPE')
    )
    
    print("MAPE by Department:")
    print(mape_by_department)
    
    # Save the DataFrame with forecasts
    forecasted_data = test_data[['Date', 'Store', 'Department', 'Quantity', 'forecast']]
    forecasted_data.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/forecasted_data.csv', index=False)

    # Plot the results for each Store and Department combination
    plot_forecasts(forecasted_data)


def plot_forecasts(forecasted_data):
    """ Plot actual vs forecasted data for each Store and Department combination """
    unique_combinations = forecasted_data.groupby(['Store', 'Department']).size().reset_index(name='count')

    # Set the number of rows and columns for the grid
    n_combinations = len(unique_combinations)
    n_cols = 3  # Number of columns in the grid
    n_rows = int(np.ceil(n_combinations / n_cols))  # Calculate number of rows needed

    # Create a large figure to hold the grid of plots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4), constrained_layout=True)

    # Flatten axes for easy indexing (in case of multiple rows)
    axes = axes.flatten()

    # Loop through each unique Store and Department combination and plot
    for idx, (name, group) in enumerate(forecasted_data.groupby(['Store', 'Department'])):
        # Plot Quantity vs Forecast
        sns.lineplot(x='Date', y='Quantity', data=group, ax=axes[idx], label='Actual Quantity', color='blue')
        sns.lineplot(x='Date', y='forecast', data=group, ax=axes[idx], label='Forecast', color='orange')
        
        # Set title and labels for each subplot
        axes[idx].set_title(f'Store {name[0]} - Dept {name[1]}')
        axes[idx].set_xlabel('Date')
        axes[idx].set_ylabel('Quantity / Forecast')
        
        # Rotate x-axis labels by 45 degrees
        axes[idx].tick_params(axis='x', rotation=45)
        axes[idx].legend()

    # Hide any empty subplots if n_combinations is not a perfect multiple of n_cols
    for i in range(n_combinations, n_rows * n_cols):
        fig.delaxes(axes[i])

    # Save the entire figure with all the plots
    fig.suptitle('Quantity vs Forecast by Store and Department', fontsize=16)
    plt.savefig('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/quantity_vs_forecast_grid.png')

def main():
    # Load the test data
    test_data = pd.read_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/test_data.csv')

    # Validate and forecast
    forecast_and_validate(test_data)

if __name__ == "__main__":
    main()
