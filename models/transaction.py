class Transaction:
    def __init__(self, transaction_id, amount, date, account_id):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.account_id = account_id
        self.splits = []

    def __repr__(self):
        return f"<Transaction(transaction_id={self.transaction_id}, amount={self.amount}, date={self.date}, account_id={self.account_id})>"

    def add_split(self, split):
        self.splits.append(split)
