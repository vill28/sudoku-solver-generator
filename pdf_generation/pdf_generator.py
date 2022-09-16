from fpdf import FPDF
from sudoku import Board

# default page dimensions
pdf_w = 210
pdf_h = 297

# default board dimensions
board_s = 135
grid_s = board_s / 3
cell_s = grid_s / 3

# board beginning coordinates
x0 = (pdf_w - board_s) / 2
y0 = (pdf_h - board_s) / 2

class PDF(FPDF):

    def __init__(self) -> None:
        FPDF.__init__(self)
        self.add_page()
        self.board()
        self.set_font("Arial", 'B', size = 25)

    def board(self) -> None:
        self.set_line_width(0.8)
        self.line(x0, y0, x0 + board_s, y0)
        self.line(x0, y0 + board_s, x0 + board_s, y0 + board_s)
        self.line(x0, y0, x0, y0 + board_s)
        self.line(x0 + board_s, y0, x0 + board_s, y0 + board_s)
        
        self.set_line_width(0.6)
        self.line(x0, y0 + grid_s, x0 + board_s, y0 + grid_s)
        self.line(x0, y0 + 2*grid_s, x0 + board_s, y0 + 2*grid_s)
        self.line(x0 + grid_s, y0, x0 + grid_s, y0 + board_s)
        self.line(x0 + 2*grid_s, y0, x0 + 2*grid_s, y0 + board_s)

        self.set_line_width(0.4)
        for i in range(3):
            self.line(x0, y0 + cell_s + i*grid_s, x0 + board_s, y0 + cell_s + i*grid_s)
            self.line(x0, y0 + 2*cell_s + i*grid_s, x0 + board_s, y0 + 2*cell_s + i*grid_s)
            self.line(x0 + cell_s + i*grid_s, y0, x0 + cell_s + i*grid_s, y0 + board_s)
            self.line(x0 + 2*cell_s + i*grid_s, y0, x0 + 2*cell_s + i*grid_s, y0 + board_s)


    def save_as_pdf(self , board: Board) -> None:
        # insert the text in pdf
        for i in range(9):
            self.set_xy(x0 + cell_s / 3.5, y0 + i*cell_s + 0.7)
            for cell in board.cells[i]:
                cell_value = ' ' if cell.value == 0 else f'{cell.value}'
                self.cell(cell_s, cell_s, txt = cell_value, align = 'L')
            self.ln()
      
        # save the pdf with name .pdf
        self.output("./new_sudoku.pdf")