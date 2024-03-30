

import heapq

def uniform_cost_search(start, goal, graph, cost, node_names):
    answer = [10**8 for i in range(len(goal))]

    queue = []

    heapq.heappush(queue, (0, start))

    visited = {}

    count = 0

    while len(queue) > 0:

        p = heapq.heappop(queue)

        if p[1] in goal:

            index = goal.index(p[1])

            if answer[index] == 10**8 or answer[index] > p[0]:
                count += 1

            if answer[index] > p[0]:
                answer[index] = p[0]

            if count == len(goal):
                return answer

        if p[1] not in visited:
            for i in range(len(graph[p[1]])):

                heapq.heappush(queue, (p[0] + cost[(p[1], graph[p[1]][i])], graph[p[1]][i]))

        visited[p[1]] = 1

    return answer

# main function
if __name__ == '__main__':
    
    num_nodes = int(input("Enter the number of nodes: "))
    graph = [[] for i in range(num_nodes)]
    cost = {}
    node_names = {}

    node_index = 0

    # add edges
    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        u, v, w = input("Enter edge u, v, and cost (separated by space): ").split()
        w = int(w)  
        if u not in node_names:
            node_names[u] = node_index
            node_index += 1
        if v not in node_names:
            node_names[v] = node_index
            node_index += 1
        graph[node_names[u]].append(node_names[v])
        cost[(node_names[u], node_names[v])] = w

    start_node = input("Enter the start node: ")
    goal_nodes = input("Enter the goal nodes (separated by space): ").split()

    start_node = node_names[start_node]
    goal_nodes = [node_names[node] for node in goal_nodes]

    answer = uniform_cost_search(start_node, goal_nodes, graph, cost, node_names)

    start_node_name = [name for name, index in node_names.items() if index == start_node][0]
    goal_node_names = [name for name, index in node_names.items() if index in goal_nodes]

    for i in range(len(goal_nodes)):
        print(f"Minimum cost from {start_node_name} to {goal_node_names[i]} is = {answer[i]}")
