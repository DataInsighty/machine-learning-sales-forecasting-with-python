import pandas as pd

def define_target_variable(data):
    """
    Defining target variable ""Quantity"" by renaming 'item_qty' column.
    """
    data = data.rename(columns={'item_qty': 'Quantity'})
    

    return data

if __name__ == "__main__":
    # Define the file paths
    filepath = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/grouped_by_primary_data.csv'
    
    # Load the data
    data = pd.read_csv(filepath)
    
    # Process the data
    define_target = define_target_variable(data)
    
    # Save the preprocessed data to a new CSV file
    define_target.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/define_target_data.csv', index=False)

