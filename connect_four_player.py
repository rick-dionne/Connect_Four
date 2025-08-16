# Rick Dionne
# August 2025

from connect_four_board import ConnectFourBoard

class ConnectFourPlayer:
    """base class for Connect Four players"""
    def __init__(self):
        self.moves_made = []

    def choose_move(self, board: ConnectFourBoard) -> int:
        """makes the first legal move lexically
        :raises ValueError: if no legal move exists
        :returns: the column chosen"""
        for col in range(board.H_DIM):
            if board.board[col][board.V_DIM-1] == 0:
                self.moves_made.append(col)
                return col + 1
        raise ValueError("No legal move")

