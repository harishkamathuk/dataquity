import sys
import os

# Add the base folder (dataquity) to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from api.routes import api_routes


# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(api_routes)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Debug mode for easier development    