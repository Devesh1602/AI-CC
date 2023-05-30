#Time Complexity of BFS = O(V+E) where V is vertices and E is edges. 
#Time Complexity of DFS is also O(V+E) where V is vertices and E is edges.
#Space Complexity for BFS is O(w) where w is the maximum width of the tree.
#Space Complexity for DFS is O(h) where h is the maximum height of the tree.
# BFS
''''
graph = {'A':['B', 'E', 'C'],
         'B':['A', 'D', 'E'],
         'D':['B', 'E'],
         'E':['A', 'D', 'B'],
         'C':['A', 'F', 'G'],
         'F':['C'],
         'G':['C']
         }      
'''
graph = {}
num_edges = int(input("Enter the number of edges in the graph: "))
for _ in range(num_edges):
    source, target = input("Enter an edge (source target): ").split()
    if source not in graph:
        graph[source] = []
    if target not in graph:
        graph[target] = []
    graph[source].append(target)

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

visited = []
queue = []

def bfs(visited, graph, start_node, goal_node):
    visited.append(start_node)
    queue.append(start_node)
    while queue:
        m = queue.pop(0)
        print("Node:", m)
        if m == goal_node:
            print("Goal node found!")
            break
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)

print("\nBFS Traversal")
bfs(visited, graph, start_node, goal_node)

# DFS

visited = []
stack = []

def dfs(graph, start, goal):
    stack.append(start)
    visited.append(start)
    while stack:
        node = stack[-1]
        stack.pop()
        print("Node:", node)
        if node == goal:
            print("Goal node found!")
            return
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                stack.append(n)

print("\nDFS Traversal")
dfs(graph, start_node, goal_node)

'''
Enter the number of edges: 5
Enter edge 1: A B
Enter edge 2: B C
Enter edge 3: C D
Enter edge 4: A D
Enter edge 5: B D
Enter the start node: A
Enter the goal node: D

The BFS Traversal is:
Node:  A
Node:  B
Node:  D
Goal node found!

DFS traversal is:
Node:  A
Node:  D
Goal node found!

'''