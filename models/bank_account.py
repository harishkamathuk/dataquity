from .account import Account

class BankAccount(Account):
    def __init__(self, account_id, balance):
        super().__init__(account_id, "Bank", balance)
        self.transactions = []

    def __repr__(self):
        return f"<BankAccount(account_id={self.account_id}, balance={self.balance})>"

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
