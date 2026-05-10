import random

achievements = [
    "First Steps", "Speed Runner", "Master Explorer", "Treasure Hunter",
    "Survivor", "Boss Slayer", "Crafting Genius", "Strategist",
    "World Savior", "Collector Supreme", "Untouchable",
    "Sharp Mind", "Unstoppable", "Hidden Path Finder"
]


def gen_player_achievements():
    player_set = set()

    for ach in achievements:
        if random.random() > 0.5:
            player_set.add(ach)
            
    if len(player_set) == 0:
        player_set.add(achievements[0])

    return player_set


print("=== Achievement Tracker System ===")

alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print(f"Player Alice: {alice}")
print(f"Player Bob: {bob}")
print(f"Player Charlie: {charlie}")
print(f"Player Dylan: {dylan}")

all_achievements = set.union(alice, bob, charlie, dylan)
print(f"All distinct achievements: {all_achievements}")

common = set.intersection(alice, bob, charlie, dylan)
print(f"Common achievements: {common}")

print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")

print(f"Alice is missing: {all_achievements.difference(alice)}")
print(f"Bob is missing: {all_achievements.difference(bob)}")
print(f"Charlie is missing: {all_achievements.difference(charlie)}")
print(f"Dylan is missing: {all_achievements.difference(dylan)}")