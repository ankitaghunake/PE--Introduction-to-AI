# 🔹 Propositional Logic Example in AI
# Example: If it is raining → then ground is wet.

def implies(p, q):
    return (not p) or q   # logical implication

# propositions
raining = True
ground_wet = True

result = implies(raining, ground_wet)

print("💡 Propositional Logic Example")
print(f"It is raining: {raining}")
print(f"Ground is wet: {ground_wet}")
print(f"Statement (If raining → ground wet): {result}")
