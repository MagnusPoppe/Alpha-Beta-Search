import sys
import time

from adverserial_search.alpha_beta_pruning import alpha_beta_search
from adverserial_search.minimax import minimax_decision
from adverserial_search.tic_tac_toe_functions import *

if __name__ == '__main__':
    human_player = len(sys.argv) == 2 and sys.argv[1] == "human-player"

    state = generate_board()
    player = 1
    runtimes = []
    algorithms = [("Minimax", minimax_decision), ("Alpha-Beta", alpha_beta_search)]
    for name, search_algorithm in algorithms:
        start = time.time()
        while not terminal(state):
            if human_player and player == 1:
                action = input("select move coordinates (x, y): ").split(",")
                action = (int(x) for x in action)
            else:
                action = search_algorithm(
                    state,
                    player,
                    terminal,
                    switch_players,
                    calculate_utility,
                    apply_action,
                    actions
                )

            state = apply_action(action, state, player)
            print(f"Player \"{get_player_symbol(player)}\" made the move {action}")
            print_board(state)
            player = switch_players(player)
        print(f"\nFinal state of {name}")
        print_board(state)
        print(f"{name} used {(time.time() - start):.6} seconds!")
        runtimes += [(name, time.time() - start)]

    runtimes.sort(key=lambda x: x[1])
    (best_name, best_time), (worst_name, worst_time) = runtimes
    print(f"\nPerformance:\n{best_name} was {worst_time/best_time:.1}x faster than {worst_name}")