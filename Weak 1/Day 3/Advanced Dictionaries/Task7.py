inventory = {"Laptop": 10, "Mouse": 50}

inventory["Keyboard"] = 20

inventory["Laptop"] -= 1

item_to_sell = "Webcam"
if inventory.get(item_to_sell, 0) > 0:
    inventory[item_to_sell] -= 1
else:
    print(f"Error: '{item_to_sell}' is out of stock or does not exist.")

print("Current Inventory:", inventory)