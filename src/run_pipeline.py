import subprocess
import logging

def run_pipeline():
    """ Run the full pipeline with subprocesses """
    
    # Set up logging
    logging.basicConfig(filename='pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Step 1: Feature Engineering
    try:
        logging.info("Starting feature engineering...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/feature/run_feature_pipeline.py"], check=True)
        logging.info("Feature engineering completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Feature engineering failed: {e}")
        return
    
    # Step 2: Create Master Table
    try:
        logging.info("Creating master table...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/create_master.py"], check=True)
        logging.info("Master table created successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Creating master table failed: {e}")
        return
    
    # Step 3: Data Splitting
    try:
        logging.info("Splitting data...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/data_split.py"], check=True)
        logging.info("Data splitting completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Data splitting failed: {e}")
        return
    
    # Step 4: Model Training
    try:
        logging.info("Training model...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/model_training.py"], check=True)
        logging.info("Model training completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Model training failed: {e}")
        return
    
    # Step 5: Forecasting and Validation
    try:
        logging.info("Performing forecasting and validation...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/forecast_and_validate.py"], check=True)
        logging.info("Forecasting and validation completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Forecasting and validation failed: {e}")
        return
    
    # Step 6: Feature Importance
    try:
        logging.info("Calculating feature importance...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/src/feature_importance.py"], check=True)
        logging.info("Feature importance calculation completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Feature importance calculation failed: {e}")
        return
    
    # Step 7: App creation
    try:
        logging.info("Creating App...")
        subprocess.run(["python", "C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/run.py"], check=True)
        logging.info("App development successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"App development failed: {e}")
        return

if __name__ == "__main__":
    run_pipeline()
