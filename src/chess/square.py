#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary

Attributes:
    Sqr (TYPE): Description
"""


from typing import TypeVar

from .piece import Piece


Sqr = TypeVar("Sqr")


#==============================================================================
#      SQUARE OF A CHESS BOARD CLASS
#==============================================================================
class Square:
    """Summary

    Attributes:
        col_idx (TYPE): Description
        occupant (TYPE): Description
        row_idx (TYPE): Description
    """

    def __init__(self,
                 col_idx  : int,
                 row_idx  : int,
                 occupant : Piece = None):
        """Summary

        Args:
            col_idx (int): Description
            row_idx (int): Description
            occupant (Piece, optional): Description
        """
        self.__occupant = None

        self.col_idx = col_idx
        self.row_idx = row_idx

        self.occupant = occupant


    #==========================================================================
    #       PRIVATE PROPERTY(S) INTERFACE METHOD(s)
    #==========================================================================
    @property
    def occupant(self) -> Piece:
        """Summary

        Returns:
            Piece: Description
        """
        return self.__occupant


    @occupant.setter
    def occupant(self,
                 occupant : Piece):
        """Summary

        Args:
            occupant (Piece): Description
        """
        if isinstance(occupant, Piece) or occupant is None:
            self.__occupant = occupant


    #==========================================================================
    #       OVERLOAD(S) FOR CLASS'S PYTHON MAGIC METHOD(s)
    #==========================================================================
    def __eq__(self,
               other : Sqr) -> bool:
        """Summary

        Args:
            other (Sqr): Description

        Returns:
            bool: Description
        """
        is_eq = False

        try:
            is_eq = (self.col_idx == other.col_idx
                     and self.row_idx == other.row_idx)

        except (AttributeError, TypeError, ValueError):
            pass

        return is_eq


    def __str__(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        return "(" + str(self.row_idx) + "," + str(self.col_idx) + ")"
