class Graph:
    def __init__(self, edges, n):
 
        self.adjList = [None] * n
 
        for i in range(n):
            self.adjList[i] = []
 
        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))
 
 
def printGraph(graph):
    for src in range(len(graph.adjList)):
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()
 
 
if __name__ == '__main__':
 
    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
            (4, 5, 1), (5, 4, 3)]
 
    n = 6
 
    graph = Graph(edges, n)
 
    printGraph(graph)