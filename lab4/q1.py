from queue import PriorityQueue

class Node:
    def __init__(self, position, visited_goals=None, parent=None):
        self.position = position
        self.parent = parent
        self.visited_goals = visited_goals if visited_goals else set()
        self.g = 0  # Cost from start node
        self.h = 0  # Heuristic (Manhattan distance)
        self.f = 0  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f  # Priority queue comparison

def heuristic(current_pos, goals):
    """ Returns the minimum Manhattan distance to any unvisited goal. """
    return min(abs(current_pos[0] - gx) + abs(current_pos[1] - gy) for gx, gy in goals)

def best_first_search_multi_goal(maze, start, goal_positions):
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start, set())
    frontier = PriorityQueue()
    frontier.put((0, start_node))  # (priority, node)
    visited_states = set()

    while not frontier.empty():
        _, current_node = frontier.get()
        current_pos = current_node.position
        visited_goals = current_node.visited_goals.copy()

        # If the current position is a goal, mark it as visited
        if current_pos in goal_positions:
            visited_goals.add(current_pos)

        # If all goals are visited, reconstruct the path
        if visited_goals == set(goal_positions):
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse path to get the correct order

        # Mark state as visited (position + visited goals)
        state = (current_pos, frozenset(visited_goals))
        if state in visited_states:
            continue
        visited_states.add(state)

        # Generate adjacent nodes
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0:
                new_node = Node(new_pos, visited_goals, current_node)
                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_pos, goal_positions - visited_goals)
                new_node.f = new_node.g + new_node.h
                frontier.put((new_node.f, new_node))

    return None  # No path found

# Example maze with obstacles (1 = Wall, 0 = Open path)
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal_positions = {(4, 4), (2, 3), (1, 4)}  # Multiple goal locations

# Run Best-First Search for Multiple Goals
path = best_first_search_multi_goal(maze, start, goal_positions)

# Print results
if path:
    print("\nShortest Path Visiting All Goals:", path)
else:
    print("\nNo Path Found!")
