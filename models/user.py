class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.accounts = []

    def __repr__(self):
        return f"<User(user_id={self.user_id}, name={self.name}, role={self.role})>"

    def add_account(self, account):
        self.accounts.append(account)
