# Custom exception class - inherits from built-in Exception
# Used to handle insufficient balance scenarios
class InsufficientFunds(Exception):
    pass  # No additional functionality - just a named exception type

# Global variable to track account balance
balance = 0

# Function to add money to account
def deposit(amount):
    global balance  # Declare we're modifying the global balance variable
    
    # Validation - amount must be positive
    if amount <= 0:
        raise ValueError("Amount must be positive")  # Raise built-in ValueError
    
    balance += amount  # Add amount to current balance

# Function to withdraw money from account
def withdraw(amount):
    global balance  # Declare we're modifying the global balance variable
    
    # Check if sufficient funds exist
    if amount > balance:
        # Raise custom exception with formatted error message
        raise InsufficientFunds(f"Not enough funds. Current balance {balance}")
    
    balance -= amount  # Subtract amount from current balance

# Transaction sequence:
deposit(10)   # balance = 0 + 10 = 10 ✅
deposit(7)    # balance = 10 + 7 = 17 ✅
withdraw(50)  # balance = 17, trying to withdraw 50 ❌ RAISES InsufficientFunds
print(balance)  # This line NEVER executes because exception crashes the program