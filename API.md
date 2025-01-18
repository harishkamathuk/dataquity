# API Documentation for DataQuity

## Overview
The **DataQuity** API provides access to stock market data, including fetching the latest stock market information and retrieving data for specific stock symbols. The API is designed to be simple and easy to use, allowing users to programmatically interact with stock data.

---

## Base URL
```
http://localhost:8000/api
```

---

## Endpoints

### 1. **GET /stock-data**
Fetches the latest stock market data in JSON format.

**Request:**
- Method: `GET`
- Endpoint: `/stock-data`

**Response:**
- Status: `200 OK`
- Body:
```json
{
  "message": "Latest stock data retrieved successfully.",
  "data": [
    {
      "symbol": "AAPL",
      "price": 150.25,
      "timestamp": "2025-01-18T00:00:00Z"
    },
    {
      "symbol": "GOOG",
      "price": 2735.50,
      "timestamp": "2025-01-18T00:00:00Z"
    }
  ]
}
```

### 2. **GET /stock-data/{symbol}**
Retrieves stock data for a specific symbol.

**Request:**
- Method: `GET`
- Endpoint: `/stock-data/{symbol}`
  - Replace `{symbol}` with the desired stock symbol (e.g., `AAPL`, `GOOG`).

**Response:**
- Status: `200 OK`
- Body:
```json
{
  "symbol": "AAPL",
  "price": 150.25,
  "timestamp": "2025-01-18T00:00:00Z"
}
```

---

## Authentication
No authentication is required to use the API.

---

## Error Handling
The API will respond with appropriate HTTP status codes and error messages.

**Example:**
- **Error 404**: Stock symbol not found.
```json
{
  "error": "Stock symbol not found"
}
```

---

## Usage Example

1. **Fetch all stock data:**
```bash
curl http://localhost:8000/api/stock-data
```

2. **Fetch stock data for a specific symbol (e.g., AAPL):**
```bash
curl http://localhost:8000/api/stock-data/AAPL
```

---

## Contribution Guidelines
- Fork the repository.
- Create a new branch for your changes.
- Submit a pull request with a clear description of the changes.

---

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for more details.

---

For any questions or support, please contact us via GitHub issues or email.

```
