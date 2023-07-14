from collections.abc import Callable
from sudoku import Board
from board_export.pdf_exporter import save_to_pdf
from board_export.txt_exporter import save_to_txt

formats: dict[str, Callable[[Board], None]] = {
    'pdf': save_to_pdf,
    'txt': save_to_txt
}