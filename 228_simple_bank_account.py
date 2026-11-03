class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposited: ₹{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount:.2f}")

    def show_balance(self):
        print(f"{self.owner}'s balance: ₹{self.balance:.2f}")

def main():
    name = input("Account holder name: ").strip() or "User"
    account = BankAccount(name)
    while True:
        print("\n1. Deposit  2. Withdraw  3. Check balance  4. Exit")
        choice = input("Choose an option: ").strip()
        if choice in ("1", "2"):
            try:
                amount = float(input("Enter amount: ₹"))
                (account.deposit if choice == "1" else account.withdraw)(amount)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "3":
            account.show_balance()
        elif choice == "4":
            print("Thank you for trying the demo account.")
            break
        else:
            print("Invalid option. Choose 1–4.")

if __name__ == "__main__":
    main()
