# Rick Dionne
# August 2025

from connect_four_board import ConnectFourBoard
"""Connect Four game class supporting a game with standard rules and dimension 
"""
class ConnectFourGame:
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
        self.is_game_over = True if self.board.check_stalemate() else False
        self.winner = None

    def __str__(self):
        return str(self.board)

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
        self.is_game_over = self.board.check_stalemate()
        self.board.current_player *= -1
        self.current_player = self.player2 if self.board.current_player == self.player1 else self.player1
        return self.is_game_over