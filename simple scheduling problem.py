import random, math

# ---- Problem Setup ----
tasks = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
time_slots = [0, 1, 2]  # 3 available slots

# Random initial schedule (assign each task to a random slot)
def random_schedule():
    return [random.choice(time_slots) for _ in tasks]

# ---- Cost Function ----
# Penalize overcrowded slots (more than 2 tasks per slot)
def cost(schedule):
    slot_counts = {slot: schedule.count(slot) for slot in time_slots}
    penalty = sum(max(0, count - 2) ** 2 for count in slot_counts.values())
    return penalty

# ---- Generate Neighbor ----
def neighbor(schedule):
    new_schedule = schedule.copy()
    i = random.randrange(len(schedule))
    new_schedule[i] = random.choice(time_slots)
    return new_schedule

# ---- Simulated Annealing ----
def simulated_annealing(initial_temp=100, cooling_rate=0.95, min_temp=1):
    current = random_schedule()
    current_cost = cost(current)
    best = current
    best_cost = current_cost
    T = initial_temp

    while T > min_temp:
        new = neighbor(current)
        new_cost = cost(new)
        delta = new_cost - current_cost

        # Accept better or probabilistically accept worse solutions
        if delta < 0 or random.random() < math.exp(-delta / T):
            current, current_cost = new, new_cost

        # Update best found
        if current_cost < best_cost:
            best, best_cost = current, current_cost

        # Cool down
        T *= cooling_rate

    return best, best_cost

# ---- Run Algorithm ----
best_schedule, best_cost = simulated_annealing()

# ---- Display Results ----
print("Tasks:", tasks)
for i, slot in enumerate(best_schedule):
    print(f"{tasks[i]} → Slot {slot}")

print("Best Cost:", best_cost)
