#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary

Attributes:
    BOARD_COLUMNS (Dict[int,str]): Dictionary linking column indices to letters.

        .. code-block::
          :name: `BOARD_COLUMNS` code block
          :linenos:
          :caption: ``BOARD_COLUMNS``.

          BOARD_COLUMNS = {0 : "a",
                           1 : "b",
                           2 : "c",
                           3 : "d",
                           4 : "e",
                           5 : "f",
                           6 : "g",
                           7 : "h"}

    PIECE_TYPES (List[str]): List containing all types of chess Piece(s).

        .. code-block::
          :name: `PIECE_TYPES` code block
          :linenos:
          :caption: ``PIECE_TYPES``.

          PIECE_TYPES = ["pawn",
                         "rook",
                         "knight",
                         "bishop",
                         "queen",
                         "king"]

    PLAYER_COLORS (List[str]): List containing all Player color(s).

        .. code-block::
          :name: `PLAYER_COLORS` code block
          :linenos:
          :caption: ``PLAYER_COLORS``.

          PLAYER_COLORS = ["black",
                           "white"]
"""


#==============================================================================
#       MISCELLANEOUS CONSTANT(s)
#==============================================================================
BOARD_COLUMNS = {0 : "a",
                 1 : "b",
                 2 : "c",
                 3 : "d",
                 4 : "e",
                 5 : "f",
                 6 : "g",
                 7 : "h"}


PLAYER_COLORS = ["black",
                 "white"]


PIECE_TYPES = ["pawn",
               "rook",
               "knight",
               "bishop",
               "queen",
               "king"]


NUM_COLS = 8
NUM_ROWS = 8
