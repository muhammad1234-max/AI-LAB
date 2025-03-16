# Graph Representation
graph = {
0: [1, 3],
1: [0, 3],
2: [4,5],
3: [0, 1, 6, 4],
4: [3, 2, 5],
5: [4, 2, 6],
6: [3, 5]
}

# BFS Function
def bfs(graph, start, goal):
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
# Define Start and Goal Nodes
start_node =0
goal_node = 5
# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(graph, start_node, goal_node)
