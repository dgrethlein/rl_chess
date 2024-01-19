#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""


import traceback

from enum import Enum


class PlayerColor(Enum):
    """Summary

    Attributes:
        black (int): Description
        white (int): Description
    """

    white = 1
    black = 2


class PieceType(Enum):
    """Summary

    Attributes:
        bishop (int): Description
        king (int): Description
        knight (int): Description
        pawn (int): Description
        queen (int): Description
        rook (int): Description
    """

    pawn = 1
    rook = 2
    knight = 3
    bishop = 4
    queen = 5
    king = 6



def is_idx_in_range(int_val : int,
                    num_idx : int = 8) -> bool:
    """Summary

    Args:
        int_val (int): Description
        num_idx (int, optional): Description

    Returns:
        TYPE: Description
    """
    in_range = False

    try:
        in_range = (0 <= int(int_val) < num_idx)

    except (AttributeError, TypeError, ValueError):
        pass

    return in_range


#==============================================================================
#       SCRIPT ENTRY POINT
#==============================================================================
if __name__ == "__main__":

    print(f"\n// [DEBUG]  Running File['{__file__}'] as __main__!\n")

    print("\n// [DEBUG]  All done, nothing to see here!\n")

