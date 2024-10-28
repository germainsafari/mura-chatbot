# backend/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from routes import auth_blueprint, chat_blueprint

# Initialize Flask app
app = Flask(__name__)

# Load configuration from the config file
app.config.from_object(Config)

# Initialize extensions
db = SQLAlchemy(app)          # Initialize SQLAlchemy
jwt = JWTManager(app)        # Initialize JWT Manager
CORS(app)                    # Enable CORS

# Register Blueprints (for authentication and chat routes)
app.register_blueprint(auth_blueprint, url_prefix="/api/auth")
app.register_blueprint(chat_blueprint, url_prefix="/api/chat")

# Main entry point
if __name__ == '__main__':
    with app.app_context():  # Ensure the app context is available for database operations
        db.create_all()      # Create database tables
    app.run(debug=True)       # Run the Flask app in debug mode
