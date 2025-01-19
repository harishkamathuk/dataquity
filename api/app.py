import sys
import os
from flask import Flask
from waitress import serve

# Add the base folder (dataquity) to the sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.routes import api_routes
from config import Config
from app.utils.logger import get_logger

# get logger
logger = get_logger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(api_routes)

# Run the Flask app in development mode locally
if __name__ == '__main__':
    # For local development, we use 0.0.0.0 to make it accessible on all interfaces
    # Render will automatically manage the port
    logger.info("Starting Flask app in {Config.FLASK_ENV} mode")
    if Config.FLASK_ENV == 'production':
        # Use Gunicorn in production (when FLASK_ENV is set to 'production')
        logger.info("Gunicorn should be started via Procfile or command line.")
    else:
        # Use Waitress locally
        serve(app, host='0.0.0.0', port=5000)
