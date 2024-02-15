#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""


import traceback

from .piece import Piece
from .piece import Pawn
from .piece import Rook
from .piece import Knight
from .piece import Bishop
from .piece import Queen
from .piece import King

from .square import Square


from ..utils import NUM_COLS
from ..utils import NUM_ROWS

from ..utils import PLAYER_COLORS


#==============================================================================
#      CHESS BOARD CLASS
#==============================================================================
class Board:

    """Summary

    Attributes:
        board (TYPE): Description

    Deleted Attributes:
        grid (TYPE): Description
    """

    def __init__(self):
        """Summary
        """
        self._create_board()
        self._add_pieces("black")
        self._add_pieces("white")


    #==========================================================================
    #       PRIVATE INITIALIZATION METHOD(s)
    #==========================================================================
    def _add_pieces(self,
                    color : str = "white"):
        """Summary

        Args:
            color (str, optional): Description

        Raises:
            ValueError: Description
        """
        try:
            pawn_row, other_row = (6,7) if color == "white" else (1,0)

            if color not in PLAYER_COLORS:
                raise ValueError("Improper color provided when adding Piece(s) to grid!")

            # Pawn(s)
            for col_idx in range(NUM_COLS):
                self.board[pawn_row][col_idx] = Square(col_idx=col_idx,
                                                       row_idx=pawn_row,
                                                       occupant=Pawn(col_idx,
                                                                     pawn_row,
                                                                     past_moves=[],
                                                                     piece_color=color))

            # Rook(s)
            self.board[other_row][0] = Square(col_idx=0,
                                              row_idx=other_row,
                                              occupant=Rook(col_idx=0,
                                                            row_idx=other_row,
                                                            past_moves=[],
                                                            piece_color=color))
            self.board[other_row][7] = Square(col_idx=7,
                                              row_idx=other_row,
                                              occupant=Rook(col_idx=7,
                                                            row_idx=other_row,
                                                            past_moves=[],
                                                            piece_color=color))

            # Knight(s)
            self.board[other_row][1] = Square(col_idx=1,
                                              row_idx=other_row,
                                              occupant=Knight(col_idx=1,
                                                              row_idx=other_row,
                                                              past_moves=[],
                                                              piece_color=color))
            self.board[other_row][6] = Square(col_idx=6,
                                              row_idx=other_row,
                                              occupant=Knight(col_idx=6,
                                                              row_idx=other_row,
                                                              past_moves=[],
                                                              piece_color=color))

            # Bishop(s)
            self.board[other_row][2] = Square(col_idx=2,
                                              row_idx=other_row,
                                              occupant=Bishop(col_idx=2,
                                                              row_idx=other_row,
                                                              past_moves=[],
                                                              piece_color=color))
            self.board[other_row][5] = Square(col_idx=5,
                                              row_idx=other_row,
                                              occupant=Bishop(col_idx=5,
                                                              row_idx=other_row,
                                                              past_moves=[],
                                                              piece_color=color))

            # Queen
            self.board[other_row][3] = Square(col_idx=3,
                                              row_idx=other_row,
                                              occupant=Queen(col_idx=3,
                                                             row_idx=other_row,
                                                             past_moves=[],
                                                             piece_color=color))

            # King
            self.board[other_row][4] = Square(col_idx=4,
                                              row_idx=other_row,
                                              occupant=King(col_idx=4,
                                                            row_idx=other_row,
                                                            past_moves=[],
                                                            piece_color=color))

        except (AttributeError, IndexError, KeyError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't add Piece(s) to Board's grid!\n")
            traceback.print_exc()


    def _create_board(self):
        """Summary
        """
        self.board = [[Square(col_idx,
                              row_idx) for col_idx in range(NUM_COLS)]
                      for row_idx in range(NUM_ROWS)]


    #==========================================================================
    #       SQUARE OCCUPANCY METHOD(s)
    #==========================================================================
