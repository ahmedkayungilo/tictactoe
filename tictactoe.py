
class TicTacToe:
    def __init__(self):
        self.x_symbol = 'X'
        self.o_symbol = 'O'
        self.x_value = 1
        self.o_value = -1
        self.turn = self.x_symbol
        self.val = [" " for i in range(10)]
        self.values = [0 for i in range(10)]
        self.winner = ''
        self.can_continue = True

    def draw_board(self):
        self.board = f' {self.val[0]} | {self.val[1]} | {self.val[2]} \n-----------\n {self.val[3]} | {self.val[4]} | {self.val[5]} \n-----------\n {self.val[6]} | {self.val[7]} | {self.val[8]} '
        print(self.board)

    def play_move(self):
        move = input(f"{self.turn} to play: ")
        self.val[int(move) - 1] = self.turn
        print(self.val)

        # Give the turn to the next player
        if self.turn == self.x_symbol:
            self.values[int(move) - 1] = self.x_value
            print(self.values)
            self.turn = self.o_symbol
        else:
            self.values[int(move) - 1] = self.o_value
            self.turn = self.x_symbol

        # Display the board once the move has been played
        self.draw_board()

    def check_winner(self):
        sum_of_rows = [sum(self.values[0:2]), sum(self.values[3:5]), sum(self.values[6:8])]
        sum_of_cols = [
            self.values[0] + self.values[3] + self.values[6],
            self.values[1] + self.values[4] + self.values[7],
            self.values[2] + self.values[5] + self.values[8]
                       ]
        sum_of_diags = [
            self.values[0] + self.values[4] + self.values[8],
            self.values[2] + self.values[4] + self.values[6]
        ]

        if 3 in sum_of_diags or 3 in sum_of_cols or 3 in sum_of_rows:
            self.winner = self.x_symbol
            self.can_continue = False
        elif -3 in sum_of_cols or -3 in sum_of_diags or -3 in sum_of_rows:
            self.winner = self.o_symbol
            self.can_continue = False
        else:
            if 0 not in self.values:
                self.can_continue = False
            self.winner = "Draw"

