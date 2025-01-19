from dotenv import load_dotenv
import os
import requests
import logging

from config import Config
from app.utils.logger import get_logger

# get logger
logger = get_logger(__name__)

def fetch_stock_data(symbol):
    """
    Fetch stock data for a given symbol from the stock data API.
    Args:
        symbol (str): The stock symbol to fetch data for.
    Returns:
        dict: A dictionary containing the stock data for the given symbol if successful.
        None: If there was an error fetching the data or the data is invalid.
    Raises:
        ValueError: If the fetched data does not contain valid stock information.
        requests.exceptions.RequestException: For network-related or other request exceptions.
    """
    try:
        
        logger.info(f"Fetching stock data for symbol: {symbol}")
        
        params = {
            'api_token': Config.STOCKDATA_API_KEY,
            'symbols': symbol
        }
    
        # Attempt to fetch data from the API
        response = requests.get(Config.STOCKDATA_API_URL, params=params)

        # Check for successful status code
        response.raise_for_status()  # Will raise HTTPError for bad responses
        
        # Parse the JSON data
        data = response.json()
        
        # Check if the data is valid
        if 'data' not in data:
            raise ValueError("No stock data found.")
        
        logger.info(f"Stock data successfully fetched for {symbol}")        
        return data['data'][0]  # Return the first stock entry

    except requests.exceptions.RequestException as e:
        # Handle network-related or other request exceptions
        logger.error(f"Error fetching data from API: {e}")
        return None

    except ValueError as e:
        # Handle data structure errors
        logger.error(f"Error with data: {e}")
        return None

