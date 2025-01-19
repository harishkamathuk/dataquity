class TransactionSplit:
    def __init__(self, transaction_id, account_id, amount, asset_id=None):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.asset_id = asset_id

    def __repr__(self):
        return f"<TransactionSplit(transaction_id={self.transaction_id}, account_id={self.account_id}, amount={self.amount}, asset_id={self.asset_id})>"

    def validate(self):
        if not self.transaction_id or not self.account_id or self.amount <= 0:
            return False
        return True
