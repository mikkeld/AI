from tic_tac_toe import Board, Position
from game_agent import CustomPlayer
import unittest


class TestBoard(unittest.TestCase):
    player1 = 1
    player2 = 2
    board = Board(1, 2)

    def test_winning_combination(self):
        self.board.board_state = [[1, 1, 1], [2, 0, 2], [0, 0, 2]]
        assert(self.board.is_winner(self.player1)) is True

    def test_losing_combination(self):
        self.board.board_state = [[1, 1, 0], [2, 0, 2], [0, 1, 2]]
        assert (self.board.is_winner(self.player1)) is False

class TestCustomPlayer(unittest.TestCase):
    player1 = CustomPlayer()
    player2 = CustomPlayer()
    game = Board(player1, player2)

    def test_move(self):
        self.game.board_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        move = self.player1.get_move(self.game)
        print("move:", move.column, move.row)
        self.game.apply_move(move)
        print(self.game.board_state)




if __name__ == '__main__':
    unittest.main()
