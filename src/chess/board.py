#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""


import traceback

from typing import List

from .move import Move

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
        current_move_color (str): Description
        moves_log (list): Description

    """

    def __init__(self,
                 current_move_color : str = "white",
                 moves_log          : List[Move] = None,
                 pieces             : List[Piece] = None):
        """Summary

        Args:
            current_move_color (str, optional): Description
            moves_log (List[Move], optional): Description
            pieces (List[Piece], optional): Description
        """
        self._create_board()
        self._create_moves_log()

        if pieces is None:
            self._add_pieces_to_board("black")
            self._add_pieces_to_board("white")

        else:
            for piece in pieces:
                prow_idx = piece.row_idx
                pcol_idx = pieces.col_idx

                self.board[prow_idx][pcol_idx] = Square(col_idx=pcol_idx,
                                                        row_idx=prow_idx,
                                                        occupant=piece)

        if current_move_color not in ["black", "white"]:
            self.current_move_color = current_move_color

        if (moves_log is not None
            and all(isinstance(moov, Move)
                    for moov in moves_log)):
            self.moves_log = moves_log


    #==========================================================================
    #       OVERLOAD(S) FOR CLASS'S PYTHON MAGIC METHOD(s)
    #==========================================================================
    def __str__(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        self_str = "\n"

        try:
            for row_idx in range(NUM_ROWS):
                for col_idx in range(NUM_COLS):
                    sqr = self.board[row_idx][col_idx]
                    self_str += "[ ]" if sqr.is_empty() else str(sqr.occupant)
                    self_str += " "
                self_str += "\n"

        except (AttributeError, IndexError, KeyError, TypeError, ValueError):
            pass

        return self_str


    #==========================================================================
    #       PRIVATE INITIALIZATION METHOD(s)
    #==========================================================================
    def _add_pieces_to_board(self,
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


    def _create_moves_log(self):
        """Summary
        """
        self.moves_log = []

    #==========================================================================
    #       CALCULATE PIECE MOVEMENT METHOD(s)
    #==========================================================================
    def is_move_available(self,
                          piece : Piece,
                          move  : Move) -> bool:
        """Summary

        Args:
            piece (Piece): Description
            move (Move): Description

        Returns:
            bool: Description
        """
        is_valid = False

        try:
            is_valid = move in piece.available_moves

        except (AttributeError, TypeError, ValueError):
            pass

        return is_valid


    def move_piece_on_board(self,
                            piece : Piece,
                            move  : Move):
        """Summary

        Args:
            piece (Piece): Description
            move (Move): Description
        """
        try:
            # Moves the Piece on the Board.
            piece.past_moves += [move]
            self.board[move.before.row_idx][move.before.col_idx].occupant = None
            self.board[move.after.row_idx][move.after.col_idx].occupant = piece

        except (AttributeError, IndexError, KeyError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't move Piece on Board!\n")
            traceback.print_exc()


    def calculate_available_moves(self,
                                  piece : Piece) -> List[Move]:
        """Summary

        Returns:
            List[Move]: Description

        Args:
            piece (Piece): Description
        """

        def calculate_straight_line_moves() -> List[Move]:
            """Summary
            """

        def calculate_diagonal_moves() -> List[Move]:
            """Summary
            """



        def calculate_available_pawn_moves() -> List[Move]:
            """Summary
            """
            try:
                # Move forward two spaces only available first time Pawn moves.
                if not piece.has_moved():

                else:

                # Checks for Pawn targets immediately in front and diagonal.


                # Checks for an en passant Pawn target.

            except (AttributeError, TypeError, ValueError):
                print("\n// [ERROR]  Couldn't calculate available Pawn Move(s)!\n")
                traceback.print_exc()


        def calculate_available_rook_moves():
            """Summary
            """

        def calculate_available_knight_moves():
            """Summary
            """

        def calculate_available_bishop_moves():
            """Summary
            """

        def calculate_available_queen_moves():
            """Summary
            """

        def calculate_available_king_moves():
            """Summary
            """

        if isinstance(piece, Pawn):

        elif isinstance(piece, Rook):

        elif isinstance(piece, Knight):

        elif isinstance(piece, Bishop):

        elif isinstance(piece, Queen):

        elif isinstance(piece, King):


        #----------------------------------------------------------------------
        # Calculate all available moves public method implementation.
        #----------------------------------------------------------------------
        all_moves = []

        try:
            if isinstance(piece, Pawn):
                calculate_available_pawn_moves()

            elif isinstance(piece, Rook):
                calculate_available_rook_moves()

            elif isinstance(piece, Knight):
                calculate_available_knight_moves()

            elif isinstance(piece, Bishop):
                calculate_available_bishop_moves()

            elif isinstance(piece, Queen):
                calculate_available_queen_moves()

            elif isinstance(piece, King):
                calculate_available_king_moves()

        except (AttributeError, IndexError, KeyError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't calculate all available Move(s)!\n")
            traceback.print_exc()

        return all_moves
