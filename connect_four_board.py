# Rick Dionne
# August 2025
"""Connect Four board class with class constants for:
 - horizontal dimension
 - vertical dimension
 - winning line length
 instance variables for:
 - starting player (Red or Yellow)
 - current turn (Red or Yellow)
 - piece layout (nested array of ints, -1 for Red checkers, +1 for Yellow checkers, 0 for empty)
 and methods for:
 - playing a checker of the appropriate color for the current turn
 - checking if a player has won
"""
import numpy as np
from numpy.typing import NDArray


class ConnectFourBoard:
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
        total_checkers = np.sum(np.abs(self.board))
        if self.starting_player == self.current_player and total_checkers % 2 != 0:
            raise Exception('Invalid board parity')
        elif total_checkers % 2 == 0:
            raise Exception('Invalid board parity')

    def check_winner(self, player: int) -> bool:
        """Checks if the indicated player has won
        :param player: Red (-1) or Yellow (1)
        :return True if player has won, False otherwise
        """
        pass # TODO: implement function

    def play_checker(self, col: int) -> None:
        """Plays a checker of the current player's color on the board
        :param col: the column to place the checker in
        :raises ValueError: if col is not within [0,H_DIM-1]
        :raises ValueError: if col is already full
        """
        pass # TODO: implement function
