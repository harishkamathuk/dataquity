# tests/test_api.py
import pytest
from api.app import app

@pytest.fixture
def client():
    """Fixture to provide a test client for Flask app."""
    with app.test_client() as client:
        yield client

def test_get_stock_data(client):
    """Test the GET /api/stocks/<symbol> endpoint."""
    symbol = "AAPL"
    response = client.get(f"/api/stocks/{symbol}")
    
    # Check the response status code and JSON content
    assert response.status_code == 200
    data = response.get_json()
    assert "symbol" in data
    assert data["symbol"] == symbol
    assert "price" in data
    assert "volume" in data
    assert "market_cap" in data

def test_trigger_etl(client):
    """Test the POST /api/stocks/<symbol>/etl endpoint."""
    symbol = "AAPL"
    response = client.post(f"/api/stocks/{symbol}/etl")
    
    # Check if the response status code indicates success
    assert response.status_code == 200
    assert "message" in response.get_json()

# def test_get_status(client):
#     """Test the GET /api/status endpoint."""
#     response = client.get("/api/status")
    
#     # Check the response status code and content
#     assert response.status_code == 200
#     data = response.get_json()
#     assert "status" in data
#     assert data["status"] == "ETL process completed successfully."
