# Goal: A retail website logs shopping cart activities. A user can ADD an item to their cart or REMOVE it. You want to audit what items are still sitting in carts at 18:00:00 (6 PM) so you can send an abandonment email. log file: ecommercecartlogs.txt

with open("ecommercecartlogs.txt", "r") as file:
    lines = file.read().splitlines()

cart_items = set()

for line in lines:
    line = line.split()

    user_name = line[2]
    time_cart = line[0]
    status    = line[1]
    item      = line[3]

    if time_cart > "18:00:00":
        continue

    cart_entry = f"{user_name}: {item}"
    
    if status == "ADD":
       cart_items.add(cart_entry)
    elif status == "REMOVE":
        cart_items.discard(cart_entry)

print(cart_items)