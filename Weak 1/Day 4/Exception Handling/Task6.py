def process_order(order):
    try:
        item = order["item"]
        price = order["price"]
    except KeyError as e:
        print(f"Error: Missing required key {e} in order.")
    else:
        print(f"Order Details -> Item: {item}, Price: {price}")
    finally:
        print("Processing complete")

process_order({"item": "Laptop", "price": 55000})
process_order({"item": "Mouse"})