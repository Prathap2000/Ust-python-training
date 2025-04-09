class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        """Returns the current balance with a message in INR."""
        return f"Your balance is ₹{self._balance}"

    @classmethod
    def from_dict(cls, account_data):
        """Creates a BankAccount instance from a dictionary."""
        if not isinstance(account_data, dict):
            raise TypeError("Account data must be a dictionary.")
        if "name" not in account_data or "balance" not in account_data:
            raise ValueError("Dictionary must contain 'name' and 'balance' keys.")
        name = account_data["name"]
        balance = account_data["balance"]
        if not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number.")
        return cls(name, balance)

    @staticmethod
    def is_valid_withdrawal(amount, current_balance):
        """Checks if a given withdrawal amount is valid."""
        return isinstance(amount, (int, float)) and amount > 0 and amount <= current_balance

    def deposit(self, amount):
        """Deposits a positive amount into the account."""
        if isinstance(amount, (int, float)) and amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        """Withdraws a valid amount from the account."""
        if BankAccount.is_valid_withdrawal(amount, self._balance):
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Invalid withdrawal amount.")

# Example usage:
if __name__ == "__main__":
    # Create a BankAccount instance
    account1 = BankAccount("Bob", 5000)
    print(account1.balance)

    # Create a BankAccount from a dictionary
    account_data = {"name": "Alice", "balance": 10000}
    account2 = BankAccount.from_dict(account_data)
    print(f"Account holder: {account2.name}")
    print(account2.balance)

    # Perform transactions
    account1.deposit(2000)
    print(account1.balance)
    account1.withdraw(3000)
    print(account1.balance)
    account1.withdraw(5000)  # Invalid withdrawal
    print(account1.balance)

    # Check if a withdrawal is valid
    print(f"Is withdrawing ₹1000 from account2 valid? {BankAccount.is_valid_withdrawal(1000, account2._balance)}")
    print(f"Is withdrawing ₹15000 from account2 valid? {BankAccount.is_valid_withdrawal(15000, account2._balance)}")
    print(f"Is withdrawing ₹-500 from account1 valid? {BankAccount.is_valid_withdrawal(-500, account1._balance)}")
    # Trying to create an account from an invalid dictionary
    invalid_data1 = {"name": "Charlie"}
    try:
        account3 = BankAccount.from_dict(invalid_data1)
    except ValueError as e:
        print(f"Error creating account: {e}")

    invalid_data2 = {"name": "David", "balance": "invalid"}
    try:
        account4 = BankAccount.from_dict(invalid_data2)
    except TypeError as e:
        print(f"Error creating account: {e}")