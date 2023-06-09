import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_distance(self, dist, visited):
        min_value = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_value and not visited[v]:
                min_value = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        visited = [False] * self.V

        dist[src] = 0

        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if (
                    not visited[v]
                    and self.graph[u][v] > 0
                    and dist[u] + self.graph[u][v] < dist[v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

# Example usage:
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

src = 0
distances = g.dijkstra(src)
print("Shortest distances from source vertex", src)
for v in range(g.V):
    print(f"To vertex {v}: Distance = {distances[v]}")
