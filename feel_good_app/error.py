import random

feel = input("Enter: ")

with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
    quotes = file.readlines()
    # self.ids.quote.text = random.choice(quotes)
    print(random.choice(quotes))