from .account import Account

class PortfolioAccount(Account):
    def __init__(self, account_id, balance):
        super().__init__(account_id, "Portfolio", balance)
        self.assets = []

    def __repr__(self):
        return f"<PortfolioAccount(account_id={self.account_id}, balance={self.balance})>"

    def add_asset(self, asset):
        self.assets.append(asset)
