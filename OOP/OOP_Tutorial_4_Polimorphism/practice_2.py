class Account:
    # Constructor to initialize account number and balance
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    # Method to credit (deposit) money
    def credit(self, amount):
        self.balance += amount
        print(f"₹{amount} credited successfully!")
        self.print_balance()

    # Method to debit (withdraw) money
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Transaction failed.")
        else:
            self.balance -= amount
            print(f"₹{amount} debited successfully!")
        self.print_balance()

    # Method to print current balance
    def print_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")
        print("-" * 30)


# Example usage
acc1 = Account(123456789, 50000)

acc1.print_balance()     # Show initial balance
acc1.credit(10000)       # Deposit ₹10,000
acc1.debit(20000)        # Withdraw ₹20,000
acc1.debit(60000)        # Try to withdraw more than balance
