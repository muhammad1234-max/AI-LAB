# tree Representation
tree = {
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
# BFS Function
def bfs(tree, start, goal):
visited = [] # List for visited nodes
queue = [] # Initialize a queue
visited.append(start)
queue.append(start)
while queue:
node = queue.pop(0) # Dequeue
print(node, end=" ")
if node == goal: # Stop if goal is found
print("\nGoal found!")
break
for neighbour in graph[node]:
if neighbour not in visited:
visited.append(neighbour)
queue.append(neighbour)
# BFS Function
# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'
# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(tree, start_node, goal_node)
