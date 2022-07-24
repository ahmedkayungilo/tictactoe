from tictactoe import TicTacToe


game = TicTacToe()

game.draw_board()

while game.can_continue:
    game.play_move()
    game.check_winner()