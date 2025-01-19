class Asset:
    def __init__(self, asset_id, name, value):
        self.asset_id = asset_id
        self.name = name
        self.value = value

    def __repr__(self):
        return f"<Asset(asset_id={self.asset_id}, name={self.name}, value={self.value})>"
