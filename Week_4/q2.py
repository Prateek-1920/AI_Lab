from collections import defaultdict, deque

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, queue, visited):

        while queue:
            vertex = queue.popleft()
            visited[vertex] = True
            
            for neighbor in self.graph[vertex]:
                if visited[neighbor] == False:
                    queue.append(neighbor)
                elif neighbor != -1:   
                    return True      
        
        return False     

    def isCyclic(self):
        visited = [False] * (self.V + 1)

        for i in range(self.V):
            if not visited[i]:
                queue = deque([i])
                if self.isCyclicUtil(queue, visited) == True:
                    return True

        return False


# Driver code
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")