#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""


import traceback

from abc import ABC, abstractmethod

from typing import Dict, List, Tuple


from ..utils import is_idx_in_range

from ..utils import PieceType
from ..utils import PlayerColor



class ChessPiece(ABC):
    """Summary

    Attributes:
        col_idx (TYPE): Description
        has_moved (TYPE): Description
        on_board (TYPE): Description
        piece_color (TYPE): Description
        piece_type (TYPE): Description
        row_idx (TYPE): Description
    """

    def __init__(self,
                 col_idx      : int = None,
                 row_idx      : int = None,
                 has_moved    : bool = False,
                 on_board     : bool = False,
                 piece_color  : PlayerColor = PlayerColor.WHITE,
                 piece_type   : PieceType = PieceType.PAWN):
        """Summary

        Args:
            col_idx (int, optional): Description
            row_idx (int, optional): Description
            has_moved (bool, optional): Description
            on_board (bool, optional): Description
            piece_color (PlayerColor, optional): Description
            piece_type (PieceType, optional): Description
        """
        self.__col_idx = None
        self.__row_idx = None
        self.__has_moved = False
        self.__on_board = False
        self.__piece_color = PlayerColor.WHITE
        self.__piece_type = PieceType.PAWN

        self.col_idx = col_idx
        self.row_idx = row_idx
        self.has_moved = has_moved
        self.on_board = on_board
        self.piece_color = piece_color
        self.piece_type = piece_type


    #==========================================================================
    #       CLASS FACTORY METHOD(s)
    #==========================================================================
    @classmethod
    @abstractmethod
    def from_dict(cls,
                  piece_dict : Dict):
        """Summary

        Args:
            piece_dict (Dict): Description
        """

    #==========================================================================
    #       CLASS SERIALIZATION METHOD(s)
    #==========================================================================
    @abstractmethod
    def to_dict(self) -> Dict:
        """Summary

        Returns:
            Dict: Description
        """
        return {"col_idx"     : self.col_idx,
                "row_idx"     : self.row_idx,
                "has_moved"   : self.has_moved,
                "on_board"    : self.on_board,
                "piece_color" : self.piece_color,
                "piece_type"  : self.piece_type}


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
        if is_idx_in_range(col_idx):
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
        if is_idx_in_range(row_idx):
            self.__row_idx = row_idx


    @property
    def has_moved(self) -> bool:
        """Summary

        Returns:
            bool: Description
        """
        return self.__has_moved


    @has_moved.setter
    def has_moved(self,
                  has_moved : bool):
        """Summary

        Args:
            has_moved (bool): Description
        """
        if isinstance(has_moved, bool):
            self.__has_moved = has_moved


    @property
    def on_board(self) -> bool:
        """Summary

        Returns:
            bool: Description
        """
        return self.__on_board


    @on_board.setter
    def on_board(self,
                 on_board : bool):
        """Summary

        Args:
            on_board (bool): Description
        """
        if isinstance(on_board, bool):
            self.__on_board = on_board


    @property
    def piece_color(self) -> PlayerColor:
        """Summary

        Returns:
            PlayerColor: Description
        """
        return self.__piece_color


    @piece_color.setter
    def piece_color(self,
                    piece_color : PlayerColor):
        """Summary

        Args:
            piece_color (PlayerColor): Description
        """
        if isinstance(piece_color, PlayerColor):
            self.__piece_color = piece_color


    @property
    def piece_type(self) -> PieceType:
        """Summary

        Returns:
            PieceType: Description
        """
        return self.__piece_type


    @piece_type.setter
    def piece_type(self,
                   piece_type : PieceType):
        """Summary

        Args:
            piece_type (PieceType): Description
        """
        if isinstance(piece_type, PieceType):
            self.__piece_type = piece_type


    #==========================================================================
    #       PIECE MOVEMENT METHOD(s)
    #==========================================================================
    def move_piece(self,
                   dest_col_idx : int,
                   dest_row_idx : int):
        """Summary

        Args:
            dest_col_idx (int): Description
            dest_row_idx (int): Description
        """
        try:
            self.col_idx = dest_col_idx
            self.row_idx = dest_row_idx

            if self.col_idx == dest_col_idx and self.row_idx == dest_row_idx:


            if not self.has_moved:
                self.has_moved = True

        except (AttributeError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't move ChessPiece!\n")
            traceback.print_exc()


#==============================================================================
#       SCRIPT ENTRY POINT
#==============================================================================
if __name__ == "__main__":

    print(f"\n// [DEBUG]  Running File['{__file__}'] as __main__!\n")

    print("\n// [DEBUG]  All done, nothing to see here!\n")