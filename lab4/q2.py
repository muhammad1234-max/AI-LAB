import heapq
import random
import time

# Graph with dynamic edge costs
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5, 'E': 10},
    'C': {'F': 3},
    'D': {'G': 2},
    'E': {'H': 4},
    'F': {'I': 8},
    'G': {'J': 6},
    'H': {'J': 3},
    'I': {'J': 7},
    'J': {}  # Goal node
}

# Heuristic function (Manhattan distance approximation)
heuristic = {
    'A': 10, 'B': 8, 'C': 7, 'D': 5, 'E': 6,
    'F': 6, 'G': 3, 'H': 2, 'I': 4, 'J': 0  # Goal node
}

# Function to randomly update edge costs at runtime
def update_edge_costs():
    for node in graph:
        for neighbor in graph[node]:
            if random.random() < 0.3:  # 30% chance of cost change
                new_cost = random.randint(1, 10)  # Random new cost
                print(f"Edge cost updated: {node} → {neighbor} = {new_cost}")
                graph[node][neighbor] = new_cost

# A* Search Function with Dynamic Cost Updates
def dynamic_a_star(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0 + heuristic[start], start))  # (f, node)
    g_costs = {node: float('inf') for node in graph}
    g_costs[start] = 0
    came_from = {start: None}

    while frontier:
        time.sleep(1)  # Simulate real-time updates
        update_edge_costs()  # Randomly update edge costs

        _, current = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            print("\nOptimal Path Found:", path)
            return path

        for neighbor in graph[current]:
            new_g_cost = g_costs[current] + graph[current][neighbor]
            if new_g_cost < g_costs[neighbor]:  # Update path if better
                g_costs[neighbor] = new_g_cost
                f_cost = new_g_cost + heuristic[neighbor]
                heapq.heappush(frontier, (f_cost, neighbor))
                came_from[neighbor] = current

    print("\nNo Path Found!")
    return None

# Run Dynamic A* Search
print("\nRunning A* Search with Dynamic Edge Costs...")
dynamic_a_star(graph, 'A', 'J')
