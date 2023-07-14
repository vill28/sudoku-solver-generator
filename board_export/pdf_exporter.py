from fpdf import FPDF
from sudoku import Board

def save_to_pdf(board: Board) -> None:
    pdf = FPDF()
    pdf.add_page()

    # default page dimensions
    PDF_WIDTH = 210
    PDF_HEIGHT = 297
    # default board dimensions
    BOARD_SIZE = 135
    GRID_SIZE = BOARD_SIZE / 3
    CELL_SIZE = GRID_SIZE / 3
    # board beginning coordinates
    X_0 = (PDF_WIDTH - BOARD_SIZE) / 2
    Y_0 = (PDF_HEIGHT - BOARD_SIZE) / 2

    # draw board
    pdf.set_line_width(0.8)
    pdf.line(X_0, Y_0, X_0 + BOARD_SIZE, Y_0)
    pdf.line(X_0, Y_0 + BOARD_SIZE, X_0 + BOARD_SIZE, Y_0 + BOARD_SIZE)
    pdf.line(X_0, Y_0, X_0, Y_0 + BOARD_SIZE)
    pdf.line(X_0 + BOARD_SIZE, Y_0, X_0 + BOARD_SIZE, Y_0 + BOARD_SIZE)
    
    # draw grid
    pdf.set_line_width(0.6)
    pdf.line(X_0, Y_0 + GRID_SIZE, X_0 + BOARD_SIZE, Y_0 + GRID_SIZE)
    pdf.line(X_0, Y_0 + 2*GRID_SIZE, X_0 + BOARD_SIZE, Y_0 + 2*GRID_SIZE)
    pdf.line(X_0 + GRID_SIZE, Y_0, X_0 + GRID_SIZE, Y_0 + BOARD_SIZE)
    pdf.line(X_0 + 2*GRID_SIZE, Y_0, X_0 + 2*GRID_SIZE, Y_0 + BOARD_SIZE)

    # draw cells
    pdf.set_line_width(0.4)
    for i in range(3):
        pdf.line(X_0, Y_0 + CELL_SIZE + i*GRID_SIZE, X_0 + BOARD_SIZE, Y_0 + CELL_SIZE + i*GRID_SIZE)
        pdf.line(X_0, Y_0 + 2*CELL_SIZE + i*GRID_SIZE, X_0 + BOARD_SIZE, Y_0 + 2*CELL_SIZE + i*GRID_SIZE)
        pdf.line(X_0 + CELL_SIZE + i*GRID_SIZE, Y_0, X_0 + CELL_SIZE + i*GRID_SIZE, Y_0 + BOARD_SIZE)
        pdf.line(X_0 + 2*CELL_SIZE + i*GRID_SIZE, Y_0, X_0 + 2*CELL_SIZE + i*GRID_SIZE, Y_0 + BOARD_SIZE)

    # insert the text inside cells
    pdf.set_font("Arial", 'B', size = 25)
    for i in range(9):
        pdf.set_xy(X_0 + CELL_SIZE / 3.5, Y_0 + i*CELL_SIZE + 0.7)
        for cell in board.cells[i]:
            cell_value = ' ' if cell.value == 0 else f'{cell.value}'
            pdf.cell(CELL_SIZE, CELL_SIZE, txt = cell_value, align = 'L')
        pdf.ln()
    
    # save the pdf with name .pdf
    pdf.output("./new_sudoku.pdf")