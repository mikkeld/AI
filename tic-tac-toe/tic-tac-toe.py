ROWS = '123'
COLS = '123'

class Board(object):

    BLANK = 0


    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.active_player = player1
        self.move_count = 0
        self.board_state = [[Board.BLANK for i in range(3)] for j in range(3)]
        self.player_symbols = {player1: 1, player2: 2}

    def forecast_placement(self, placement):
        pass

    def forecast_move(self, move):
        new_board_state = self.board_state.copy()
        row, col = move
        new_board_state[row][col] = self.player_symbols[self.active_player]

    def apply_placement(self, placement):
        pass

    def apply_move(self, move):
        row, col = move
        self.board_state[row][col] = self.player_symbols[self.active_player]

    def available_moves(self):
        result = []

        if self.move_count < 6:
            for row_index, rows in enumerate(self.board_state):
                for column_index, unit in enumerate(rows):
                    if unit == 0:
                        result.append(Position(row_index, column_index))
        else:
            for row_index, rows in enumerate(self.board_state):
                for column_index, unit in enumerate(rows):
                    if unit == 0 or unit == self.player_symbols[self.active_player]:
                        result.append(Position(row_index, column_index))
        return result

    def winning_combinations(self):
        rows = [[(r, c) for c in COLS] for r in ROWS]
        cols = [[(c, r) for c in COLS] for r in ROWS]
        crosses = [[(1,1), (2,2), (3,3)], [(3,1), (2,2), (1,3)]]
        return crosses

    def is_winner(self, player):
        for c in self.winning_combinations():
            if all((p is self.player_symbols[player] for p in c)):
                return True
        else:
            return False


class Position(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def get_position(self):
        return self.row, self.column


board = Board("a", "b")
winning_combinations = board.winning_combinations()
for position in winning_combinations:
    print(position)
