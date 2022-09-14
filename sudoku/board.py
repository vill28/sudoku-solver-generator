from . import Cell

class Board:
    cells: list[list[Cell]]

    def __init__(self, board: list[list[int]] = None) -> None:
        self.cells = []

        if board:
            if len(board) != 9: raise ValueError('Invalid board size')

            for y, row in enumerate(board):
                if len(row) != 9: raise ValueError('Invalid board size')
                self.cells.append([Cell(x, y, value) for x, value in enumerate(row)])
            self._setup_neighbours()
            return

        for y in range(9):
            self.cells.append([Cell(x, y) for x in range(9)])

        self._setup_neighbours()

    def _setup_neighbours(self) -> None:
        for row in self.cells:
            for cell in row:
                cell.neighbours = self._get_neighbours(cell)
        
    def _get_neighbours(self, cell: Cell) -> list[Cell]:
        n_cells = [r[cell.x] for r in self.cells]
        n_cells += self.cells[cell.y]

        box_x, box_y = (cell.x // 3) * 3, (cell.y // 3) * 3
        for box_row in self.cells[box_y:box_y + 3]:
            n_cells += box_row[box_x:box_x + 3]

        return [c for c in n_cells if c is not cell]

    def get_unassigned_cells(self) -> list[Cell]:
        unassigned_cells: list[Cell] = []
        for row in self.cells:
            for cell in row:
                if not cell.value:
                    unassigned_cells.append(cell)

        return unassigned_cells

    def get_assigned_cells(self) -> list[Cell]:
        unassigned_cells: list[Cell] = []
        for row in self.cells:
            for cell in row:
                if cell.value:
                    unassigned_cells.append(cell)

        return unassigned_cells

    def print_board(self, plain=False) -> None:
        if plain:
            for row in self.cells:
                row = [f'{cell.value}' for cell in row]
                print(' '.join(row))
            return
        
        print('┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓')
        for i, row in enumerate(self.cells):
            if i % 3 == 0 and i != 0:
                print('┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫')

            for j, cell in enumerate(row):
                str_val = cell.value if cell.value else ' '
                if j % 3 == 0:
                    print(f'┃ {str_val}', end=' ')
                else:
                    print(f'│ {str_val}', end=' ')
            print('┃')
            
            if i % 3 != 2:
                print('┠───┼───┼───╂───┼───┼───╂───┼───┼───┨')
            
        print('┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛')
