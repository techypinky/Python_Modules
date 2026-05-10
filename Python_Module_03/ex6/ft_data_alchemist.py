import random
print("=== Game Data Alchemist ===")

players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']

print(f"Initial list of players: {players}")

capitalized = [p.capitalize() for p in players]
print(f"New list with all names capitalized: {capitalized}")

only_cap = [p for p in players if p == p.capitalize()]
print(f"New list of capitalized names only: {only_cap}")

scores = {p: random.randint(0, 1000) for p in capitalized}
print(f"Score dict: {scores}")

avg = sum(scores.values()) / len(scores)
print(f"Score average is {round(avg, 2)}")

high_scores = {k: v for k, v in scores.items() if v > avg}
print(f"High scores: {high_scores}")