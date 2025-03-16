# Maze representation as a graph
maze = [
[1, 1, 0],
[0, 1, 0],
[0, 1, 1]
]
# Directions for movement (right and down)
directions = [(0, 1), (1, 0)] # (row, col)
# Convert maze to a graph (adjacency list representation)
def create_graph(maze):
graph = {}
rows = len(maze)
cols = len(maze[0])
for i in range(rows):
for j in range(cols):
if maze[i][j] == 1: # If it's an open path
neighbors = []
for dx, dy in directions:
nx, ny = i + dx, j + dy
if 0 <= nx < rows and 0 <= ny < cols and
maze[nx][ny] == 1:
neighbors.append((nx, ny))
graph[(i, j)] = neighbors
return graph
# BFS Function using queue
def bfs(graph, start, goal):
visited = [] # List for visited nodes
queue = [] # Initialize queue
visited.append(start)
queue.append(start)
while queue:
node = queue.pop(0) # FIFO: Dequeue from front
print(node, end=" ")
if node == goal: # Stop if goal is found
print("\nGoal found!")
break
for neighbour in graph[node]: # Visit neighbors
if neighbour not in visited:
visited.append(neighbour)
queue.append(neighbour)
# Create graph from maze
graph = create_graph(maze)
# Define Start and Goal nodes
start_node = (0, 0) # Starting point (0,0)
goal_node = (2, 2) # Goal point (2,2)
# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(graph, start_node, goal_node)
