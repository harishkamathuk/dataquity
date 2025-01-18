from flask import Blueprint, jsonify, request
from app.stock_data_service import insert_stock_data
from app.etl_pipeline import run_etl
from config import Config
from app.__utils.logger import get_logger
from app.__utils.db_connection_manager import DatabaseConnectionManager

# Get logger instance
logger = get_logger(__name__)

api_routes = Blueprint('api', __name__)

# Define a simple route
@api_routes.route('/')
def home():
    return "Hello, Flask is running!"

@api_routes.route('/api/stocks/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    """
    Fetch stock data for the given symbol from the database using DatabaseConnectionManager.
    This method will use connection pooling for efficient resource management.

    Parameters:
    symbol (str): The stock symbol for which data is being fetched.
    
    Returns:
    jsonify: A JSON response containing stock data or an error message.
    """
    db_manager = DatabaseConnectionManager()  # Initialize the connection manager

    try:
        # Acquire a connection from the pool
        connection = db_manager.get_connection()
        cursor = connection.cursor()

        # Query to fetch stock data for the given symbol
        query = """
        SELECT symbol, company_name, price, volume, market_cap, date
        FROM stocks
        WHERE symbol = %s;
        """
        cursor.execute(query, (symbol,))
        result = cursor.fetchone()  # Fetch the first matching row

        if result:
            # If data exists for the symbol, return it
            stock_data = {
                "symbol": result[0],
                "company_name": result[1],
                "price": result[2],
                "volume": result[3],
                "market_cap": result[4],
                "last_trade_time": result[5]
            }
            return jsonify(stock_data), 200
        else:
            # If no data is found for the symbol, return an error message
            return jsonify({"error": "Stock symbol not found"}), 404

    except Exception as e:
        logger.error(f"Error fetching data for symbol {symbol}: {e}")
        return jsonify({"error": "Internal server error"}), 500

    finally:
        # Release the connection back to the pool
        if connection:
            db_manager.release_connection(connection)

@api_routes.route('/api/stocks/<symbol>/etl', methods=['POST'])
def trigger_etl(symbol):
    """
    Trigger the ETL process for a given stock symbol.
    """
    try:
        run_etl(symbol)
        return jsonify({"message": f"ETL process triggered for {symbol}."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
