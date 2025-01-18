import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class to centralize app settings."""
    
    # Database configuration
    DATABASE_URL = os.getenv("DATABASE_URL")
    
    # API configuration
    STOCKDATA_API_KEY = os.getenv("STOCKDATA_API_KEY")
    STOCKDATA_API_URL = os.getenv("STOCKDATA_API_URL")
    
    # Logging configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "logs/app.log")
    
    # Temporary file storage path
    TEMP_DIR = os.getenv("TEMP_DIR", "data/temp/")
    
    @staticmethod
    def validate():
        """Validate required environment variables."""
        required_vars = ["DATABASE_URL", "STOCKDATA_API_KEY", "STOCKDATA_API_URL"]
        for var in required_vars:
            if not getattr(Config, var):
                raise ValueError(f"Missing required environment variable: {var}")
        
# Optionally validate config on startup
Config.validate()
