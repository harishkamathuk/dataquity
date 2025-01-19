import os
import psycopg2
from psycopg2 import pool
from threading import Lock

from config import Config

class DatabaseConnectionManager:
    """
    A Singleton class to manage the database connection pool.
    """
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialize()
            return cls._instance

    def _initialize(self):
        db_url = Config.DATABASE_URL
        if not db_url:
            raise Exception("Database URL not found in environment variables.")

        # Ensure SSL mode is enabled by adding sslmode=require
        if "sslmode" not in db_url:
            db_url += "?sslmode=require"
            
        # Initialize a connection pool
        self._pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,  # Adjust this based on your application needs
            dsn=db_url
        )
        if not self._pool:
            raise Exception("Failed to create the database connection pool.")

    def get_connection(self):
        """
        Get a connection from the pool.
        """
        try:
            return self._pool.getconn()
        except Exception as e:
            raise Exception(f"Error getting connection from the pool: {e}")

    def release_connection(self, connection):
        """
        Release a connection back to the pool.
        """
        try:
            self._pool.putconn(connection)
        except Exception as e:
            raise Exception(f"Error releasing connection back to the pool: {e}")

    def close_all_connections(self):
        """
        Close all connections in the pool.
        """
        try:
            self._pool.closeall()
        except Exception as e:
            raise Exception(f"Error closing all connections: {e}")
