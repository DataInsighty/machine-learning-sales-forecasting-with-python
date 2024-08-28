from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from skopt import BayesSearchCV
from skopt.space import Real, Integer
from sklearn.metrics import mean_squared_error
import joblib
import pandas as pd

def load_data():
    """ Load training and test data from CSV files """
    X_train = pd.read_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/split/X_train.csv')
    y_train = pd.read_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/split/y_train.csv').values.ravel()
    X_test = pd.read_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/split/X_test.csv')
    y_test = pd.read_csv('C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/data/split/y_test.csv').values.ravel()
    return X_train, X_test, y_train, y_test

def train_and_optimize_gradient_boosting(X_train, X_test, y_train, y_test):
    """ Train and optimize Gradient Boosting model with Bayesian optimization. """
    
    # Define the imputer to handle missing values
    imputer = SimpleImputer(strategy='mean')
    
    # Define the Gradient Boosting model
    model = GradientBoostingRegressor()
    
    # Define the parameter space for Bayesian optimization
    param_space = {
        'model__n_estimators': Integer(50, 300),
        'model__learning_rate': Real(0.01, 0.3, prior='uniform'),
        'model__max_depth': Integer(3, 10),
        'model__min_samples_split': Integer(2, 20),
        'model__min_samples_leaf': Integer(1, 20),
        'model__subsample': Real(0.5, 1.0, prior='uniform')
    }
    
    # Create a pipeline with imputation and model
    pipeline = Pipeline([
        ('imputer', imputer),
        ('model', model)
    ])
    
    # Set up Bayesian optimization using BayesSearchCV
    optimizer = BayesSearchCV(
        pipeline,
        param_space,
        n_iter=50,
        cv=5,
        n_jobs=-1,
        scoring='neg_mean_squared_error',
        random_state=42
    )
    
    # Fit the model
    optimizer.fit(X_train, y_train)
    
    # Print the best parameters and score
    print("Best parameters found: ", optimizer.best_params_)
    print("Best score found: ", optimizer.best_score_)
    
    # Make predictions and evaluate the model
    y_pred = optimizer.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    # Save the best model
    joblib.dump(optimizer.best_estimator_, 'C:/Users/LENOVO/Documents/ML Time Series Forecasting/project/models/gradient_boosting_model.pkl')

def main():
    # Load the training and test data
    X_train, X_test, y_train, y_test = load_data()
    
    # Train and optimize Gradient Boosting model
    train_and_optimize_gradient_boosting(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()
