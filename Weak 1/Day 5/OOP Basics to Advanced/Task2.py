class Counter:
    total_count = 0

    def __init__(self):
        Counter.total_count += 1

    @classmethod
    def get_total_count(cls):
        return cls.total_count

for _ in range(5):
    Counter()

print("Total Counter objects created:", Counter.get_total_count())