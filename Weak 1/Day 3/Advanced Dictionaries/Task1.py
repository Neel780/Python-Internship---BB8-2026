products = {"Mouse": 25, "Keyboard": 120, "Monitor": 300, "Cable": 15, "Desk": 250}

expensive_products = {k: v for k, v in products.items() if v > 100}
print("Expensive products:", expensive_products)