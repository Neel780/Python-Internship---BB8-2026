subscribers = {"user1@mail.com", "user2@mail.com", "user3@mail.com"}
customers = {"user2@mail.com", "user4@mail.com"}

never_purchased = subscribers - customers
never_subscribed = customers - subscribers

print("Subscribed but never purchased:", never_purchased)
print("Purchased but never subscribed:", never_subscribed)