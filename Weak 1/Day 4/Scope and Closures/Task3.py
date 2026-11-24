def make_counter(start):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter_a = make_counter(0)
counter_b = make_counter(100)

print("Counter A:", counter_a())
print("Counter A:", counter_a())
print("Counter A:", counter_a())

print("Counter B:", counter_b())
print("Counter B:", counter_b())