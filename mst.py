def mst(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    parent = [None] * num_vertices
    key = [float('inf')] * num_vertices

    # Start with the first vertex as the root
    parent[0] = -1
    key[0] = 0

    for _ in range(num_vertices):
        # Find the vertex with the minimum key value
        min_key = float('inf')
        min_index = -1
        for i in range(num_vertices):
            if not visited[i] and key[i] < min_key:
                min_key = key[i]
                min_index = i

        # Mark the vertex as visited
        visited[min_index] = True

        # Update the key and parent values for the adjacent vertices
        for j in range(num_vertices):
            if (
                graph[min_index][j] > 0  # Check if there is an edge
                and not visited[j]  # Check if the vertex is not visited
                and graph[min_index][j] < key[j]  # Check if the weight is smaller
            ):
                parent[j] = min_index
                key[j] = graph[min_index][j]

    # Return the MST as a list of edges
    mst = []
    for i in range(1, num_vertices):
        mst.append((parent[i], i))

    return mst
