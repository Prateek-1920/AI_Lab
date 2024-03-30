max_x = int(input("Max capacity X: "))
max_y = int(input("Max capacity Y: "))

class State:
    """Current state of the jugs.
    
    Attributes:
        X (int): gallons of water in the max_x-gallon jug
        Y (int): gallons of water in the max_y-gallon jug
        rule (int): id of rule taken from parent state
    """
    def __init__(self, X=0, Y=0, rule=None):
        self.X = X
        self.Y = Y
        self.rule = rule
    
    def neighbors(self) -> list[tuple]:
        result = []
        X, Y = self.X, self.Y

        if X < max_x: 
            result.append(State(max_x, Y, 1)) # fill X
        if Y < max_y:
            result.append(State(X, max_y, 2)) # fill Y
        if X > 0:
            result.append(State(0, Y, 3)) # empty X
        if Y > 0:
            result.append(State(X, 0, 4)) # empty Y
        if X + Y >= max_x and Y > 0:
            result.append(State(max_x, Y - (max_x - X), 5)) # pour from Y to X
        if X + Y >= max_y and X > 0:
            result.append(State(X - (max_y - Y), max_y, 6)) # pour from X to Y
        if X + Y <= max_x and Y > 0:
            result.append(State(X + Y, 0, 7)) # pour all from Y to X
        if X + Y <= max_y and X > 0:
            result.append(State(0, X + Y, 8)) # pour all from X to Y
        
        return result
    
    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y
    
    def __str__(self):
        rule_str = f" # rule {self.rule}" if self.rule else ""
        return f"({self.X}, {self.Y})" + rule_str
    
    def __hash__(self):
        return self.X * 10 + self.Y

def construct_path(prev, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = prev[current]
    path.append(start)
    path.reverse()
    return path

def bfs(start, goal):
    frontier = [start]
    prev = {start: None}

    while frontier:
        current = frontier.pop(0)

        if current == goal:
            break

        for next in current.neighbors():
            if next not in prev:
                frontier.append(next)
                prev[next] = current

    return construct_path(prev, start, goal)

def dfs(start, goal):
    frontier = [start]
    prev = {start: None}

    while frontier:
        current = frontier.pop() # the only line that differs from bfs

        if current == goal:
            break

        for next in current.neighbors():
            if next not in prev:
                frontier.append(next)
                prev[next] = current

    return construct_path(prev, start, goal)

def display_path(path):
    for q in path:
        print(q)

print("Enter goal state")
X_g = int(input("X jug goal: "))
Y_g = int(input("Y jug goal: "))
print(f"Goal state = ({X_g}, {Y_g})")

start = State(0, 0)
goal = State(X_g, Y_g)

bfs_path = bfs(start, goal)
dfs_path = dfs(start, goal)

print("\nBFS Path:")
display_path(bfs_path)

print("\nDFS Path:")
display_path(dfs_path)

