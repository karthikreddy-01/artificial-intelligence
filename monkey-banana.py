def monkey_banana():
    # Initial state
    monkey = "floor"
    box = "corner"
    bananas = "ceiling"
    has_bananas = False

    print("Initial State: Monkey on the floor, Box in the corner, Bananas hanging from ceiling.")

    # Step 1: Monkey moves the box under the bananas
    box = "under bananas"
    print("Monkey moves the box under the bananas.")

    # Step 2: Monkey climbs on the box
    monkey = "on box"
    print("Monkey climbs on the box.")

    # Step 3: Monkey takes the bananas
    has_bananas = True
    print("Monkey grabs the bananas!")

    # Final state
    if has_bananas:
        print("Goal achieved: Monkey has the bananas 🐒🍌")
    else:
        print("Goal not achieved.")

# Run the function
monkey_banana()


