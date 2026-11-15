product = ("Laptop", 1200.00, 10)

try:
    product[1] = 1100.00
except TypeError as e:
    print(f"Error observed: {e}")

updated_product = (product[0], 1100.00, product[2])
print("Updated Product:", updated_product)