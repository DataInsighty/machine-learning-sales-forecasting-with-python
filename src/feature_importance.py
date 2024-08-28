import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt


def compute_feature_importance(training_data):
    """ Compute feature importance for a regression model """
    
    # Prepare the data by dropping non-feature columns
    feature_columns = [
        'Revenue', 'day_of_week', 'is_weekend', 'is_holiday', 'day_of_month', 
        'is_month_start', 'is_month_end', 'Revenue_growth', 'cumulative_Revenue', 
        'Revenue_per_day_of_week', 'Previous_day_revenue', 'Revenue_from_7_days_ago', 
        '7_day_rolling_average_of_revenue', 'Profile', 'Size'
    ]
    features = training_data[feature_columns]
    target = training_data['Quantity']
    
    # Train a Random Forest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(features, target)
    
    # Get feature importances
    importances = model.feature_importances_
    feature_names = features.columns
    
    # Create a DataFrame for feature importances
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)

    # Plotting the feature importances
    plt.figure(figsize=(10, 8))
    plt.barh(importance_df['Feature'], importance_df['Importance'], color='skyblue')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.title('Feature Importances')
    plt.gca().invert_yaxis()  # Display the most important feature at the top

    # Save the plot as an image file
    plt.savefig('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/feature_importances_barchart.png', bbox_inches='tight')

    
    # Save feature importances to a CSV file
    importance_df.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/feature_importance.csv', index=False)
    print("Feature importances saved to 'data/master/feature_importance.csv'")


def main():
    # Load the training data
    training_data = pd.read_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/master/training_data.csv')
    
    # Compute feature importance
    compute_feature_importance(training_data)

if __name__ == "__main__":
    main()
