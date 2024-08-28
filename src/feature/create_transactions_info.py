import pandas as pd

def create_transactions_info(train_file, test_file, output_file):
    # Load the training and testing data
    train_data = pd.read_csv(train_file)
    test_data = pd.read_csv(test_file)

    # Combine the datasets
    combined_data = pd.concat([train_data, test_data], ignore_index=True)

    # Save the combined dataset to a CSV file
    combined_data.to_csv(output_file, index=False)
    print(f"Combined dataset saved to {output_file}")


if __name__ == "__main__":
    # Assuming the CSV file is named 'data.csv' and is in the current directory
    train_file = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/raw/training_data.csv'
    test_file = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/raw/test_data.csv'
    output_file = 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/raw/transactions_info.csv'
    
    # Apply the function

    create_transactions_info(train_file, test_file, output_file)
    
