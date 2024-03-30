class BoardConfiguration:
    def __init__(self, config: list[int]):
        self.config = config
    
    def neighbors(self) -> list:
        blank_index = self.config.index(None)
        result = []
        for offset in [-1, 1, -3, 3]:
            swap_index = blank_index + offset

            if (abs(offset) == 1 and swap_index // 3 != blank_index // 3):
                continue
            
            if swap_index in range(9):
                tmp = self.config.copy()
                tmp[swap_index], tmp[blank_index] = None, tmp[swap_index]
                result.append(tmp)

        return [BoardConfiguration(i) for i in result] 
    def __hash__(self) -> int:
        return self.config.index(None)
    
    def __lt__(self, other) -> bool:       
        return self.config.index(None) < other.config.index(None)
    
    def __eq__(self, other) -> bool:
        return self.config == other.config

    def __str__(self) -> str:
        result = "-" * 5 + "\n"
        for i in range(3):
            for j in range(3):
                value = self.config[i * 3 + j]
                result += (str(value) if value else " ") + " "
            result += "\n"
        result += "-" * 5
        return result

def backtrack(end: BoardConfiguration, prev: dict) -> list:
    path = []
    current = end
    while prev[current]:
        path.append(current)
        current = prev[current]
    return path[::-1]

def heuristic(current: BoardConfiguration, goal: BoardConfiguration) -> int:
    h = 0
    for i in range(9):
        x = goal.config.index(current.config[i])
        h += abs((i % 3) - (x % 3))     # col diff
        h += abs((i // 3) - (x // 3))   # row diff
    return h // 2 

from heapq import heappush, heappop
from collections import defaultdict

def a_star(start, goal) -> list[BoardConfiguration]:
    dist = defaultdict(lambda: float("inf"))  # initial distance estimates
    dist[start] = 0

    prev = defaultdict(lambda: None)
    prev[start] = None

    frontier = [(0, start)] # "frontier" to be explored 
    closed = set()

    while frontier:
        priority_current, current = heappop(frontier)
        
        if current == goal:
            break

        closed.add(current)

        for neighbor in current.neighbors():
            if neighbor in closed:
                continue

            alt_dist = dist[current] + 1 
            if alt_dist < dist[neighbor]:
                dist[neighbor] = alt_dist
                prev[neighbor] = current
                priority = alt_dist + heuristic(neighbor, goal)
                heappush(frontier, (priority, neighbor)) 

    return backtrack(current, prev)

goal_config = [1, 2, 3, 8, None, 4, 7, 6, 5]
start_config = [2, 8, 3, 1, 6, 4, 7, None, 5]

start = BoardConfiguration(start_config)
goal = BoardConfiguration(goal_config)

path = a_star(start, goal)
for b in path:
    print(b)

