usernames = ["ali", "rohan_99", "dev", "priya_sharma", "sam", "alex123"]
valid_usernames = list(filter(lambda name: len(name) >= 6, usernames))
print(valid_usernames)