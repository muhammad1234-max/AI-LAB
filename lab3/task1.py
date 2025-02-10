import heapq

class GoalBasedAgentDFS:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        return percept == self.goal

    def act(self, percept, environment):
        if self.formulate_goal(percept):
            return f"Goal {self.goal} found!"
        return environment.dfs_search(percept, self.goal)

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def dfs_search(self, start, goal):
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()
            print(f"Visiting: {node}")
            
            if node == goal:
                return f"Goal {goal} found!"
            
            if node not in visited:
                visited.append(node)
                stack.extend(reversed(self.graph.get(node, [])))
        return "Goal not found"


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

# Define Graph for DFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

start_node = 'A'
goal_node = 'I'

environment = Environment(graph)
agent = GoalBasedAgentDFS(goal_node)
run_agent(agent, environment, start_node)


# Depth-Limited Search (DLS) as Goal-Based Agent
def dls(graph, start, goal, depth_limit):
    visited = []

    def dfs(node, depth):
        if depth > depth_limit:
            return None
        visited.append(node)
        if node == goal:
            print(f"Goal found with DLS. Path: {visited}")
            return visited
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                path = dfs(neighbor, depth + 1)
                if path:
                    return path
        visited.pop()
        return None
    return dfs(start, 0)

dls(graph, 'A', 'I', 3)


# Uniform Cost Search (UCS) as a Utility-Based Agent
def ucs(graph, start, goal):
    frontier = [(0, start)]
    visited = {}
    came_from = {start: None}
    while frontier:
        cost, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited[node] = cost
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"Goal found with UCS. Path: {path}, Total Cost: {cost}")
            return
        for neighbor, edge_cost in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(frontier, (cost + edge_cost, neighbor))
                came_from[neighbor] = node
    print("Goal not found")

graph_with_costs = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}
ucs(graph_with_costs, 'A', 'I')


# Iterative Deepening DFS
def iterative_deepening(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Depth: {depth}")
        path = []
        if dls(graph, start, goal, depth):
            print("Path to goal:", " → ".join(reversed(path)))
            return
    print("Goal not found within depth limit.")

iterative_deepening('A', 'I', 5)


# Bidirectional Search
def bidirectional_search(graph, start, goal):
    from collections import deque
    if start == goal:
        return [start]
    
    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_visited = {start: None}
    backward_visited = {goal: None}
    
    while forward_queue and backward_queue:
        if forward_queue:
            node = forward_queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = node
                    forward_queue.append(neighbor)
                    if neighbor in backward_visited:
                        return construct_path(forward_visited, backward_visited, neighbor)
        
        if backward_queue:
            node = backward_queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor not in backward_visited:
                    backward_visited[neighbor] = node
                    backward_queue.append(neighbor)
                    if neighbor in forward_visited:
                        return construct_path(forward_visited, backward_visited, neighbor)
    return "No path found"

def construct_path(forward_visited, backward_visited, meeting_point):
    path = []
    node = meeting_point
    while node:
        path.append(node)
        node = forward_visited[node]
    path.reverse()
    node = backward_visited[meeting_point]
    while node:
        path.append(node)
        node = backward_visited[node]
    return path

graph_bidirectional = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}
print("Bidirectional Search Path:", bidirectional_search(graph_bidirectional, 'A', 'I'))
