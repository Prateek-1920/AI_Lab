class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {
            'A': 7,
            'B': 3,
            'C': 4,
            'D': 6,
            'E': 5,
            'F': 6,
            'S': 5,
            'G1': 0,
            'G2': 0,
            'G3': 0

        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = [start_node]
        closed_list = []

        g = {}
        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while open_list:
            n = None

            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()

                print('Path found:', reconst_path)
                # instead of returning path we return (path, cost)
                return (reconst_path, g[stop_node])

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.append(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.append(m)

            open_list.remove(n)
            closed_list.append(n)

        print('Path does not exist!')
        return None


# Example usage:
adjacency_list = {
    'A': [('B', 3), ('G1', 9)],
    'B': [('A', 2), ('C', 1)],
    'C': [('G2', 5), ('F', 7), ('S', 6)],
    'D': [('C', 2), ('E', 2), ('S', 1)],
    'E': [('G3', 7)],
    'F': [('D', 2), ('G3', 8)],
    'S': [('A', 5), ('B', 9), ('D', 6)],
    'G1': [],
    'G2': [],
    'G3': []





}

graph = Graph(adjacency_list)
start_node = 'S'
goal_nodes = ['G1', 'G2', 'G3']

d = {goal: graph.a_star_algorithm(start_node, goal) for goal in goal_nodes}

nearest_goal = min(d, key=lambda goal: d[goal][1])

print(d[nearest_goal][0])
print(d[nearest_goal][1])