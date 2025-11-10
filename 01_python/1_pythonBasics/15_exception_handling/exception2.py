class InsufficientFunds(Exception):
    pass


balance = 0


def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError("Amount must be positive")
    balance += amount


deposit(10)
deposit(7)
# deposit(-4)
print(balance)


def withdraw(amount):
    global balance
    if amount > balance:
        raise InsufficientFunds(f"Now enough funds. Current balance {balance}")
    balance -= amount


withdraw(50)
print(balance)
