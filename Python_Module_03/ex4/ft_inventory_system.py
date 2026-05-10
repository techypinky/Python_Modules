import sys
print("=== Inventory System Analysis ===")

inventory = {}

for arg in sys.argv[1:]:
    parts = arg.split(":")

    if len(parts) != 2:
        print(f"Error - invalid parameter'{arg}'")
        continue

    key = parts[0]
    value_str = parts[1]

    try:
        value = int(value_str)
    except:
        print(f"Quantity error for'{key}': invalid literal for int() with base 10:'{value_str}'")
        continue

    if key in inventory:
        print(f"Redundant item '{key}' - discarding")
        continue

    inventory[key] = value

print(f"Got inventory: {inventory}")

items = list(inventory.keys())
print(f"Item list: {items}")

total = sum(inventory.values())
print(f"Total quantity of the {len(items)} items: {total}")

for key in inventory:
    percent = (inventory[key] / total) * 100
    print(f"Item {key} represents {round(percent, 1)}%")

max_item = None
max_val = -1

min_item = None
min_val = None

for key in inventory:
    val = inventory[key]

    if max_item is None or val > max_val:
        max_item = key
        max_val = val

    if min_item is None or val < min_val:
        min_item = key
        min_val = val

print(f"Item most abundant: {max_item} with quantity {max_val}")
print(f"Item least abundant: {min_item} with quantity {min_val}")

inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")