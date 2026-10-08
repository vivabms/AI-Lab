loc = input("Location (A/B): ").upper()
state = {'A': int(input("A (0:Clean, 1:Dirty): ")), 'B': int(input("B (0:Clean, 1:Dirty): "))}
cost = 0

for i in range(2):
    print(f"Vacuum at {loc}. State: {state}")
    if state[loc] == 1:
        print(f"Cleaning {loc}...")
        state[loc] = 0
        cost += 1

# Output:

# Location (A/B): a
# A (0:Clean, 1:Dirty): 1
# B (0:Clean, 1:Dirty): 0
# Vacuum at A. State: {'A': 1, 'B': 0}
# Cleaning A...
# Vacuum at A. State: {'A': 0, 'B': 0}
