def transform_stock_data(stock_data):
    """
    Transforms the raw stock data into a structured format suitable for database insertion.
    """
    transformed_data = {
        'name': stock_data.get('name', 'Unknown Company'),
        'price': stock_data.get('price', 0),
        'volume': stock_data.get('volume', 0),
        'market_cap': stock_data.get('market_cap', 0),
        'last_trade_time': stock_data.get('last_trade_time', '1970-01-01T00:00:00.000000'),
    }
    if transformed_data['market_cap'] is None:
        transformed_data['market_cap'] = 0
    return transformed_data