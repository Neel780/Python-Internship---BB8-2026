class Account:
    def get_interest_rate(self):
        return 4

class SavingsAccount(Account):
    def get_interest_rate(self):
        return 5.5

class FixedDeposit(Account):
    def get_interest_rate(self):
        return 7.5

accounts = [Account(), SavingsAccount(), FixedDeposit()]

for acc in accounts:
    print(f"{acc.__class__.__name__} Interest Rate: {acc.get_interest_rate()}%")