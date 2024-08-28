import pandas as pd

def primary_key_dataframe(data):
    
    """renaming primary keys 'Date', 'Store', and 'department'.
       group data based on primary key
    """

    # Ensure 'Date' is in datetime format
    data['date_id'] = pd.to_datetime(data['date_id'])
    
    # Assuming 'df' is your DataFrame
    data = data.rename(columns={'date_id': 'Date', 'store': 'Store', 'item_dept': 'Department'})

    # Group the data by 'date', 'store', and 'department' and sum up 'net_sales' and 'item_qty'
    grouped_df = data.groupby(['Date', 'Store', 'Department']).agg({'net_sales': 'sum', 'item_qty': 'sum'}).reset_index()

    return grouped_df

if __name__ == "__main__":
    # Define the file paths
    filepath = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/preprocessed_data.csv'
    
    # Load the data
    df = pd.read_csv(filepath)
    
    # Process the data
    grouped_df = primary_key_dataframe(df)
    
    # Save the preprocessed data to a new CSV file
    grouped_df.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/grouped_by_primary_data.csv', index=False)

