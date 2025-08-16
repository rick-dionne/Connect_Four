# Rick Dionne
# August 2025

from connect_four_board import ConnectFourBoard

class ConnectFourGame:
    """Connect Four game class supporting a game with standard rules and dimension"""

    def __init__(self, player1, player2, red_starts: bool = True, initial_board: ConnectFourBoard = None):
        self.player1 = player1
        self.player2 = player2
        if initial_board is not None:
            self.board = initial_board
            self.current_player = self.player1 if self.board.current_player < 1 else self.player2
        else:
            starting_player_num = -1 if red_starts else 1
            self.current_player = self.player1 if red_starts else self.player2
            self.board = ConnectFourBoard(starting_player_num, starting_player_num)

        self.checkers_placed = []
        self.winner = None
        if self.board.check_winner(-1):
            self.game_over = True
            self.winner = self.player1
        elif self.board.check_winner(1):
            self.game_over = True
            self.winner = self.player2
        else:
            self.is_game_over = True if self.board.check_stalemate() else False

    def __str__(self):
        my_str = "Game between {} (Red) and {} (Yellow):\n".format(self.player1, self.player2)
        my_str += "Turn {}\n".format(len(self.checkers_placed) + 1)
        if self.is_game_over:
            my_str += "Game over: "
            if self.winner is not None:
                my_str += str(self.winner) + " wins\n"
            else:
                my_str += "stalemate\n"
        my_str += str(self.board)
        return my_str

    def make_move(self) -> bool:
        """have the current player make a move
        :raises Exception: if the game is already over
        :returns True if the move ended the game, False otherwise.
        """
        if self.is_game_over:
            raise Exception('Game already over')
        move_made = False
        (col,height) = (0,0)
        while not move_made:
            try:
                col_to_play = self.current_player.choose_move(self.board)
                col,height = self.board.play_checker(col_to_play)
                move_made = True
            except ValueError as e:
                print(e)
        self.checkers_placed.append((col,height))
        self.is_game_over = self.board.check_winner(-1) if self.current_player == self.player1 \
            else self.board.check_winner(1)
        if self.is_game_over:
            self.winner = self.current_player
        if not self.is_game_over:
            self.is_game_over = self.board.check_stalemate()
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        self.board.switch_current_player()
        return self.is_game_over