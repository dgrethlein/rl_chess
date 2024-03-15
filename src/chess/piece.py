#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary

Attributes:
    PIECE_SHORT_STRS (TYPE): Description
"""


import traceback

from abc import ABC, abstractmethod

from pathlib import Path
from typing import List

from .move import Move

from ..utils import PIECE_TYPES
from ..utils import PLAYER_COLORS


PIECE_SHORT_STRS = {"pawn"   : "p",
                    "rook"   : "r",
                    "knight" : "n",
                    "bishop" : "b",
                    "queen"  : "q",
                    "king"   : "k"}


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
        piece_value (TYPE): Description
        row_idx (TYPE): Description
    """

    @abstractmethod
    def __init__(self,
                 col_idx          : int,
                 row_idx          : int,
                 past_moves       : List[Move] = None,
                 piece_color      : str = "white",
                 piece_type       : str = "pawn",
                 piece_value      : float = 1.0):
        """Summary

        Args:
            col_idx (int): Description
            row_idx (int): Description
            past_moves (List[Move], optional): Description
            piece_color (str, optional): Description
            piece_type (str, optional): Description
            piece_value (float, optional): Description
        """
        self.__col_idx = None
        self.__row_idx = None

        self.__available_moves = []
        self.__past_moves = []

        self.__piece_color = "white"
        self.__piece_type = "pawn"
        self.__piece_value = 1.0

        self.col_idx = col_idx
        self.row_idx = row_idx

        self.past_moves = past_moves

        self.piece_color = piece_color
        self.piece_type = piece_type
        self.piece_value = piece_value


    #==========================================================================
    #       PRIVATE PROPERTY(S) INTERFACE METHOD(s)
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
    def available_moves(self) -> List[Move]:
        """Summary

        Returns:
            List[Move]: Description
        """
        return self.__available_moves


    @available_moves.setter
    def available_moves(self,
                        available_moves : List[Move]):
        """Summary

        Args:
            available_moves (List[Move]): Description
        """
        if all(isinstance(pmove, Move) for pmove in available_moves):
            self.__available_moves = available_moves


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


    @property
    def piece_value(self) -> float:
        """Summary

        Returns:
            float: Description
        """
        return self.__piece_value


    @piece_value.setter
    def piece_value(self,
                    piece_value : float):
        """Summary

        Args:
            piece_value (float): Description
        """
        try:
            if 0.0 < piece_value <= 10E+7:
                self.piece_value = float(piece_value)

        except (AttributeError, TypeError, ValueError):
            pass


    #==========================================================================
    #       PIECE REPRESENTATION METHOD(s)
    #==========================================================================
    def to_short_str(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        return PIECE_SHORT_STRS[self.piece_type]


    @abstractmethod
    def to_unicode_char(self) -> str:
        """Summary
        """


    #==========================================================================
    #       PIECE MOVE HISTORY METHOD(s)
    #==========================================================================
    def has_moved(self) -> bool:
        """Summary

        Returns:
            bool: Description
        """
        moved = False

        try:
            moved = len(self.past_moves) > 0

        except (AttributeError, TypeError, ValueError):
            print("\n// [ERROR]  Couldn't determine if Piece has moved!\n")
            traceback.print_exc()

        return moved


    #==========================================================================
    #       PIECE REPRESENTATION METHOD(s)
    #==========================================================================
    def get_piece_texture_path(self,
                               assets_dir : Path = None,
                               image_size : int = 128) -> Path:
        """Summary

        Returns:
            Path: Description

        Args:
            assets_dir (Path, optional): Description
            image_size (int, optional): Description
        """
        text_path = None

        try:
            if image_size not in [80, 128]:
                image_size = 128

            if not (isinstance(assets_dir, Path) and assets_dir.is_dir()):
                assets_dir = Path(f"./assets/images/imgs-{image_size}px/")

            text_path = Path(assets_dir / f"{self.piece_color}_{self.piece_type}")

        except (AttributeError, TypeError, ValueError):
            print("\n// [ERROR]  Coulnd't get Piece texture file path!\n")
            traceback.print_exc()

        return text_path



#==============================================================================
#       PAWN CHESS PIECE CLASS
#==============================================================================
class Pawn(Piece):
    """Summary

    Attributes:
        did_en_passant (bool): Description
        dir (TYPE): Description
    """

    def __init__(self,
                 col_idx        : int,
                 row_idx        : int,
                 past_moves     : List[Move],
                 piece_color    : str = "white",
                 did_en_passant : bool = False):
        """Summary

        Args:
            col_idx (int): Description
            row_idx (int): Description
            past_moves (List[Move]): Description
            piece_color (str, optional): Description
            did_en_passant (bool, optional): Description
        """
        super().__init__(col_idx=col_idx,
                         row_idx=row_idx,
                         past_moves=past_moves,
                         piece_color=piece_color,
                         piece_type="pawn",
                         piece_value=1.0)

        self.dir = -1 if piece_color == "white" else 1

        self.did_en_passant = False
        if isinstance(did_en_passant, bool):
            self.did_en_passant = did_en_passant


    #==========================================================================
    #       PIECE REPRESENTATION METHOD(s)
    #==========================================================================
    def to_unicode_char(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        unicode_str = None

        try:
            # white pawn unicode (♙)
            if self.piece_color == "white":
                unicode_str = "\u2659"

            # black pawn unicode (♟)
            else:
                unicode_str = "\u265f"

        except (AttributeError, TypeError, ValueError):
            print(f"\n// [ERROR]  Couldn't convert the {self.__class__.__name__} "
                  " to a unicode string!\n")
            traceback.print_exc()

        return unicode_str



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
                         piece_type="rook",
                         piece_value=5.0)


    #==========================================================================
    #       PIECE REPRESENTATION METHOD(s)
    #==========================================================================
    def to_unicode_char(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        unicode_str = None

        try:
            # white rook unicode (♖)
            if self.piece_color == "white":
                unicode_str = "\u2656"

            # black rook unicode (♜)
            else:
                unicode_str = "\u265c"

        except (AttributeError, TypeError, ValueError):
            print(f"\n// [ERROR]  Couldn't convert the {self.__class__.__name__} "
                  " to a unicode string!\n")
            traceback.print_exc()

        return unicode_str


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
                         piece_type="knight",
                         piece_value=3.0)


    #==========================================================================
    #       PIECE REPRESENTATION METHOD(s)
    #==========================================================================
    def to_unicode_char(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        unicode_str = None

        try:
            # white knight unicode (♘)
            if self.piece_color == "white":
                unicode_str = "\u2658"

            # black knight unicode (♞)
            else:
                unicode_str = "\u265e"

        except (AttributeError, TypeError, ValueError):
            print(f"\n// [ERROR]  Couldn't convert the {self.__class__.__name__} "
                  " to a unicode string!\n")
            traceback.print_exc()

        return unicode_str


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
                         piece_type="bishop",
                         piece_value=3.001)


    #==========================================================================
    #       PIECE REPRESENTATION METHOD(s)
    #==========================================================================
    def to_unicode_char(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        unicode_str = None

        try:
            # white bishop unicode (♗)
            if self.piece_color == "white":
                unicode_str = "\u2657"

            # black bishop unicode (♝)
            else:
                unicode_str = "\u265d"

        except (AttributeError, TypeError, ValueError):
            print(f"\n// [ERROR]  Couldn't convert the {self.__class__.__name__} "
                  " to a unicode string!\n")
            traceback.print_exc()

        return unicode_str


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
                         piece_type="queen",
                         piece_value=9.0)


    #==========================================================================
    #       PIECE REPRESENTATION METHOD(s)
    #==========================================================================
    def to_unicode_char(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        unicode_str = None

        try:
            # white queen unicode (♕)
            if self.piece_color == "white":
                unicode_str = "\u2655"

            # black queen unicode (♛)
            else:
                unicode_str = "\u265b"

        except (AttributeError, TypeError, ValueError):
            print(f"\n// [ERROR]  Couldn't convert the {self.__class__.__name__} "
                  " to a unicode string!\n")
            traceback.print_exc()

        return unicode_str


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
                         piece_type="king",
                         piece_value=10000.0)


    #==========================================================================
    #       PIECE REPRESENTATION METHOD(s)
    #==========================================================================
    def to_unicode_char(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        unicode_str = None

        try:
            # white king unicode (♔)
            if self.piece_color == "white":
                unicode_str = "\u2654"

            # black king unicode (♚)
            else:
                unicode_str = "\u265a"

        except (AttributeError, TypeError, ValueError):
            print(f"\n// [ERROR]  Couldn't convert the {self.__class__.__name__} "
                  " to a unicode string!\n")
            traceback.print_exc()

        return unicode_str


#==============================================================================
#       SCRIPT ENTRY POINT
#==============================================================================
if __name__ == "__main__":

    print(f"\n// [DEBUG]  Running File['{__file__}'] as __main__!\n")

    print("\n// [DEBUG]  All done, nothing to see here!\n")
