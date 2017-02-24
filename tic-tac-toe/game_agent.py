from tic_tac_toe import *
import random


def custom_score(game, player):
    if game.is_winner(game.get_opponent(player)):
        return float("-inf")
    if game.is_winner(player):
        return float("inf")
    else:
        return 0


class CustomPlayer(object):
    """
    The custom player is clever and play the game by looking at
    the whole tree to make the best decision
    """
    def __init__(self, score_fn=custom_score, method="minimax"):
        self.test = 0
        self.method = method
        self.score = score_fn

    def get_move(self, game):
        if self.method == "minimax":
            _, best_move = self.minimax(game)
            result = best_move
        else:
            result = random.choice(game.available_moves())
        return result

    def minimax(self, game, max_player=True):
        available_moves = game.available_moves()
        best_move = None
        if not available_moves:
            return game.utility(self), Position(0, 0)

        if game.is_winner(self) or game.is_winner(game.get_opponent(self)):
            return self.score(game, self), Position(0, 0)

        if max_player:
            best_score = float('-inf')
            for move in available_moves:
                new_state = game.forecast_move(move)
                score, _ = self.minimax(new_state, False)
                if score > best_score:
                    best_move, best_score = move, score
        else:
            best_score = float('inf')
            for move in available_moves:
                new_state = game.forecast_move(move)
                score, _ = self.minimax(new_state, True)
                if score < best_score:
                    best_move, best_score = move, score

        return best_score, best_move

    def alphabeta(self):
        pass