import sys
import os
import time
from typing import List, Dict, Optional

# Ensure the root project directory is in the sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app.utils.database_connection import DatabaseConnectionManager

class StockRepository:
    """
    Repository class for handling stock data database operations.
    """

    def __init__(self, db_manager: DatabaseConnectionManager, retries: int = 3, delay: float = 1.0):
        """
        Initialize the repository with a database manager and retry settings.
        :param db_manager: Instance of DatabaseConnectionManager.
        :param retries: Number of retry attempts for transient failures.
        :param delay: Delay (in seconds) between retries.
        """
        self.db_manager = db_manager
        self.retries = retries
        self.delay = delay

    def insert_stock_data(self, symbol: str, company_name: str, price: float, volume: int, market_cap: float,
                          percentage_change: float, daily_price_range: float, fiftytwo_week_range: float) -> None:
        """
        Insert stock data into the database.
        Retries on transient errors.

        :param symbol: Stock symbol.
        :param company_name: Company name.
        :param price: Stock price.
        :param volume: Volume of stocks traded.
        :param market_cap: Market capitalization.
        :param percentage_change: Percentage change in stock price.
        :param daily_price_range: Daily price range.
        :param fiftytwo_week_range: 52-week price range.
        """
        query = """
        INSERT INTO stocks (symbol, company_name, price, volume, market_cap, percentage_change, 
                            daily_price_range, fiftytwo_week_range)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (symbol, company_name, price, volume, market_cap, percentage_change, daily_price_range, fiftytwo_week_range)
        self._execute_with_retry(query, params)

    def fetch_stock_data(self, symbol: str) -> Optional[Dict]:
        """
        Fetch stock data for a given symbol.

        :param symbol: Stock symbol.
        :return: Stock data for the given symbol.
        """
        query = "SELECT id, symbol, company_name, price, volume, market_cap, percentage_change, " \
                "daily_price_range, fiftytwo_week_range, date FROM stocks WHERE symbol = %s"
        params = (symbol,)
        result = self._execute_query(query, params, fetch_one=True)
        if result:
            return {
                "id": result[0],
                "symbol": result[1],
                "company_name": result[2],
                "price": result[3],
                "volume": result[4],
                "market_cap": result[5],
                "percentage_change": result[6],
                "daily_price_range": result[7],
                "fiftytwo_week_range": result[8],
                "date": result[9]
            }
        return None

    def update_stock_data(self, symbol: str, company_name: str, price: float, volume: int, market_cap: float,
                          percentage_change: float, daily_price_range: float, fiftytwo_week_range: float) -> None:
        """
        Update stock data for a given symbol.

        :param symbol: Stock symbol.
        :param company_name: Company name.
        :param price: Stock price.
        :param volume: Volume of stocks traded.
        :param market_cap: Market capitalization.
        :param percentage_change: Percentage change in stock price.
        :param daily_price_range: Daily price range.
        :param fiftytwo_week_range: 52-week price range.
        """
        query = """
        UPDATE stocks
        SET company_name = %s, price = %s, volume = %s, market_cap = %s, percentage_change = %s, 
            daily_price_range = %s, fiftytwo_week_range = %s, date = CURRENT_TIMESTAMP
        WHERE symbol = %s
        """
        params = (company_name, price, volume, market_cap, percentage_change, daily_price_range, fiftytwo_week_range, symbol)
        self._execute_with_retry(query, params)

    def delete_stock_data(self, symbol: str) -> None:
        """
        Delete stock data for a given symbol.

        :param symbol: Stock symbol.
        """
        query = "DELETE FROM stocks WHERE symbol = %s"
        params = (symbol,)
        self._execute_with_retry(query, params)

    def _execute_with_retry(self, query: str, params: tuple) -> None:
        """
        Execute a query with retry logic for transient database errors.

        :param query: SQL query to execute.
        :param params: Query parameters.
        """
        for attempt in range(1, self.retries + 1):
            try:
                with self.db_manager.get_connection() as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(query, params)
                        conn.commit()
                return
            except Exception as e:
                if attempt == self.retries:
                    raise RuntimeError(f"Database operation failed after {self.retries} attempts: {e}")
                time.sleep(self.delay)

    def _execute_query(self, query: str, params: tuple, fetch_one: bool = True) -> Optional[List[Dict]]:
        """
        Execute a query and fetch results.

        :param query: SQL query to execute.
        :param params: Query parameters.
        :param fetch_one: Whether to fetch a single record or all records.
        :return: Fetched record(s) as a dictionary.
        """
        try:
            with self.db_manager.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    records = cursor.fetchone() if fetch_one else cursor.fetchall()
                    return records
        except Exception as e:
            raise RuntimeError(f"Error executing query: {e}")
