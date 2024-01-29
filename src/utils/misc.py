#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""


import traceback

from enum import Enum


class PieceType(Enum):
    """Summary

    Attributes:
        BISHOP (int): Description
        KING (int): Description
        KNIGHT (int): Description
        PAWN (int): Description
        QUEEN (int): Description
        ROOK (int): Description
    """

    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6


class PlayerColor(Enum):
    """Summary

    Attributes:
        BLACK (int): Description
        WHITE (int): Description
    """

    WHITE = 1
    BLACK = 2






def is_idx_in_range(int_val : int,
                    num_idx : int = 8) -> bool:
    """Summary

    Args:
        int_val (int): Description
        num_idx (int, optional): Description

    Returns:
        bool: Description
    """
    in_range = False

    try:
        in_range = (isinstance(int_val, int)
                    and 0 <= int_val < num_idx)

    except (AttributeError, TypeError, ValueError):
        pass

    return in_range


#==============================================================================
#       SCRIPT ENTRY POINT
#==============================================================================
if __name__ == "__main__":

    print(f"\n// [DEBUG]  Running File['{__file__}'] as __main__!\n")

    print("\n// [DEBUG]  All done, nothing to see here!\n")

