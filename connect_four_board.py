# Rick Dionne
# August 2025

import numpy as np
from numpy.typing import NDArray
from typing import Tuple

class ConnectFourBoard:
    """Connect Four board class with class constants for:
     - horizontal dimension
     - vertical dimension
     - winning line length
     instance variables for:
     - starting player (Red or Yellow)
     - current turn (Red or Yellow)
     - piece layout (nested numpy array of ints, -1 for Red checkers, +1 for Yellow checkers, 0 for empty)
     and methods for:
     - playing a checker of the appropriate color for the current turn
     - checking if a player has won
     - checking if a stalemate has occurred
     - representing the board as a string
    """
    # standard Connect Four dimensions
    H_DIM = 7
    V_DIM = 6
    WINNING_LINE_LENGTH = 4

    def __init__(self, starting_player: int, current_player: int, board: NDArray[np.int8] = None):
        """Initializes a board
        :param starting_player: Red (-1) or Yellow (1)
        :param current_player: Red (-1) or Yellow (1)
        :param board: H_DIM by V_DIM nested np array of ints, None for empty board
        :return an instance of ConnectFourBoard
        :raises Exception: if parity is incorrect
        :raises TypeError: if board is not an np array of ints
        :raises ValueError: if board is not an H_DIM x V_DIM np array of ints
        """
        self.starting_player = starting_player
        self.current_player = current_player
        if board is not None:
            # check type of board
            if not isinstance(board, np.ndarray) or board.dtype != np.int8:
                raise TypeError("board must be an np array of ints")
            if board.shape[0] != ConnectFourBoard.H_DIM \
                    or board.shape[1] != ConnectFourBoard.V_DIM:
                raise ValueError("board must be H_DIM x V_DIM np array of ints")
            self.board = board
        else:
            self.board = np.zeros((self.H_DIM, self.V_DIM), np.int8)

        # check for parity: if it's the starting players turn -> even # of checkers
        total_checkers = int(np.sum(np.abs(self.board)))
        if self.starting_player == self.current_player and total_checkers % 2 != 0:
            raise Exception('Invalid board parity: odd')
        elif self.starting_player != self.current_player and total_checkers % 2 == 0:
            raise Exception('Invalid board parity: even')

        # check for piece balance
        # if current player was starting player, should be 0
        # else, if Red started balance should be -1, if Yellow, +1
        balance = int(np.sum(self.board))
        if self.starting_player == self.current_player and balance != 0:
            raise Exception('Invalid piece balance: Red and Yellow should have same number')
        elif self.starting_player == -1 and self.current_player != self.starting_player and balance != -1:
            raise Exception('Invalid board: Should be exactly one extra Red checker')
        elif self.starting_player == 1 and self.current_player != self.starting_player and balance != 1:
            raise Exception('Invalid board: Should be exactly one extra Yellow checker')

    def __str__(self) -> str:
        """String representation of ConnectFourBoard"""
        my_str = ""
        if self.starting_player < 0:
            my_str += "First to play: Red\n"
        else:
            my_str += "First to play: Yellow\n"
        if self.current_player < 0:
            my_str += "Currently playing: Red\n"
        else:
            my_str += "Currently playing: Yellow\n"
        flipped = np.flip(self.board,1)
        color_dict = {-1: "R", 0: "-", 1: "Y"}
        for v in range(ConnectFourBoard.V_DIM):
            my_str += str(ConnectFourBoard.V_DIM - v) + " "
            for h in range(ConnectFourBoard.H_DIM):
                my_str += color_dict[int(flipped[h][v])] + " "
            my_str += "\n"
        my_str += "  1 2 3 4 5 6 7\n"
        return my_str

    def check_winner(self, player: int) -> bool:
        """Checks if the indicated player has won
        :param player: Red (-1) or Yellow (1)
        :return True if player has won, False otherwise
        """
        for h_pos in range(self.H_DIM):
            for v_pos in range(self.V_DIM):
                if int(self.board[h_pos][v_pos]) == player:
                    # check vertical wins
                    length = 1
                    new_v_pos = v_pos + 1
                    while new_v_pos < self.V_DIM and length < self.WINNING_LINE_LENGTH \
                            and int(self.board[h_pos][new_v_pos]) == player:
                        length += 1
                        new_v_pos += 1
                    if length == self.WINNING_LINE_LENGTH:
                        return True
                    # check horizontal wins
                    length = 1
                    new_h_pos = h_pos + 1
                    while new_h_pos < self.H_DIM and length < self.WINNING_LINE_LENGTH \
                            and int(self.board[new_h_pos][v_pos]) == player:
                        length += 1
                        new_h_pos += 1
                    if length == self.WINNING_LINE_LENGTH:
                        return True
                    # check upward diagonal wins
                    length = 1
                    new_v_pos = v_pos + 1
                    new_h_pos = new_h_pos + 1
                    while new_v_pos < self.V_DIM and new_h_pos < self.H_DIM \
                        and length < self.WINNING_LINE_LENGTH and int(self.board[new_h_pos][new_v_pos]) == player:
                        length += 1
                        new_v_pos += 1
                        new_h_pos += 1
                    if length == self.WINNING_LINE_LENGTH:
                        return True
                    # check downward diagonal wins
                    length = 1
                    new_v_pos = v_pos - 1
                    new_h_pos = new_h_pos + 1
                    while new_v_pos >= 0 and new_h_pos < self.H_DIM \
                            and length < self.WINNING_LINE_LENGTH and int(self.board[new_h_pos][new_v_pos]) == player:
                        length += 1
                        new_v_pos -= 1
                        new_h_pos += 1
                    if length == self.WINNING_LINE_LENGTH:
                        return True
        return False

    def check_stalemate(self) -> bool:
        """Checks if the board is a stalemate, assuming neither player has won
        :return True if board is a stalemate, False otherwise
        """
        total_checkers = int(np.sum(np.abs(self.board)))
        if total_checkers == self.H_DIM * self.V_DIM:
            return True # a stalemate occurs when the board is full, with no winner
        return False

    def play_checker(self, col: int) -> Tuple[int, int]:
        """Plays a checker of the current player's color on the board
        :param col: the column to place the checker in
        :raises ValueError: if col is not within [1,H_DIM]
        :raises ValueError: if col is already full
        :return (col,height): the location of the newly placed checker
        """
        if col < 1 or col > ConnectFourBoard.H_DIM:
            raise ValueError("col must be in range [1, H_DIM]")
        height_to_place = 0
        while height_to_place < ConnectFourBoard.V_DIM and self.board[col-1][height_to_place] != 0:
            height_to_place += 1
        if height_to_place >= ConnectFourBoard.V_DIM:
            raise ValueError("col must not be full")
        self.board[col-1][height_to_place] = np.sign(self.current_player)
        return col, height_to_place
