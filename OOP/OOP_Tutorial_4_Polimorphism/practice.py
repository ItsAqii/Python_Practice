class Account:
    # Constructor to initialize account number and balance
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    # Method to display account details
    def display(self):
        print(f"Account Number: {self.account_no}")
        print(f"Account Balance: ₹{self.balance:.2f}")


# Example usage
acc1 = Account(123456789, 50000)
acc1.display()
