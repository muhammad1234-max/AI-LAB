from itertools import permutations

def tsp(graph, start):
    cities = list(graph.keys())
    min_cost = float('inf')
    best_path = []

    for perm in permutations(cities):
        if perm[0] == start:
            cost = sum(graph[perm[i]][perm[i+1]] for i in range(len(perm)-1)) + graph[perm[-1]][start]
            if cost < min_cost:
                min_cost = cost
                best_path = perm
    
    return best_path, min_cost

tsp_graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

start_city = 'A'
print("Optimal TSP Path and Cost:", tsp(tsp_graph, start_city))
