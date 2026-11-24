class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Cannot compare different currencies: {self.currency} and {other.currency}")
        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Cannot compare different currencies: {self.currency} and {other.currency}")
        return self.amount > other.amount

m1 = Money(100, "USD")
m2 = Money(250, "USD")
m3 = Money(100, "INR")

print("m1 < m2:", m1 < m2)
print("m1 > m2:", m1 > m2)

try:
    print(m1 < m3)
except ValueError as e:
    print("Error:", e)