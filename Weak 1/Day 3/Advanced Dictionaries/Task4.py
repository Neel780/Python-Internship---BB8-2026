words = ["apple", "ant", "banana", "bat", "cat", "carrot"]
grouped_words = {}

for word in words:
    grouped_words.setdefault(word[0], []).append(word)

print("Grouped words:", grouped_words)