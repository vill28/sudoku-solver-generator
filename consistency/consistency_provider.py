from typing import Callable
from abc import ABC, abstractmethod

from consistency import forward_check
from sudoku import Board, Cell
from . import forward_check

InitConsistencyFunction = Callable[[Board], bool]
ConsistencyFunction = Callable[[Cell, Board], tuple[bool, list[Cell]]]

class ConsistencyProvider(ABC):

    @abstractmethod
    def get_init_consistency_funtion(self) -> InitConsistencyFunction:
        """Returns initial consistency function"""
    
    @abstractmethod
    def get_consistency_function(self) -> ConsistencyFunction:
        """Returns consistency function"""

class ForwardCheck(ConsistencyProvider):

    def get_init_consistency_funtion(self) -> InitConsistencyFunction:
        return forward_check.init_consistency

    def get_consistency_function(self) -> ConsistencyFunction:
        return forward_check.fw_check
