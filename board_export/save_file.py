from board_export.pdf_exporter import save_to_pdf
from board_export.txt_exporter import save_to_txt

formats: dict[str, callable] = {
    'pdf': save_to_pdf,
    'txt': save_to_txt
}