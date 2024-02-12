#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""


import traceback

from abc import ABC, abstractmethod

from pathlib import Path
from typing import Dict

from .move import Move

from ..utils import BOARD_COLUMNS
from ..utils import PIECE_TYPES
from ..utils import PLAYER_COLORS


#==============================================================================
#       CHESS PIECE ABSTRACT BASE CLASS
#==============================================================================
class Piece(ABC):
    """Summary

    Attributes:
        col_idx (TYPE): Description
        past_moves (TYPE): Description
        piece_color (TYPE): Description
        piece_type (TYPE): Description
        row_idx (TYPE): Description
    """

    @abstractmethod
    def __init__(self,
                 col_idx      : int = None,
                 row_idx      : int = None,
                 past_moves   : List[Move] = [],
                 piece_color  : str = "white",
                 piece_name   : str = "pawn"):
        """Summary

        Args:
            col_idx (int, optional): Description
            row_idx (int, optional): Description
            past_moves (List[Move], optional): Description
            piece_color (str, optional): Description
            piece_name (str, optional): Description
        """
        self.__col_idx = None
        self.__row_idx = None

        self.__past_moves = []
        self.__piece_color = "white"
        self.__piece_type = "pawn"

        self.col_idx = col_idx
        self.row_idx = row_idx

        self.past_moves = past_moves
        self.piece_color = piece_color
        self.piece_type = piece_type


    #==========================================================================
    #       PROPERTY INTERFACE METHOD(s)
    #==========================================================================
    @property
    def col_idx(self) -> int:
        """Summary

        Returns:
            int: Description
        """
        return self.__col_idx


    @col_idx.setter
    def col_idx(self,
                col_idx : int):
        """Summary

        Args:
            col_idx (int): Description
        """
        if isinstance(col_idx, int) and 0 <= col_idx < 8:
            self.__col_idx = col_idx


    @property
    def row_idx(self) -> int:
        """Summary

        Returns:
            int: Description
        """
        return self.__row_idx


    @row_idx.setter
    def row_idx(self,
                row_idx : int):
        """Summary

        Args:
            row_idx (int): Description
        """
        if isinstance(row_idx, int) and 0 <= row_idx < 8:
            self.__row_idx = row_idx


    @property
    def past_moves(self) -> List[Move]:
        """Summary

        Returns:
            List[Move]: Description
        """
        return self.__past_moves


    @past_moves.setter
    def past_moves(self,
                   past_moves : List[Move]):
        """Summary

        Args:
            past_moves (List[Move]): Description
        """
        if all(isinstance(pmove, Move) for pmove in past_moves):
            self.__past_moves = past_moves


    @property
    def piece_color(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        return self.__piece_color


    @piece_color.setter
    def piece_color(self,
                    piece_color : str):
        """Summary

        Args:
            piece_color (str): Description
        """
        if piece_color in PLAYER_COLORS:
            self.__piece_color = piece_color


    @property
    def piece_type(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        return self.__piece_type


    @piece_type.setter
    def piece_type(self,
                   piece_type : str):
        """Summary

        Args:
            piece_type (str): Description
        """
        if piece_type in PIECE_TYPES:
            self.__piece_type = piece_type


    #==========================================================================
    #       PIECE REPRESENTATION METHOD(s)
    #==========================================================================
    def to_short_str(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        short_str = None

        try:
            short_str = piece_type[0].upper()

            if include_color:
                short_str = piece_color[0].upper() + short_str

        except (AttributeError, IndexError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't represent the Chess Piece as a short str!\n")
            traceback.print_exc()

        return short_str


#==============================================================================
#       ROOK CHESS PIECE CLASS
#==============================================================================
class Rook(Piece):
    """Summary
    """

    def __init__(self,
                 col_idx     : int,
                 row_idx     : int,
                 past_moves  : List[Move],
                 piece_color : str = "white"):
        """Summary

        Args:
            col_idx (int): Description
            row_idx (int): Description
            past_moves (List[Move]): Description
            piece_color (str, optional): Description
        """
        super().__init__(col_idx=col_idx,
                         row_idx=row_idx,
                         past_moves=past_moves,
                         piece_color=piece_color,
                         piece_type="rook")


#==============================================================================
#       KNIGHT CHESS PIECE CLASS
#==============================================================================
class Knight(Piece):
    """Summary
    """

    def __init__(self,
                 col_idx     : int,
                 row_idx     : int,
                 past_moves  : List[Move],
                 piece_color : str = "white"):
        """Summary

        Args:
            col_idx (int): Description
            row_idx (int): Description
            past_moves (List[Move]): Description
            piece_color (str, optional): Description
        """
        super().__init__(col_idx=col_idx,
                         row_idx=row_idx,
                         past_moves=past_moves,
                         piece_color=piece_color,
                         piece_type="knight")


#==============================================================================
#       BISHOP CHESS PIECE CLASS
#==============================================================================
class Bishop(Piece):
    """Summary
    """

    def __init__(self,
                 col_idx     : int,
                 row_idx     : int,
                 past_moves  : List[Move],
                 piece_color : str = "white"):
        """Summary

        Args:
            col_idx (int): Description
            row_idx (int): Description
            past_moves (List[Move]): Description
            piece_color (str, optional): Description
        """
        super().__init__(col_idx=col_idx,
                         row_idx=row_idx,
                         past_moves=past_moves,
                         piece_color=piece_color,
                         piece_type="bishop")


#==============================================================================
#       QUUEN CHESS PIECE CLASS
#==============================================================================
class Queen(Piece):
    """Summary
    """

    def __init__(self,
                 col_idx     : int,
                 row_idx     : int,
                 past_moves  : List[Move],
                 piece_color : str = "white"):
        """Summary

        Args:
            col_idx (int): Description
            row_idx (int): Description
            past_moves (List[Move]): Description
            piece_color (str, optional): Description
        """
        super().__init__(col_idx=col_idx,
                         row_idx=row_idx,
                         past_moves=past_moves,
                         piece_color=piece_color,
                         piece_type="queen")


#==============================================================================
#       KING CHESS PIECE CLASS
#==============================================================================
class King(Piece):
    """Summary
    """

    def __init__(self,
                 col_idx     : int,
                 row_idx     : int,
                 past_moves  : List[Move],
                 piece_color : str = "white"):
        """Summary

        Args:
            col_idx (int): Description
            row_idx (int): Description
            past_moves (List[Move]): Description
            piece_color (str, optional): Description
        """
        super().__init__(col_idx=col_idx,
                         row_idx=row_idx,
                         past_moves=past_moves,
                         piece_color=piece_color,
                         piece_type="king")

#==============================================================================
#       SCRIPT ENTRY POINT
#==============================================================================
if __name__ == "__main__":

    print(f"\n// [DEBUG]  Running File['{__file__}'] as __main__!\n")

    print("\n// [DEBUG]  All done, nothing to see here!\n")
