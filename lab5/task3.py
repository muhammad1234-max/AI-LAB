import random
import math

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to calculate total distance of a given route
def total_distance(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1)) + distance(route[-1], route[0])  # Returning to start

# Generate a random initial population of routes
def create_population(cities, population_size):
    return [random.sample(cities, len(cities)) for _ in range(population_size)]

# Selection: Tournament Selection (Select the best among random individuals)
def select_parents(population, k=3):
    return min(random.sample(population, k), key=total_distance)

# Crossover: Order Crossover (OX) to preserve partial order
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    
    child = [None] * size
    child[start:end] = parent1[start:end]

    # Fill remaining positions from parent2 in order
    p2_index = 0
    for i in range(size):
        if child[i] is None:
            while parent2[p2_index] in child:
                p2_index += 1
            child[i] = parent2[p2_index]
    
    return child

# Mutation: Swap two cities with a small probability
def mutate(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route

# Genetic Algorithm Function
def genetic_algorithm(cities, population_size=100, generations=500, mutation_rate=0.1):
    population = create_population(cities, population_size)
    
    for _ in range(generations):
        new_population = []
        
        # Selection & Reproduction
        for _ in range(population_size // 2):
            parent1 = select_parents(population)
            parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
        
        population = new_population
    
    # Return the best route found
    best_route = min(population, key=total_distance)
    return best_route, total_distance(best_route)

# Example cities (random coordinates for 10 cities)
cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]

# Run Genetic Algorithm for TSP
best_route, best_distance = genetic_algorithm(cities)

# Print results
print("Optimized Route:", best_route)
print("Total Distance:", round(best_distance, 2))
