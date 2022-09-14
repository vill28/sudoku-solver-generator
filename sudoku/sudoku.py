from datetime import datetime
import random

from consistency import ConsistencyProvider
from consistency import ConsistencyFunction
from . import Cell, Board

class Sudoku:
    board: Board
    backtrack_count: int

    def __init__(self, board: Board = None) -> None:
        self.board = board
        self.backtrack_count = 0
        random.seed(datetime.now())

        if not board:
            self.board = Board()

    def solve(self, consistency_provider: ConsistencyProvider) -> bool:
        # maybe check if board is empty.. nothing to solve
        init_consistency = consistency_provider.get_init_consistency_funtion()
        consistency_function = consistency_provider.get_consistency_function()
        self.backtrack_count = 0

        if not init_consistency(self.board):
            return False

        if not self._backtrack(consistency_function):
            return False

        return True

    # generates sudoku puzzles for "human computers" (lol)
    def generate(self, consistency_provider: ConsistencyProvider, *, difficulty: float = .7) -> None:
        # most likely there would be more than 1 solution
        if difficulty > .79:
            difficulty = .79
        if difficulty < 0:
            difficulty = .1

        cells = self.board.get_unassigned_cells()
        consistency_fn = consistency_provider.get_consistency_function()
        random.shuffle(cells)
        
        for cell in cells[:9]:
            cell.assign_random(clear_domain=True)
            if not consistency_fn(cell, self.board):
                raise RuntimeError('Failed to generate sudoku puzzle')

        if not self._backtrack(consistency_fn):
            raise RuntimeError('Failed to generate sudoku puzzle')

        random.shuffle(cells)
        for i in range(round(81 * difficulty)):
            cells[i].reset()
    
    def is_solved(self) -> bool:
        for i in range(9):
            row = {cell.value for cell in self.board.cells[i]}
            if sum(row) != 45:
                return False

            col = {row[i].value for row in self.board.cells}
            if sum(col) != 45:
                return False
                
        for box_y in range(0, 9, 3):
            for box_x in range(0, 9, 3):
                box = set()

                for row in self.board.cells[box_y:box_y + 3]:
                    row = row[box_x:box_x + 3]
                    box.update([c.value for c in row])

                if sum(box) != 45:
                    return False
        return True

    def _select_mrv_cell(self) -> Cell:
        unassigned: list[Cell] = self.board.get_unassigned_cells()
        rv_sorted = sorted(unassigned, key = lambda cell: len(cell.domain))
        return rv_sorted[0]

    def _ordered_domain_values(self, cell: Cell) -> list[Cell]:
        if len(cell.domain) <= 1:
            return cell.domain

        def conflicts_count(value: int, cell: Cell):
            count: int = 0
            for n_cell in cell.neighbours:
                if not n_cell.value and value in n_cell.domain:
                    count += 1
            return count

        return sorted(cell.domain, key = lambda value: conflicts_count(value, cell))

    def _backtrack(self, consistency_fn: ConsistencyFunction) -> bool:
        if self.is_solved():
            return True

        cell = self._select_mrv_cell()
        for value in self._ordered_domain_values(cell):
            cell.value = value
            res, affected_cells = consistency_fn(cell, self.board)
            if res and self._backtrack(consistency_fn):
                return True

            self.backtrack_count += 1
            cell.value = 0
            for affected_cell in affected_cells:
                affected_cell.domain.append(value)

        return False
