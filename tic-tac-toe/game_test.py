from tic_tac_toe import Board, Position
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


if __name__ == '__main__':
    unittest.main()
