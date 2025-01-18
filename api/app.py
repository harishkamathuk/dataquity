import sys
import os
from flask import Flask
from api.routes import api_routes

# Add the base folder (dataquity) to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(api_routes)

# Run the Flask app in development mode locally
if __name__ == '__main__':
    # For local development, we use 0.0.0.0 to make it accessible on all interfaces
    # Render will automatically manage the port
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 10000)), debug=True)
    