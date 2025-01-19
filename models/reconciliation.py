class Reconciliation:
    def __init__(self, reconciliation_id, date, status):
        self.reconciliation_id = reconciliation_id
        self.date = date
        self.status = status
        self.transactions = []

    def __repr__(self):
        return f"<Reconciliation(reconciliation_id={self.reconciliation_id}, date={self.date}, status={self.status})>"

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
