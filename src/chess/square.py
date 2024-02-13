#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary
"""

from .piece import Piece 

class Square:
	"""Summary
	"""

	def __init__(self,
				 col_idx : int,
				 row_idx : int,
				 occupant : Piece = None):
		"""Summary

		Args:
		    col_idx (int): Description
		    row_idx (int): Description
		    occupant (Piece, optional): Description
		"""

