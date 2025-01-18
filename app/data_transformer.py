def transform_stock_data(stock_data):
    """
    Transforms the raw stock data into a structured format suitable for database insertion,
    including derived fields for percentage change, daily price range, and 52-week price range.
    """
    transformed_data = {
        'name': stock_data.get('name', 'Unknown Company'),
        'price': stock_data.get('price', 0),
        'volume': stock_data.get('volume', 0),
        'market_cap': stock_data.get('market_cap', 0),
        'last_trade_time': stock_data.get('last_trade_time', '1970-01-01T00:00:00.000000'),
    }

    # Calculate derived fields
    percentage_change = (
        (stock_data["price"] - stock_data["previous_close_price"]) / stock_data["previous_close_price"] * 100
        if stock_data.get("previous_close_price") else None
    )
    daily_price_range = (
        stock_data["day_high"] - stock_data["day_low"]
        if stock_data.get("day_high") and stock_data.get("day_low") else None
    )
    fiftytwo_week_range = (
        stock_data["52_week_high"] - stock_data["52_week_low"]
        if stock_data.get("52_week_high") and stock_data.get("52_week_low") else None
    )

    # Include derived fields in the transformed data
    transformed_data.update({
        'percentage_change': percentage_change,
        'daily_price_range': daily_price_range,
        'fiftytwo_week_range': fiftytwo_week_range,
    })

    # Handle cases where market cap is None
    if transformed_data['market_cap'] is None:
        transformed_data['market_cap'] = 0

    return transformed_data
