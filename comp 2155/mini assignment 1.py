class BankAccount:
    def __init__(self, owner: str, balance: float):
        """
        Constructor for BankAccount class.

        Args:
            owner (str): The name of the account holder. Must be at least 10 characters.
            balance (float): The initial balance of the account. Must be a non-negative number.

        Raises:
            ValueError: If owner is less than 10 characters or balance is negative.
        """
        if len(owner) < 10:
            raise ValueError("Owner name must be at least 10 characters")
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def __str__(self) -> str:
        """
        Returns a string representation of the BankAccount object.

        Returns:
            str: A string stating the owner and balance.
        """
        return f"Account Owner: {self.owner}, Balance: ${self.balance:.2f}"

    def deposit(self, amount: float) -> None:
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be at least 1 dollar.

        Raises:
            ValueError: If amount is less than 1 dollar.
        """
        if amount < 1:
            print("Warning: Deposit amount must be at least $1")
            return
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws the specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If there are insufficient funds.
        """
        if amount > self.balance:
            print("Warning: Insufficient funds")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount:.2f}")

    def display_balance(self) -> None:
        """
        Prints the current balance.
        """
        print(f"Current Balance: ${self.balance:.2f}")

    def display_transactions(self) -> None:
        """
        Prints all transactions for the account.
        """
        for i, transaction in enumerate(self.transactions, start=1):
            print(f"{i}. {transaction}")