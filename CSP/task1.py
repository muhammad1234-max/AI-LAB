from ortools.sat.python import cp_model

# Define product properties
products = {
    0: {'frequency': 15, 'volume': 2},
    1: {'frequency': 8, 'volume': 1},
    2: {'frequency': 20, 'volume': 3},
}

# Define slot properties
slots = {
    0: {'distance': 1, 'capacity': 3},
    1: {'distance': 2, 'capacity': 3},
    2: {'distance': 3, 'capacity': 3},
}

num_products = len(products)
num_slots = len(slots)

# Create the CP model
model = cp_model.CpModel()

# Create assignment variables: assign[p][s] = 1 if product p is assigned to slot s
assign = {}
for p in range(num_products):
    for s in range(num_slots):
        assign[(p, s)] = model.NewBoolVar(f'assign_p{p}_s{s}')

# Constraint 1: Each product is assigned to exactly one slot
for p in range(num_products):
    model.Add(sum(assign[(p, s)] for s in range(num_slots)) == 1)

# Constraint 2: Total volume in each slot must not exceed its capacity
for s in range(num_slots):
    model.Add(
        sum(assign[(p, s)] * products[p]['volume'] for p in range(num_products)) <= slots[s]['capacity']
    )

# Objective: Minimize total weighted walking distance
# Total cost = sum (frequency of product * distance of assigned slot)
model.Minimize(
    sum(assign[(p, s)] * products[p]['frequency'] * slots[s]['distance']
        for p in range(num_products)
        for s in range(num_slots))
)

# Solve the model
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Output result
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("📦 Product-to-Slot Assignments:")
    for p in range(num_products):
        for s in range(num_slots):
            if solver.Value(assign[(p, s)]) == 1:
                print(f"Product {p+1} → Slot {s+1}")
    print(f"\n🚶 Total Walking Cost: {solver.ObjectiveValue()}")
else:
    print("No feasible assignment found.")
