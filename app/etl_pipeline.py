'''
etl_pipeline.py
This module defines the ETL (Extract, Transform, Load) pipeline for processing stock data. 
It includes functions to fetch raw stock data, transform the data, and insert the transformed 
data into a database. The ETL process is logged to provide information on the success or 
failure of the operations and the time taken to complete the process.
Modules:
    time: Provides various time-related functions.
    __utils.logger: Provides logging functionality.
    data_transformer: Contains the logic for transforming stock data.
    fetch_stock_data: Contains the logic for fetching raw stock data.
    stock_data_service: Contains the logic for inserting transformed stock data into a database.
Functions:
    run_etl(symbol): Executes the ETL process for a given stock symbol.
Usage:
    This script can be run as a standalone module to process a specific stock symbol.
    Example:
        python etl_pipeline.py

'''
import sys
import os
import time

# Add the base folder (dataquity) to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Config
from app.data_transformer import transform_stock_data
from app.fetch_stock_data import fetch_stock_data
from app.stock_data_service import insert_stock_data
from app.__utils.file_utils import save_data_to_file, load_data_from_file, clean_temp_files
from app.__utils.logger import get_logger

# get logger
logger = get_logger(__name__)

def run_etl(symbol):
    """
    Executes the ETL (Extract, Transform, Load) process for a given stock symbol.

    This function fetches raw stock data for the specified symbol, transforms the data, 
    inserts the transformed data into a database, and logs the success or failure 
    of the operation. It also logs the time taken to complete the process.

    Args:
        symbol (str): The stock symbol to process.

    Logs:
        Success and error messages are logged to indicate the status of the ETL process.
        The total time taken to complete the ETL process is also logged.
    """
    start_time = time.time()
    try:

        # Extract: Fetch raw data
        raw_data = fetch_stock_data(symbol)
        if raw_data:
            # Save raw data to file for debugging or reprocessing
            raw_file = save_data_to_file(f"{symbol}_raw_data.json", raw_data)
            logger.info(f"Raw data saved to file: {raw_file}")

            # Transform data
            transformed_data = transform_stock_data(raw_data)
            
            # Save transformed data to file for debugging or reprocessing
            transformed_file = save_data_to_file(f"{symbol}_transformed_data.json", transformed_data)
            logger.info(f"Transformed data saved to file: {transformed_file}")

            # Load data into database
            insert_stock_data(symbol, transformed_data)
            logger.info(f"Successfully processed {symbol}")            

    except Exception as e:
        logger.error(f"Error processing {symbol}: {e}")
    finally:
        end_time = time.time()
        logger.info(f"ETL process for {symbol} completed in {end_time - start_time:.2f} seconds")

        # Clean up temporary files after the ETL process if required
        if Config.CLEAN_TEMP_DIR: 
            logger.info(f"Clean temp dir is set to: {Config.CLEAN_TEMP_DIR}")
            logger.info(f"Cleaning temporary files...")
            clean_temp_files()


if __name__ == "__main__":
    symbol = "MSFT"  # Example: Apple stock
    run_etl(symbol)

