from collections import deque

def water_jug_problem():
    # capacities
    jug4, jug3 = 4, 3  
    visited = set()  
    queue = deque([(0, 0)])  # initial state (0,0)

    while queue:
        a, b = queue.popleft()
        print(f"({a}, {b})")  # print each step

        # check goal condition
        if a == 2:
            print("\nGoal reached: 2 gallons in 4-gallon jug.")
            return

        if (a, b) in visited:
            continue
        visited.add((a, b))

        # possible actions
        next_states = [
            (jug4, b),              # fill 4-gallon jug
            (a, jug3),              # fill 3-gallon jug
            (0, b),                 # empty 4-gallon jug
            (a, 0),                 # empty 3-gallon jug
            (a - min(a, jug3 - b), b + min(a, jug3 - b)),  # pour 4 -> 3
            (a + min(b, jug4 - a), b - min(b, jug4 - a))   # pour 3 -> 4
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

# Run the program
water_jug_problem()
