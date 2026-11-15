prices = [15, 42, 99, 120, 5, 200, 75, 30, 80, 150]
average_price = sum(prices) / len(prices)

high_prices = [p for p in prices if p > average_price]
print("Prices above average:", high_prices)