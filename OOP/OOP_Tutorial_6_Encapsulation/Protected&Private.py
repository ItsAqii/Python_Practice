# Example:
#  This example demonstrates how a protected method (_show_balance)
#  and a private method (__update_balance) are used to control access. 
# The private method updates balance internally, while protected method displays it. 
# Both are accessed via a public method (deposit), 
# showing how Python uses naming conventions for encapsulation.

class BankAccount:
    def __init__(self):
        self.balance = 1000  # Public attribute

    def _Show_Balance(self):  # Protected method
        print(f"Current Balance: ${self.balance}")

    def __Update_Balance(self, amount):  # Private method
        self.balance += amount

    def deposit(self, amount):  # Public method
        if amount > 0:
            self.__Update_Balance(amount)  # Accessing private method
            self._Show_Balance()  # Accessing protected method
        else:
            print("Deposit amount must be positive.")

account = BankAccount() # Create an instance of BankAccount
account._Show_Balance() # Accessing protected method
account.deposit(500) # Using public method to deposit money
account._Show_Balance() # Accessing protected method again to show updated balance

