import sys


def alpha_beta_search(state, player, terminal, switch_players, utility, apply, actions):
    def max_value(state, player, alpha, beta):
        if terminal(state):
            return utility(state, player)

        v = -sys.maxsize
        for action in actions(state):
            v = min_value(apply(action, state, player), switch_players(player), alpha, beta)
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, player, alpha, beta):
        if terminal(state):
            return utility(state, player)

        v = sys.maxsize
        for action in actions(state):
            v = max_value(apply(action, state, player), switch_players(player), alpha, beta)
            if alpha <= v:
                return v
            beta = min(v, beta)
        return v

    alpha = -sys.maxsize
    beta = sys.maxsize
    util = -sys.maxsize
    best_action = None
    for action in actions(state):
        best_utility = max_value(apply(action, state, player), player, alpha, beta)
        if util < best_utility:
            best_action = action
    return best_action


def alpha_beta_set_depth_search(_state, player, max_depth, switch_players, eval, apply, actions):
    def max_value(state, player, alpha, beta, depth):
        if depth == max_depth:
            return eval(state, player)

        v = -sys.maxsize
        for action in actions(state):
            v = min_value(apply(action, state, player), switch_players(player), alpha, beta, depth+1)
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, player, alpha, beta, depth):
        if depth == max_depth:
            return eval(state, player)

        v = sys.maxsize
        for action in actions(state):
            v = max_value(apply(action, state, player), switch_players(player), alpha, beta, depth+1)
            if alpha <= v:
                return v
            beta = min(v, beta)
        return v

    _alpha = -sys.maxsize
    _beta = sys.maxsize
    util = -sys.maxsize
    best_action = None
    for action in actions(_state):
        best_utility = max_value(apply(action, _state, player), player, _alpha, _beta, depth=1)
        if util < best_utility:
            best_action = action
    return best_action
