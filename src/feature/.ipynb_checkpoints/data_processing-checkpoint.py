import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)

def handle_missing_values(df):
    """Handle missing values in the DataFrame."""
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].median(), inplace=True)
    
    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    
    return df

def convert_negative_values(df, column_name):
    """Convert negative values in the specified column to positive."""
    df[column_name] = df[column_name].abs()
    return df

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
    df = handle_missing_values(df)
    df = convert_negative_values(df, 'item_qty')
    df = convert_to_datetime(df, 'date_id')
    df = drop_columns(df, ['item', 'invoice_num'])
    return df

data = load_data('C:/Users/LENOVO/Documents/All_Python/MLQ5/project/data/raw/transactions_info.csv')
processed_data = preprocess_data(data)
print(processed_data.head())
