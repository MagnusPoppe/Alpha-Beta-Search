import sys


def argmax(values: ((int, int), int)) -> (int, int):
    best_action, best_utility = None, None
    for (y, x), utility in values:
        if not best_utility or (best_utility and best_utility < utility):
            best_action, best_utility = (y, x), utility
    return best_action


def minimax_decision(state, player, terminal, switch_players, utility, apply, actions):
    # def min_value(state, player):
    #     if terminal(state):
    #         return utility(state, player)
    #
    #     v = sys.maxsize
    #     for action in actions(state):
    #         v = min(v, max_value( apply(action, state, player), switch_players(player)) )
    #     return v

    # def max_value(state, player):
    #     if terminal(state):
    #         return utility(state, player)
    #     v = -sys.maxsize
    #     for action in actions(state):
    #         v = max(v, min_value( apply(action, state, player), switch_players(player) ))
    #     return v

    def value(fn, init_value, state, player):
        if terminal(state):
            return utility(state, player)

        v = sys.maxsize
        for action in actions(state):
            best_utility = value(
                min if init_value < 0 else max,
                sys.maxsize if init_value < 0 else -sys.maxsize,
                apply(action, state, player),
                switch_players(player)
            )
            v = fn(v, best_utility)
        return v

    utilities = []
    for a in actions(state):
        utilities = [(a, value(max, -sys.maxsize, apply(a, state, player), player))]
    return argmax(utilities)
