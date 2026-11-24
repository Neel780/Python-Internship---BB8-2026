def require_positive(func):
    def wrapper(*args, **kwargs):
        if any(arg <= 0 for arg in args):
            print("Error: All arguments must be positive numbers.")
            return None
        return func(*args, **kwargs)
    return wrapper

@require_positive
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, -2))
print(divide(0, 5))