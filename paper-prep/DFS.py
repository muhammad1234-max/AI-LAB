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
# DFS Function
def dfs(graph, start, goal):
visited = [] # List for visited nodes
stack = [] # Initialize stack

visited.append(start)
stack.append(start)

while stack:
node = stack.pop() # LIFO: Pop from top
print(node, end=" ")
if node == goal: # Stop if goal is found
print("\nGoal found!")
break

for neighbour in reversed(graph[node]): # Reverse to maintain
correct order
if neighbour not in visited:
visited.append(neighbour)
stack.append(neighbour)
# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Run DFS
print("\nFollowing is the Depth-First Search (DFS):")
dfs(graph, start_node, goal_node)
