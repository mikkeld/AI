from tic_tac_toe import Board
import random
from game_agent import CustomPlayer

class RandomPlayer(object):
    def __init__(self):
        self.name = "random idiot"

    def get_name(self):
        return self.name

    def get_move(self, game):
        return random.choice(game.available_moves())


def play_game(player1, player2):
    game = Board(player1, player2)

    winner = None

    for i in range(9):
        print("state:", game.board_state)
        move = game.get_active_player().get_move(game)
        game.apply_move(move)
        player = game.get_active_player()
        if game.is_winner(player):
            winner = player
            break

    try:
        return game.player_symbols[winner]
    except KeyError:
        return None


def play_n_games(n):
    winners = {1: 0, 2: 0, None: 0}
    for i in range(n):
        player1 = CustomPlayer()
        player2 = RandomPlayer()
        winner = play_game(player1, player2)
        winners[winner] += 1

    return winners


print(play_n_games(1))