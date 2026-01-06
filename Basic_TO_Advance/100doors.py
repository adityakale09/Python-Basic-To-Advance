# ==========📘 Problem Statement (100 door puzzle Question)===========

# There are 100 doors, all initially closed.
# There are also 100 keys, numbered from 1 to 100.

# You perform the following operation:
# Key 1 toggles (opens if closed, closes if open) every door.
# Key 2 toggles every 2nd door.
# Key 3 toggles every 3rd door.
# …
# Key k toggles all doors whose numbers are multiples of k.
# This continues until Key 100, which toggles only door 100.

# ❓ Question:
# After all 100 keys have been used exactly once, which doors remain open?

# ---------------------------Answer-----------------------------------

# Number of doors
n = 100

# Step 1: All doors are initially CLOSED (False = Closed, True = Open)
doors = [False] * n

# Step 2: Apply keys 1 to 100
for key in range(1, n + 1):
    for door in range(key - 1, n, key): #(this is for tables 1 ) (key is escape number)
        doors[door] = not doors[door]  # toggle door

# if not doors[door] : ##if no want to use doors[door] = not doors[door]
#     doors[door] = True
# else:
#     doors[door] = False

# Step 3: Find open doors
open_doors = []

for i in range(n):
    if doors[i]:
        open_doors.append(i + 1)

# Step 4: Print result
print("Open doors at the end:")
print(open_doors)
