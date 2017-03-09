"""
This file contains the Board class which implements
the rules for the game TicTacToe
"""

from copy import copy
from copy import deepcopy

ROWS = '012'
COLS = '012'

class Board(object):
    """
    Implement a model for the game TicTacToe

    Parameters
    ----------
    player1 : object
        An object with the get_move() function
    player2 : object:
        An object with the get_move() function
    """

    BLANK = 0

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.active_player = player1
        self.move_count = 0
        self.board_state = [[Board.BLANK for i in range(3)] for j in range(3)]
        self.player_symbols = {player1: 1, player2: 2}

    def set_active_player(self):
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1

    def get_active_player(self):
        return self.active_player

    def get_board_state(self):
        return self.board_state

    def get_opponent(self, player):
        if player == self.player1: return self.player2
        else: return self.player1

    def forecast_move(self, move):
        """
        Returns a deep copy of the current game with the move applied to it
        :param move: (int, int)
            A coordinate pair (row, column) indicating the next move
        :return: board: (Board)
            A new board with the moved applied to it
        """
        new_board = copy(self)
        new_board.board_state[move.row][move.column] = self.player_symbols[self.active_player]
        return new_board

    def apply_move(self, move):
        """
        Applies the move to the board and updates the board with the new move
        :param move: A coordinate (row, column)
        """
        self.board_state[move.row][move.column] = self.player_symbols[self.active_player]
        self.set_active_player()
        self.move_count += 1

    def available_moves(self):
        """
        Find all available cells. If all bricks are not yet placed,
        only mark 0 cells as available. If not, mark 0 cells and the
        player who currently has the turn as available
        :return: A list of Position (row, column) indexes
        """
        result = []

        if self.move_count > 9:
            return None
        for row_index, rows in enumerate(self.board_state):
            for column_index, unit in enumerate(rows):
                if unit == 0:
                    result.append(Position(row_index, column_index))

        return result

    def winning_combinations(self):
        """
        Find all rows, columns and crosses of winning combinations
        :return: Return a list of touples indicating winning combinations
        """
        rows = [[Position(int(r), int(c)) for c in COLS] for r in ROWS]
        cols = [[Position(int(c), int(r)) for c in COLS] for r in ROWS]
        crosses = [[Position(0, 0), Position(1, 1), Position(2, 2)], [Position(2, 0), Position(1, 1), Position(0, 2)]]
        return rows + cols + crosses

    def is_winner(self, player):
        for c in self.winning_combinations():
            if all((self.board_state[p.row][p.column] is self.player_symbols[player] for p in c)):
                return True
        else:
            return False

    def utility(self, player):
        if self.is_winner(player):
            return float('inf')
        if self.is_winner(self.get_opponent(player)):
            return float('-inf')
        else:
            return 0.

    def copy(self):
        """ Return a deep copy of the current board. """
        new_board = Board(self.player1, self.player2)
        new_board.move_count = self.move_count
        new_board.active_player = self.active_player
        new_board.player_symbols = copy(self.player_symbols)
        new_board.board_state = deepcopy(self.board_state)
        return new_board


class Position(object):
    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column

    def get_position(self):
        return self.row, self.column



