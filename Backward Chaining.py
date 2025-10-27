# Backward Chaining in Python

# Knowledge Base: (premises => conclusion)
knowledge_base = [
    (["mammal(A)"], "vertebrate(A)"),
    (["vertebrate(A)"], "animal(A)"),
    (["vertebrate(A)", "flying(A)"], "bird(A)"),
    ([], 'vertebrate("duck")'),
    ([], 'flying("duck")'),
    ([], 'mammal("cat")')
]

# Function for variable substitution (A -> constant)
def substitute(expr, var, const):
    return expr.replace(var, const)

# Backward chaining function
def backward_chaining(goal, kb):
    print(f"Trying to prove: {goal}")

    # If goal is already known as a fact
    for premises, conclusion in kb:
        if premises == [] and conclusion == goal:
            print(f"✔ {goal} is a known fact.")
            return True

    # Try to find rules that conclude this goal
    for premises, conclusion in kb:
        if "(A)" in conclusion:
            const = goal[goal.find("(")+1 : goal.find(")")]
            rule_conclusion = substitute(conclusion, "A", const)

            if rule_conclusion == goal:
                print(f"To prove {goal}, need to prove {premises}")
                all_true = True
                for p in premises:
                    sub_goal = substitute(p, "A", const)
                    if not backward_chaining(sub_goal, kb):
                        all_true = False
                        break
                if all_true:
                    print(f"✔ {goal} proven through rule: {premises} => {conclusion}")
                    return True

    print(f"✖ Cannot prove {goal}")
    return False


# --- Main Program ---
goal = 'bird("duck")'

print("\n=== Backward Chaining Proof ===")
if backward_chaining(goal, knowledge_base):
    print(f"\n✅ Goal {goal} can be derived from the knowledge base.")
else:
    print(f"\n❌ Goal {goal} cannot be derived from the knowledge base.")
