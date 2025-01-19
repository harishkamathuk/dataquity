class Strategy:
    def __init__(self, strategy_id, name, description):
        self.strategy_id = strategy_id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Strategy(strategy_id={self.strategy_id}, name={self.name}, description={self.description})>"
