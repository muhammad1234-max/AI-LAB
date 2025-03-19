import heapq
import math

# Function to calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Greedy Best-First Search for Delivery Route Optimization
def greedy_delivery_route(start, delivery_points):
    """
    start: (x, y) tuple representing the starting location
    delivery_points: List of tuples [(x, y, earliest_time, latest_time), ...]
    Returns: Optimized delivery route and total distance covered
    """
    route = []
    total_distance = 0
    current_time = 0
    current_location = start
    delivery_queue = []

    # Push all delivery points into priority queue sorted by deadline
    for point in delivery_points:
        x, y, earliest, latest = point
        heapq.heappush(delivery_queue, (latest, earliest, (x, y)))  # Priority: latest deadline

    while delivery_queue:
        _, earliest, next_point = heapq.heappop(delivery_queue)  # Get the most time-sensitive delivery
        travel_time = distance(current_location, next_point)

        # Check if we can reach this point within the time window
        if current_time + travel_time <= earliest:
            current_time = earliest  # Wait until the earliest delivery time
        elif current_time + travel_time > _:
            continue  # Skip delivery if it can't be made on time
        
        # Move to the next delivery point
        route.append(next_point)
        total_distance += travel_time
        current_time += travel_time  # Update current time
        current_location = next_point

    return route, round(total_distance, 2)

# Example delivery points with time windows (x, y, earliest_time, latest_time)
delivery_points = [
    (3, 4, 5, 10),
    (7, 2, 2, 8),
    (8, 8, 6, 12),
    (2, 6, 1, 5),
    (6, 5, 4, 9)
]

# Run the Greedy Best-First Search for Delivery Route Optimization
start_location = (0, 0)
optimized_route, total_distance = greedy_delivery_route(start_location, delivery_points)

# Print results
print("Optimized Delivery Route:", optimized_route)
print("Total Distance Covered:", total_distance)
