import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)

def convert_to_datetime(df, column_name):
    """Convert the specified column to datetime format."""
    df[column_name] = pd.to_datetime(df[column_name])
    return df

def drop_columns(df, columns_to_drop):
    """Remove specified columns from the DataFrame."""
    df = df.drop(columns=columns_to_drop, axis=1)
    return df

def preprocess_data(df):
    """Apply all preprocessing steps to the DataFrame."""
    df = convert_to_datetime(df, 'date_id')
    df = drop_columns(df, ['item', 'invoice_num'])
    return df


if __name__ == "__main__":
    # Load the data
    filepath = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/raw/transactions_info.csv'  # Replace with your actual file path
    df = load_data(filepath)
    
    # Preprocess the data
    preprocessed_df = preprocess_data(df)
    
    # Save the preprocessed data to a new CSV file
    preprocessed_df.to_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/processed/preprocessed_data.csv', index=False)


