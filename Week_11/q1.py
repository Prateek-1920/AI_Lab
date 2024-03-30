from random import randint

N = 8

def configureRandomly():
    return [randint(0, N-1) for _ in range(N)]

def printBoard(board):
    for row in board:
        print(*row)

def calculateObjective(board, state):
    row_count = [0] * N
    diag1_count = [0] * (2 * N - 1)
    diag2_count = [0] * (2 * N - 1)

    for i in range(N):
        row_count[state[i]] += 1
        diag1_count[i + state[i]] += 1
        diag2_count[i - state[i] + N - 1] += 1

    attacking = 0
    for count in [row_count, diag1_count, diag2_count]:
        for c in count:
            attacking += c * (c - 1) // 2

    return attacking

def getNeighbour(state, current_obj):
    best_state = state[:]
    best_obj = current_obj

    for i in range(N):
        for j in range(N):
            if state[i] != j:
                new_state = state[:]
                new_state[i] = j
                obj = calculateObjective(None, new_state)
                if obj < best_obj:
                    best_obj = obj
                    best_state = new_state

    return best_state, best_obj

def hillClimbing():
    state = configureRandomly()
    current_obj = calculateObjective(None, state)

    while True:
        new_state, new_obj = getNeighbour(state, current_obj)

        if new_obj >= current_obj:
            return state

        state = new_state
        current_obj = new_obj

board = [[0 for _ in range(N)] for _ in range(N)]
final_state = hillClimbing()
for i in range(N):
    board[final_state[i]][i] = 1

printBoard(board)
