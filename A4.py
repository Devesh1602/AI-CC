#T.C->O(k^n);k=no.of colors and n=no. of vertices
#S.C->O(n)

def isSafe(graph, color):
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] and color[j] == color[i]:
                return False
    return True

def bound(graph, color, i):
    max_colors = max(color)
    remaining_vertices = len(graph) - i - 1
    return max_colors + remaining_vertices

def graphColouring(graph, m, i, color):
    if i == len(graph):
        if isSafe(graph, color):
            printSolution(color)
            return True
        return False

    available_colors = sorted(set(range(1, m + 1)), key=color.count)

    for j in available_colors:
        color[i] = j

        if bound(graph, color, i) < m:
            color[i] = 0
            return False

        if graphColouring(graph, m, i + 1, color):
            return True
        color[i] = 0

    return False

def printSolution(color):
    print('Solution exists. Following are the assigned colors:')
    for i in range(len(color)):
        print(color[i], end=' ')

if __name__ == '__main__':
    print("Enter the number of vertices in the graph:")
    num_vertices = int(input())
    
    print("Enter the adjacency matrix of the graph (1 if there is an edge, 0 otherwise):")
    graph = []
    for _ in range(num_vertices):
        row = list(map(int, input().split()))
        graph.append(row)
    
    print("Enter the number of colors:")
    m = int(input())
    
    color = [0 for _ in range(num_vertices)]

    if not graphColouring(graph, m, 0, color):
        print('Solution does not exist')


'''
graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
'''