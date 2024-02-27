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
        pieces (list): Description

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
        try:
            if current_move_color not in ["black", "white"]:
                self.current_move_color = current_move_color

            self._create_board()
            self._create_moves_log()
            self._create_pieces_list()

            if pieces is None:
                self._add_pieces_to_board("black")
                self._add_pieces_to_board("white")

            elif (isinstance(pieces, List)
                  and all(isinstance(piece, Piece) for piece in pieces)):

                # Loading a Board from a list of a Piece(s).
                self.pieces = pieces

                for piece in self.pieces:
                    prow_idx = piece.row_idx
                    pcol_idx = pieces.col_idx
                    self.board[prow_idx][pcol_idx] = Square(col_idx=pcol_idx,
                                                            row_idx=prow_idx,
                                                            occupant=piece)

            if (moves_log is not None
                and all(isinstance(moov, Move)
                        for moov in moves_log)):
                self.moves_log = moves_log

        except (AttributeError, IndexError, KeyError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't initialize a Chess Board!\n")
            traceback.print_exc()


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

                self.pieces += [self.board[pawn_row][col_idx].occupant]

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
            self.pieces += [self.board[other_row][0].occupant]
            self.pieces += [self.board[other_row][7].occupant]


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
            self.pieces += [self.board[other_row][1].occupant]
            self.pieces += [self.board[other_row][6].occupant]

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
            self.pieces += [self.board[other_row][2].occupant]
            self.pieces += [self.board[other_row][5].occupant]


            # Queen
            self.board[other_row][3] = Square(col_idx=3,
                                              row_idx=other_row,
                                              occupant=Queen(col_idx=3,
                                                             row_idx=other_row,
                                                             past_moves=[],
                                                             piece_color=color))
            self.pieces += [self.board[other_row][3].occupant]


            # King
            self.board[other_row][4] = Square(col_idx=4,
                                              row_idx=other_row,
                                              occupant=King(col_idx=4,
                                                            row_idx=other_row,
                                                            past_moves=[],
                                                            piece_color=color))
            self.pieces += [self.board[other_row][4].occupant]

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


    def _create_pieces_list(self):
        """Summary
        """
        self.pieces = []


    #==========================================================================
    #       DETERMINE KING IN CHECK METHOD(s)
    #==========================================================================

    #==========================================================================
    #       DETERMINE KING IN CHECK METHOD(s)
    #==========================================================================
    def is_current_king_in_check(self) -> bool:
        """Summary

        Returns:
            bool: Description
        """
        in_check = False

        try:
            other_color = "black" if self.current_move_color == "white" else "white"

            current_king = None
            other_pieces = []
            for piece in self.pieces:
                if piece.piece_color == other_color:
                    other_pieces += [piece]

                elif isinstance(piece, King):
                    current_king = piece

            current_king_square = Square(col_idx=current_king.col_idx,
                                         row_idx=current_king.row_idx,
                                         occupant=current_king)

            # Determines whether any of the other team's Piece(s) can
            # move to the space occupied by the current turn team's King.
            for other_piece in other_pieces:
                other_piece_square = Square(col_idx=other_piece.col_idx,
                                            row_idx=other_piece.row_idx,
                                            occupant=other_piece)

                other_piece_check_move = Move(before=other_piece_square,
                                              after=current_king_square)

                # If move is possible, indicate the current team's King is in check.
                if self.is_move_available(piece=other_piece,
                                          move=other_piece_check_move):
                    in_check = True
                    break

        except (AttributeError, IndexError, KeyError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't determine if King is in check!\n")
            traceback.print_exc()

        return in_check


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
            if self.is_move_available(piece, move):

                # Takes Piece off of Board's list of Piece(s).
                self.pieces.remove(piece)

                # Update's Piece's internal memory of Move(s).
                piece.past_moves += [move]
                piece.row_idx = move.after.row_idx
                piece.col_idx = move.after.col_idx

                # Moves the Piece on the Board.
                self.board[move.before.row_idx][move.before.col_idx].occupant = None
                self.board[move.after.row_idx][move.after.col_idx].occupant = piece

                # Puts Piece back in Board's list of Piece(s).
                self.pieces += [piece]
                self.moves_log += [move]

        except (AttributeError, IndexError, KeyError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't move Piece on Board!\n")
            traceback.print_exc()


    def compute_piece_available_moves(self,
                                      piece : Piece) -> List[Move]:
        """Summary

        Args:
            piece (Piece): Description

        Returns:
            List[Move]: Description
        """

        def compute_pawn_available_moves(piece : Piece) -> List[Move]:
            """Summary

            Args:
                piece (Piece): Description

            Returns:
                List[Move]: Description
            """
            pawn_moves = []

            try:
                pawn_row = piece.row_idx
                pawn_col = piece.col_idx

                # Determine whether Pawn can move forward one Square.
                if self.board[pawn_row + piece.dir][pawn_col].is_empty():
                    pawn_moves += [Move(before=self.board[pawn_row][pawn_col],
                                        after=self.board[pawn_row + piece.dir][pawn_col])]

                    # Determine whether Pawn can move forward two Square(s).
                    if (not piece.has_moved()
                        and self.board[pawn_row + 2 * piece.dir][pawn_col].is_empty()):

                        pawn_moves += [Move(before=self.board[pawn_row][pawn_col],
                                            after=self.board[pawn_row + 2 * piece.dir][pawn_col])]

                # Determines whether Pawn can move diagonally forward one Square (capture a Piece).
                diag_cols = list(
                                filter(
                                    lambda col_idx:
                                        0 <= col_idx <= 7,
                                        [pawn_col - 1, pawn_col + 1]
                                    )
                                )
                for dcol in diag_cols:
                    dsqr = self.board[pawn_row + piece.dir][dcol]

                    # Checks for standard diagonal capture (requires enemy piece).
                    if dsqr.is_occupied_by_rival_piece(color=pawn.piece_color):
                        pawn_moves += [Move(before=self.board[pawn_row][pawn_col],
                                            after=dsqr)]

                    # Checks for en passant capture. Looks for a Pawn in the square horizontally
                    # next to the given Pawn that has only moved once, two squares, and that Move
                    # was the last Move recorded by the Board.
                    elif (dsqr.is_empty()
                          and self.board[pawn_row][dcol].occupant.piece_color != piece.piece_color
                          and isinstance(self.board[pawn_row][dcol].occupant, Pawn)
                          and len(self.board[pawn_row][dcol].occupant.past_moves) == 1):

                        last_move = self.past_moves[-1]
                        last_opawn_move = self.board[pawn_row][dcol].occupant.past_moves[-1]

                        last_del_row = abs(last_opawn_move.before.row_idx
                                           - last_opawn_move.after.row_idx)

                        if last_move == last_opawn_move and last_del_row == 2:

                            pawn_moves += [Move(before=self.board[pawn_row][pawn_col],
                                                after=dsqr)]

            except (AttributeError, IndexError, KeyError, TypeError, ValueError):
                print("\n// [ERROR]  Couldn't compute the available Move(s) for a Pawn!\n")
                traceback.print_exc()

            return pawn_moves


        def compute_rook_available_moves(piece : Piece) -> List[Move]:
            """Summary

            Args:
                piece (Piece): Description

            Returns:
                List[Move]: Description
            """
            rook_moves = []

            try:
                # Grabs the Board coordinates of the Rook.
                rcol = piece.col_idx
                rrow = piece.row_idx

                # Examines potential moves in 4 directions.
                dir_moves = {"up"    : {"open"  : True,
                                        "moves" : []},
                             "down"  : {"open"  : True,
                                        "moves" : []},
                             "left"  : {"open"  : True,
                                        "moves" : []},
                             "right" : {"open"  : True,
                                        "moves" : []}}

                # Expands outwards in 4 directions from the Rook looking for Move(s).
                for radius in range(1,8):

                    # "Up" Move(s)
                    if 0 <= rrow - radius <= 7 and dir_moves["up"]["open"]:
                        if self.board[rrow - radius][rcol].is_empty():
                            dir_moves["up"]["moves"] += [Move(self.board[rrow][rcol],
                                                              self.board[rrow - radius][rcol])]

                        elif self.board[rrow - radius][rcol].is_occupied_by_rival_piece():
                            dir_moves["up"]["open"] = False
                            dir_moves["up"]["moves"] += [Move(self.board[rrow][rcol],
                                                              self.board[rrow - radius][rcol])]
                    else:
                        dir_moves["up"]["open"] = False

                    # "Down" Move(s)
                    if 0 <= rrow + radius <= 7 and dir_moves["down"]["open"]:
                        if self.board[rrow + radius][rcol].is_empty():
                            dir_moves["down"]["moves"] += [Move(self.board[rrow][rcol],
                                                                self.board[rrow + radius][rcol])]

                        elif self.board[rrow + radius][rcol].is_occupied_by_rival_piece():
                            dir_moves["down"]["open"] = False
                            dir_moves["down"]["moves"] += [Move(self.board[rrow][rcol],
                                                                self.board[rrow + radius][rcol])]
                    else:
                        dir_moves["down"]["open"] = False

                    # "Left" Move(s)
                    if 0 <= rcol - radius <= 7 and dir_moves["left"]["open"]:
                        if self.board[rrow][rcol - radius].is_empty():
                            dir_moves["left"]["moves"] += [Move(self.board[rrow][rcol],
                                                                self.board[rrow][rcol - radius])]

                        elif self.board[rrow][rcol - radius].is_occupied_by_rival_piece():
                            dir_moves["left"]["open"] = False
                            dir_moves["left"]["moves"] += [Move(self.board[rrow][rcol],
                                                                self.board[rrow][rcol - radius])]
                    else:
                        dir_moves["left"]["open"] = False


                    # "Right" Move(s)
                    if 0 <= rcol + radius <= 7 and dir_moves["right"]["open"]:
                        if self.board[rrow][rcol + radius].is_empty():
                            dir_moves["right"]["moves"] += [Move(self.board[rrow][rcol],
                                                                 self.board[rrow][rcol + radius])]

                        elif self.board[rrow][rcol + radius].is_occupied_by_rival_piece():
                            dir_moves["right"]["open"] = False
                            dir_moves["right"]["moves"] += [Move(self.board[rrow][rcol],
                                                                 self.board[rrow][rcol + radius])]

                # Concatenate all moves for the Rook together in a single list.
                for _, dir_dict in dir_moves.items():
                    rook_moves += dir_dict["moves"]

            except (AttributeError, IndexError, KeyError, TypeError, ValueError):
                print("\n// [ERROR]  Couldn't compute the available Move(s) for a Rook!\n")
                traceback.print_exc()

            return rook_moves



        def compute_knight_available_moves(piece : Piece) -> List[Move]:
            """Summary

            Args:
                piece (Piece): Description

            Returns:
                List[Move]: Description
            """
            knight_moves = []

            try:
                krow = piece.row_idx
                kcol = piece.col_idx
                ksqr = self.board[krow][kcol]

                # Anticipated geometry of movement for a Knight (clockwise).
                relative_moves = [(1, 2),
                                  (2, 1),
                                  (2, -1),
                                  (1, -2),
                                  (-1, -2),
                                  (-2, -1),
                                  (-2, 1),
                                  (-1, 2)]

                for (rel_row, rel_col) in relative_moves:

                    # Only include as available Move if target is on the Board.
                    if (0 <= krow + rel_row <= 7
                        and 0 <= kcol + rel_col <= 7):

                        knight_moves += [Move(before=ksqr,
                                              after=self.board[krow + rel_row][kcol + rel_col])]

            except (AttributeError, IndexError, KeyError, TypeError, ValueError):
                print("\n// [ERROR]  Couldn't compute the avilable Move(s) for a Knight!\n")
                traceback.print_exc()

            return knight_moves


        def compute_bishop_available_moves(piece : Piece) -> List[Move]:
            """Summary

            Args:
                piece (Piece): Description

            Returns:
                List[Move]: Description
            """
            bishop_moves = []


            return bishop_moves



        def compute_queen_available_moves(piece : Piece) -> List[Move]:
            """Summary

            Args:
                piece (Piece): Description

            Returns:
                List[Move]: Description
            """
            queen_moves = []


            return queen_moves


        def compute_king_available_moves(piece : Piece) -> List[Move]:
            """Summary

            Args:
                piece (Piece): Description

            Returns:
                List[Move]: Description
            """
            king_moves = []


            return king_moves


        available_moves = []

        try:
            if isinstance(piece, Pawn):
                available_moves = compute_pawn_available_moves(piece)

            elif isinstance(piece, Rook):
                available_moves = compute_rook_available_moves(piece)

            elif isinstance(piece, Knight):
                available_moves = compute_knight_available_moves(piece)

            elif isinstance(piece, Bishop):
                available_moves = compute_bishop_available_moves(piece)

            elif isinstance(piece, Queen):
                available_moves = compute_queen_available_moves(piece)

            elif isinstance(piece, King):
                available_moves = compute_king_available_moves(piece)

        except (AttributeError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't compute the Piece's available moves!\n")
            traceback.print_exc()

        return available_moves


