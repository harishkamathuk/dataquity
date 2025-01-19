from models.user import User
from models.bank_account import BankAccount
from models.portfolio_account import PortfolioAccount
from models.asset import Asset
from models.transaction import Transaction
from models.transaction_split import TransactionSplit
from models.reconciliation import Reconciliation
from models.commodity import Commodity

# Creating some dummy data
user = User(user_id=1, name="John Doe", role="Investor")

bank_account = BankAccount(account_id=1, balance=5000)
portfolio_account = PortfolioAccount(account_id=2, balance=10000)

asset1 = Asset(asset_id=1, name="Stock XYZ", value=150)
asset2 = Asset(asset_id=2, name="Mutual Fund ABC", value=200)

# Add assets to portfolio account
portfolio_account.add_asset(asset1)
portfolio_account.add_asset(asset2)

# Create a transaction and split it
transaction = Transaction(transaction_id=1, amount=500, date="2025-01-20", account_id=1)
split1 = TransactionSplit(transaction_id=1, account_id=1, amount=250)
split2 = TransactionSplit(transaction_id=1, account_id=2, amount=250)

transaction.add_split(split1)
transaction.add_split(split2)

# Add a transaction to bank account
bank_account.add_transaction(transaction)

# Reconciliation
reconciliation = Reconciliation(reconciliation_id=1, date="2025-01-20", status="Pending")
reconciliation.add_transaction(transaction)

# Print data for verification
print(user)
print(bank_account)
print(portfolio_account)
print(asset1)
print(transaction)
print(reconciliation)
