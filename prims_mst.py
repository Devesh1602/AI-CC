#T.C.->O(V^2) #If adjacency list O((V + E) log V)
#S.C.->O(V^2) can be reduced to O(V + E) because adjacency list representation only stores the edges


def prim(graph):
    num_vertices = len(graph)
    num_edges = []
    selected_vertices = [False] * num_vertices
    selected_vertices[0] = True

    while len(num_edges) < num_vertices - 1:
        min_weight = float('inf') #initial minimum weight value 
        u, v = -1, -1

        for i in range(num_vertices):
            if selected_vertices[i]:
                for j in range(num_vertices):
                    if not selected_vertices[j] and graph[i][j]:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            u, v = i, j

        num_edges.append((u, v, min_weight))
        selected_vertices[v] = True

    return num_edges


print("Enter the number of vertices in the graph:")
num_vertices = int(input())
graph = []

print("Enter the adjacency matrix of the graph:")
for _ in range(num_vertices):
    row = list(map(int, input().split()))
    graph.append(row)

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree Edges:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})")

'''
Enter the number of vertices in the graph:
5
Enter the adjacency matrix of the graph:
0 2 0 6 0
2 0 3 8 5
0 3 0 0 7
6 8 0 0 9
0 5 7 9 0


'''