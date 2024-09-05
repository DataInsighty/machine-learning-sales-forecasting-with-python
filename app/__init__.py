from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration (if needed)
    # app.config.from_object('config.DevelopmentConfig')

    with app.app_context():
        from . import routes  # Import routes

    return app
