class Inventory:
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

inv = Inventory(["Sword", "Shield", "Potion", "Map"])
print("Total items:", len(inv))
print("First item:", inv[0])
print("Third item:", inv[2])