import random

# Define number of queens
N = 8  # Change for different board sizes

# Fitness function: Counts non-attacking pairs of queens
def calculate_fitness(individual):
    non_attacking_pairs = 0
    total_pairs = (N * (N - 1)) // 2  # Maximum possible pairs

    # Check for conflicts
    attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                attacking_pairs += 1

    # Non-attacking pairs = total_pairs - attacking_pairs
    return total_pairs - attacking_pairs

# Generate a random individual (chromosome)
def create_random_individual():
    return [random.randint(0, N - 1) for _ in range(N)]

# Selection: Pick the best individuals from the population
def select_parents(population, k=3):
    return max(random.sample(population, k), key=lambda x: x[1])

# Crossover: Single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, N - 2)
    child = parent1[:point] + parent2[point:]
    return child

# Mutation: Swap two positions
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(N), 2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

# Genetic Algorithm function
def genetic_algorithm(pop_size=100, generations=1000, mutation_rate=0.1):
    population = [(create_random_individual(), 0) for _ in range(pop_size)]
    population = [(ind, calculate_fitness(ind)) for ind, _ in population]

    for generation in range(generations):
        population.sort(key=lambda x: x[1], reverse=True)

        if population[0][1] == (N * (N - 1)) // 2:
            print(f"Solution found in generation {generation}")
            return population[0][0]

        new_population = []
        for _ in range(pop_size // 2):
            parent1 = select_parents(population)[0]
            parent2 = select_parents(population)[0]
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.extend([(mutate(child1, mutation_rate), 0), (mutate(child2, mutation_rate), 0)])

        population = [(ind, calculate_fitness(ind)) for ind, _ in new_population]

    print("No perfect solution found within the given generations.")
    return None

# Run the Genetic Algorithm for N-Queens
solution = genetic_algorithm()
print("\nSolution (Row positions for queens):", solution)
