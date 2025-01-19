class Account:
    def __init__(self, account_id, account_type, balance):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def __repr__(self):
        return f"<Account(account_id={self.account_id}, account_type={self.account_type}, balance={self.balance})>"

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
