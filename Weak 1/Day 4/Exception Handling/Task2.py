def get_item_safely(items, index):
    try:
        return items[index]
    except IndexError:
        return None

my_list = [10, 20, 30]
print(get_item_safely(my_list, 1))
print(get_item_safely(my_list, 5))