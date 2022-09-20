from sudoku import Board

def save_to_txt(board: Board) -> None:
    with open("./new_sudoku", "w") as f:
        for row in board.cells:
            for cell in row:
                f.write(f'{cell.value} ')                
            f.write('\n')
