
players = {1: "X", 2: "O"}


def generate_board(board=None):
    l = []
    for y in range(3):
        l += [[]]
        for x in range(3):
            if board and board[y][x] >= 0:
                l[y] += [board[y][x]]
            else:
                l[y] += [-1]
    return l


def print_board(board):
    global players
    for y in board:
        for x in y:
            print("+" if x < 0 else players[x], end=" ")
        print()

def actions(state):
    for y in range(3):
        for x in range(3):
            if state[y][x] < 0:
                yield (y, x)


def switch_players(player):
    global players
    return [p for p in players.keys() if p != player][0]

def get_player_symbol(player):
    global players
    return players[player]

def apply_action(action, state, player):
    y, x = action
    new_state = generate_board(state)
    new_state[y][x] = player
    return new_state


def calculate_utility(state, player):
    global players
    utility = 0
    for current_player in players.keys():
        addon = 1 if player == current_player else -1
        if all(current_player == state[i][i] for i in range(3)): utility += addon
        if all(current_player == state[2-i][i] for i in range(3)): utility += addon
        for j in range(3):
            if all(current_player == state[j][i] for i in range(3)): utility += addon
            if all(current_player == state[i][j] for i in range(3)): utility += addon
    return utility


def terminal(state):
    for current_player in players.keys():
        if all(current_player == state[i][i] for i in range(3)):
            return True
        if all(current_player == state[2-i][i] for i in range(3)):
            return True
        for j in range(3):
            if all(current_player == state[j][i] for i in range(3)):
                return True
            if all(current_player == state[i][j] for i in range(3)):
                return True

    return all([state[y][x] > 0 for x in range(3) for y in range(3)])


