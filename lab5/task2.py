import random
import math

# Function to calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Function to calculate total distance of a given route
def total_distance(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1)) + distance(route[-1], route[0])  # Returning to start

# Function to generate a neighboring solution by swapping two locations
def get_neighbor(route):
    new_route = route[:]
    i, j = random.sample(range(len(route)), 2)  # Select two random indices
    new_route[i], new_route[j] = new_route[j], new_route[i]  # Swap two locations
    return new_route

# Hill Climbing Algorithm
def hill_climbing(locations, max_iterations=1000):
    current_route = random.sample(locations, len(locations))  # Start with a random route
    current_distance = total_distance(current_route)

    for _ in range(max_iterations):
        neighbor_route = get_neighbor(current_route)  # Generate a neighboring solution
        neighbor_distance = total_distance(neighbor_route)

        if neighbor_distance < current_distance:  # Accept the new route only if it's shorter
            current_route, current_distance = neighbor_route, neighbor_distance

    return current_route, current_distance

# Example delivery points (x, y coordinates)
locations = [(0, 0), (2, 3), (5, 4), (8, 2), (6, 7), (1, 6), (4, 8), (9, 9)]

# Run Hill Climbing Algorithm
best_route, best_distance = hill_climbing(locations)

# Print results
print("Optimized Delivery Route:", best_route)
print("Total Distance Covered:", round(best_distance, 2))
