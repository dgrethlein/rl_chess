#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""


import traceback

from typing import Dict

from .chess_piece import ChessPiece 

from ..utils import PieceType
from ..utils import PlayerColor


#==============================================================================
#       PAWN CHESS PIECE CLASS
#==============================================================================
class Pawn(ChessPiece):
    """Summary
    """

    def __init__(self,
                 col_idx     : int,
                 row_idx     : int,
                 has_moved   : bool = False,
                 on_board    : bool = False,
                 piece_color : PlayerColor = PlayerColor.WHITE):
        """Summary

        Args:
            col_idx (int): Description
            row_idx (int): Description
            has_moved (bool, optional): Description
            on_board (bool, optional): Description
            piece_color (PlayerColor, optional): Description
        """
        super().__init__(col_idx=col_idx,
                         row_idx=row_idx,
                         has_moved=has_moved,
                         on_board=on_board,
                         piece_color=piece_color,
                         piece_type=PieceType.PAWN)


    #==========================================================================
    #       CLASS FACTORY METHOD(s)
    #==========================================================================
    @classmethod
    def from_dict(cls,
                  piece_dict : Dict):
        """Summary

        Args:
            piece_dict (Dict): Description

        Returns:
            TYPE: Description
        """
        return cls(col_idx=piece_dict.get("col_idx"),
                   row_idx=piece_dict.get("row_idx"),
                   has_moved=piece_dict.get("has_moved"),
                   on_board=piece_dict.get("on_board"),
                   piece_color=piece_dict.get("piece_color"))


#==============================================================================
#       SCRIPT ENTRY POINT
#==============================================================================
if __name__ == "__main__":

    print(f"\n// [DEBUG]  Running File['{__file__}'] as __main__!\n")

    print("\n// [DEBUG]  All done, nothing to see here!\n")
