from sudoku import Cell, Board

def fw_check(cell: Cell, _: Board) -> tuple[bool, list[Cell]]:
    affected: list[Cell] = []
    for n_cell in cell.neighbours:
        if not n_cell.value and cell.value in n_cell.domain:
            n_cell.domain.remove(cell.value)
            affected.append(n_cell)

            if not n_cell.domain:
                return False, affected

    return True, affected

def init_consistency(board: Board) -> bool:
    assigned_cells: list[Cell] = board.get_assigned_cells()

    for cell in assigned_cells:
        res, _ = fw_check(cell, board)
        if not res:
            return False

    return True