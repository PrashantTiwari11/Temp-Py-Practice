# 100_python_mini_bank_system.py
# Mini Banking System - 10 practical features

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(("Deposit", amount))
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("Withdraw", amount))
            return True
        return False

    def check_balance(self):
        return self.balance

    def transaction_count(self):
        return len(self.transactions)

    def show_transactions(self):
        return self.transactions

    def total_deposits(self):
        return sum(amount for kind, amount in self.transactions if kind == "Deposit")

    def total_withdrawals(self):
        return sum(amount for kind, amount in self.transactions if kind == "Withdraw")

    def summary(self):
        return {
            "owner": self.owner,
            "balance": self.balance,
            "transactions": self.transaction_count()
        }

    def can_withdraw(self, amount):
        return 0 < amount <= self.balance

    def close(self):
        self.balance = 0
        self.transactions.append(("Account Closed", 0))


account = BankAccount("Prashant", 5000)
account.deposit(1500)
account.withdraw(800)

print("1. Owner:", account.owner)
print("2. Balance:", account.check_balance())
print("3. Deposit total:", account.total_deposits())
print("4. Withdrawal total:", account.total_withdrawals())
print("5. Can withdraw 2000:", account.can_withdraw(2000))
print("6. Transaction count:", account.transaction_count())
print("7. Transactions:", account.show_transactions())
print("8. Summary:", account.summary())
print("9. Can withdraw 10000:", account.can_withdraw(10000))

account.close()
print("10. After close:", account.summary())
