class Commodity:
    def __init__(self, commodity_id, name, symbol):
        self.commodity_id = commodity_id
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return f"<Commodity(commodity_id={self.commodity_id}, name={self.name}, symbol={self.symbol})>"
