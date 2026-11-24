class Wallet:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

wallet = Wallet(100)
wallet.deposit(50)
wallet.withdraw(30)
wallet.withdraw(-10)
print("Current Balance:", wallet.balance)