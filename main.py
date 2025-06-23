# Step 1
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

# Step 2
def add_item(name, quantity, price):
    if name in inventory:
        print(f"{name} already exists. Use update to change values.")
    else:
        inventory[name] = (quantity, price)
        print(f"Added {name}.")

def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Removed {name}.")
    else:
        print(f"{name} not found in inventory.")

def update_item(name, quantity=None, price=None):
    if name in inventory:
        current_quantity, current_price = inventory[name]
        new_quantity = quantity if quantity is not None else current_quantity
        new_price = price if price is not None else current_price
        inventory[name] = (new_quantity, new_price)
        print(f"Updated {name}.")
    else:
        print(f"{name} not found in inventory.")

# Step 3
def display_inventory():
    print("\nCurrent inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

# Step 4
def total_value():
    value = sum(quantity * price for quantity, price in inventory.values())
    print(f"\nTotal value of inventory: ${value:.2f}")

# Example Run
print("Welcome to the Inventory Manager!")
display_inventory()
print("\nAdding a new item: mango")
add_item("mango", 15, 3.0)
display_inventory()
total_value()
