#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summary

Attributes:
    Moov (TYPE): Description
    Sqr (TYPE): Description
"""


from typing import TypeVar


Moov = TypeVar("Moov")
Sqr = TypeVar('Sqr')


#==============================================================================
#       MOVE OF A CHESS PIECE CLASS
#==============================================================================
class Move:
    """Summary

    Attributes:
        after (TYPE): Description
        before (TYPE): Description
    """

    def __init__(self,
                 before : Sqr,
                 after  : Sqr):
        """Summary

        Args:
            before (Sqr): Description
            after (Sqr): Description
        """
        self.before = before
        self.after = after


    #==========================================================================
    #       OVERLOAD(S) FOR CLASS'S PYTHON MAGIC METHOD(s)
    #==========================================================================
    def __eq__(self,
               other : Moov) -> bool:
        """Summary

        Args:
            other (Moov): Description

        Returns:
            bool: Description
        """
        is_eq = False

        try:
            is_eq = (self.before == other.before
                     and self.after == other.after)

        except (AttributeError, TypeError, ValueError):
            pass

        return is_eq


    def __str__(self) -> str:
        """Summary

        Returns:
            str: Description
        """
        return str(self.before) + " -> " + str(self.after)
