from dotenv import load_dotenv
import os
import psycopg2

from app.__utils.logger import get_logger
from app.__utils.db_connection_manager import DatabaseConnectionManager

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

    Returns:
        None
    """
    try:
        # Get a database connection from the manager
        connection = db_manager.get_connection()
        cursor = connection.cursor()

        logger.info(f"Inserting transformed data for {symbol}")
        logger.debug(f"Transformed data for {symbol}: {transformed_data}")

        # SQL query to insert the stock data into the database
        insert_query = """
        INSERT INTO stocks (symbol, company_name, price, volume, market_cap, date)
        VALUES (%s, %s, %s, %s, %s, %s);
        """

        # Prepare the values that will be inserted
        values = (
            symbol,
            transformed_data['name'],
            transformed_data['price'],
            transformed_data['volume'],
            transformed_data['market_cap'],
            transformed_data['last_trade_time']
        )

        # Log the actual SQL query along with the values
        logger.info(f"Executing SQL: {insert_query} with values: {values}")

        # Execute the query
        cursor.execute(insert_query, values)

        # Commit the transaction
        connection.commit()
        logger.info(f"Data for {symbol} inserted successfully!")

    except Exception as e:
        logger.error(f"Error inserting data into the database: {e}")
        connection.rollback()  # Rollback in case of error

    finally:
        # Always close the cursor and connection using the connection manager
        db_manager.release_connection(connection)
