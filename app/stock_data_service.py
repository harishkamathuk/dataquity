from dotenv import load_dotenv
import os
import psycopg2

from app.utils.logger import get_logger
from app.utils.db_connection_manager import DatabaseConnectionManager

# Load environment variables
load_dotenv()

# Get logger
logger = get_logger(__name__)

# Initialize the DatabaseConnectionManager
db_manager = DatabaseConnectionManager()

def insert_stock_data(symbol, transformed_data):
    """
    Inserts transformed stock data into the database.

    Parameters:
        symbol (str): The stock symbol.
        transformed_data (dict): A dictionary containing transformed stock information. Expected to have the following keys:
            - 'name': The name of the company.
            - 'price': The current stock price.
            - 'volume': The trading volume.
            - 'market_cap': The market capitalization.
            - 'last_trade_time': The date and time of the last trade.
            - 'percentage_change': The percentage change in stock price.
            - 'daily_price_range': The daily price range of the stock.
            - 'fiftytwo_week_range': The 52-week price range of the stock.

    Returns:
        bool: True if the data was inserted successfully, False otherwise.
    """
    try:
        # Validate the required keys in transformed_data
        required_keys = ['name', 'price', 'volume', 'market_cap', 'last_trade_time', 'percentage_change', 'daily_price_range', 'fiftytwo_week_range']
        for key in required_keys:
            if key not in transformed_data:
                logger.error(f"Missing key {key} in transformed data for {symbol}.")
                return False  # Exit if any required key is missing

        # Get a database connection from the manager
        connection = db_manager.get_connection()
        cursor = connection.cursor()

        # Check if stock data for the symbol already exists (to prevent duplicates)
        cursor.execute("SELECT 1 FROM stocks WHERE symbol = %s AND date = %s", (symbol, transformed_data['last_trade_time']))
        if cursor.fetchone():
            logger.info(f"Data for {symbol} already exists for {transformed_data['last_trade_time']}. Skipping insertion.")
            return False  # Skip insertion if data already exists

        logger.info(f"Inserting transformed data for {symbol}")
        logger.debug(f"Transformed data for {symbol}: {transformed_data}")

        # SQL query to insert the stock data into the database
        insert_query = """
        INSERT INTO stocks (symbol, company_name, price, volume, market_cap, date, percentage_change, daily_price_range, fiftytwo_week_range)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        # Prepare the values that will be inserted
        values = (
            symbol,
            transformed_data['name'],
            transformed_data['price'],
            transformed_data['volume'],
            transformed_data['market_cap'],
            transformed_data['last_trade_time'],
            transformed_data['percentage_change'],
            transformed_data['daily_price_range'],
            transformed_data['fiftytwo_week_range']
        )

        # Log the actual SQL query along with the values
        logger.info(f"Executing SQL: {insert_query} with values: {values}")

        # Execute the query
        cursor.execute(insert_query, values)

        # Commit the transaction
        connection.commit()
        logger.info(f"Data for {symbol} inserted successfully!")
        return True

    except psycopg2.DatabaseError as db_error:
        logger.error(f"Database error inserting data for {symbol}: {db_error}")
        connection.rollback()  # Rollback in case of database error
        return False

    except Exception as e:
        logger.error(f"Unexpected error inserting data for {symbol}: {e}")
        connection.rollback()  # Rollback for unexpected errors
        return False

    finally:
        # Always close the cursor and connection using the connection manager
        db_manager.release_connection(connection)
