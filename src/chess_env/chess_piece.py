#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""


from abc import ABC, abstractmethod

from typing import Dict, List, Tuple


from ..utils import is_idx_in_range

from ..utils import PieceType
from ..utils import PlayerColor





class ChessPiece(ABC):
    """Summary

    Attributes:
        col_idx (TYPE): Description
        on_board (TYPE): Description
        piece_color (TYPE): Description
        piece_type (TYPE): Description
        row_idx (TYPE): Description
    """

    def __init__(self,
                 col_idx      : int = None,
                 row_idx      : int = None,
                 on_board     : bool = False,
                 piece_color  : PlayerColor = PlayerColor.white,
                 piece_type   : PieceType = PieceType.pawn):
        """Summary

        Args:
            col_idx (int, optional): Description
            row_idx (int, optional): Description
            on_board (bool, optional): Description
            piece_color (PlayerColor, optional): Description
            piece_type (PieceType, optional): Description
        """
        self.__col_idx = None
        self.__row_idx = None
        self.__on_board = False
        self.__piece_color = PlayerColor.white
        self.__piece_type = PieceType.pawn

        self.col_idx = col_idx
        self.row_idx = row_idx
        self.on_board = on_board
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
        try:
            if is_idx_in_range(col_idx):
                self.__col_idx = int(col_idx)

        except (AttributeError, TypeError, ValueError):
            pass


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
        try:
            if is_idx_in_range(row_idx):
                self.__row_idx = int(row_idx)

        except (AttributeError, TypeError, ValueError):
            pass


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



#==============================================================================
#       SCRIPT ENTRY POINT
#==============================================================================
if __name__ == "__main__":

    print(f"\n// [DEBUG]  Running File['{__file__}'] as __main__!\n")

    print("\n// [DEBUG]  All done, nothing to see here!\n")
