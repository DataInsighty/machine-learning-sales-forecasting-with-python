import subprocess
import logging

def run_pipeline():
    """ Run the full pipeline with subprocesses """
    
    # Set up logging
    logging.basicConfig(filename='feature_pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Step 1: Creatinng Transaction info data
    try:
        logging.info("Creating transactions_info data...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/feature/create_transactions_info.py"], check=True)
        logging.info("Transactions-info data created successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Transaction info data failed: {e}")
        return
    
    # Step 2: Data preprocessing
    try:
        logging.info("Preprocessing transactions_info data...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/feature/data_processing.py"], check=True)
        logging.info("Preprocessing done successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Preprocessing failed: {e}")
        return
    
    # Step 3: Defining primary keys
    try:
        logging.info("Defining primary keys...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/feature/create_primary_keys.py"], check=True)
        logging.info("Defining primary keys completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Defining primary keys failed: {e}")
        return
    
    # Step 4: Defining target variable
    try:
        logging.info("Defining target variable...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/feature/target_variable.py"], check=True)
        logging.info("Defining target variable completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Defining target variable failed: {e}")
        return
    
    # Step 5: Extracting and adding time related features
    try:
        logging.info("Feature Engineering Started.")
        logging.info("Extracting and adding time related features...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/feature/time_features.py"], check=True)
        logging.info("Extracting and adding time related features completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Extracting and adding time related features failed: {e}")
        return
    
    # Step 6: Extracting and adding sales related features
    try:
        logging.info("Extracting and adding sales related features ...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/feature/sales_features.py"], check=True)
        logging.info("Extracting and adding sales related features completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Extracting and adding sales related features failed: {e}")
        return
    

    # Step 7: Extracting and adding outlet related features
    try:
        logging.info("Extracting and adding outlet related features...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/feature/outlet_features.py"], check=True)
        logging.info("Extracting and adding outlet related features completed successfully.")
        logging.info("Feature Engineering completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Feature calculation failed: {e}")
        return
if __name__ == "__main__":
    run_pipeline()
