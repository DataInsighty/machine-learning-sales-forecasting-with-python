from flask import Flask
from config import DevelopmentConfig, TestingConfig, ProductionConfig
import os

def create_app():
    app = Flask(__name__)

    # Load configuration based on environment
    if os.getenv('FLASK_ENV') == 'production':
        app.config.from_object(ProductionConfig)
    elif os.getenv('FLASK_ENV') == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    with app.app_context():
        # Import routes
        from . import routes

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Use debug=True only in development
