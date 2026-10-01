# 124_python_mini_bank_transactions.py
# Mini Bank Transaction System - 10 practical features

account = {
    "name": "Prashant",
    "account_no": "XXXX101",
    "balance": 25000
}

transactions = [
    {"type": "Deposit", "amount": 5000},
    {"type": "Withdraw", "amount": 2000},
    {"type": "Deposit", "amount": 3000},
    {"type": "Withdraw", "amount": 1000},
]

print("1. Account:", account)
print("2. Transaction count:", len(transactions))

deposits = sum(t["amount"] for t in transactions if t["type"] == "Deposit")
print("3. Total deposits:", deposits)

withdrawals = sum(t["amount"] for t in transactions if t["type"] == "Withdraw")
print("4. Total withdrawals:", withdrawals)

print("5. Net transaction:", deposits - withdrawals)

amount = 4000
account["balance"] += amount
transactions.append({"type": "Deposit", "amount": amount})
print("6. After deposit:", account["balance"])

amount = 1500
if amount <= account["balance"]:
    account["balance"] -= amount
    transactions.append({"type": "Withdraw", "amount": amount})
print("7. After withdrawal:", account["balance"])

print("8. Recent transactions:", transactions[-3:])

largest = max(transactions, key=lambda t: t["amount"])
print("9. Largest transaction:", largest)

print("10. Summary:", {
    "holder": account["name"],
    "transactions": len(transactions),
    "balance": account["balance"]
})
