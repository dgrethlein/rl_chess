#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""


import traceback

from enum import Enum
from typing import List, Union

import numpy as np



#==============================================================================
#       CHESS PIECE TYPE ENUMERATED CLASS
#==============================================================================
class PieceType(Enum):
    """Summary

    Attributes:
        BISHOP (int): Description
        bishop (int): Description
        KING (int): Description
        king (int): Description
        KNIGHT (int): Description
        knight (int): Description
        PAWN (int): Description
        pawn (int): Description
        QUEEN (int): Description
        queen (int): Description
        ROOK (int): Description
        rook (int): Description
    """
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6

    pawn = 1
    rook = 2
    knight = 3
    bishop = 4
    queen = 5
    king = 6


#==============================================================================
#       PLAYER COLOR ENUMERATED CLASS
#==============================================================================
class PlayerColor(Enum):
    """Summary

    Attributes:
        BLACK (int): Description
        black (int): Description
        WHITE (int): Description
        white (int): Description
    """
    WHITE = 1
    BLACK = 2

    white = 1
    black = 2


#==============================================================================
#       MISCELLANEOUS INDEX CHECKING FUNCTION(s)
#==============================================================================
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
