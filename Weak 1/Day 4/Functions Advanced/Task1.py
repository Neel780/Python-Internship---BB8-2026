def build_invoice(customer_name, *args, **kwargs):
    total = sum(args)
    print(f"Customer: {customer_name}")
    print(f"Total Price: {total}")
    print("Extra Details:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

build_invoice("Alice", 150, 250, 100, discount="10%", tax="5%")