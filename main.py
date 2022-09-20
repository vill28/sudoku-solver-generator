import argparse, sys
from typing import TextIO

from sudoku import Board, Sudoku
from consistency import ForwardCheck
from board_export import save_file

def read_board(file: TextIO) -> list[list[int]]:
    lines = [line.strip().split() for line in file.readlines()]
    lines = [list(map(int, line)) for line in lines if line]
    return lines

def load_board(file_path: str) -> list[list[int]]:
    if file_path:
        with open(file_path, 'r') as file:
            return read_board(file)
    return read_board(sys.stdin)

def main() -> int:
    arg_parser = argparse.ArgumentParser(description='Sudoku solver/generator')
    arg_parser.add_argument('-c', '--count', action='store_true', help='Print backtrack count')
    arg_parser.add_argument('-p', '--plain', action='store_true', help='Print plain board')
    arg_parser.add_argument('-e', '--export', type=str, action='store', help='Export board to file', nargs='?', const='txt', metavar='FILE_TYPE')
    
    mode_group = arg_parser.add_mutually_exclusive_group()
    mode_group.add_argument('-s', '--solve', type=str, help='Solve sudoku puzzle', action='store', nargs='?', const='', metavar='SUDOKU_FILE')
    mode_group.add_argument('-g', '--generate', type=float, help='Generate sudoku puzzle', action='store', nargs='?', const=.7, metavar='DIFFICULTY')
    args = arg_parser.parse_args()

    if args.solve is not None:
        try:
            board = Board(load_board(args.solve))
        except ValueError:
            sys.stderr.write('Invalid board!\n')
            return 1
        
        sudoku = Sudoku(board)
        if sudoku.solve(ForwardCheck()):
            sudoku.board.print_board(args.plain)
        else:
            print('No solution')

        if args.count:
            print('backtrack count:', sudoku.backtrack_count)
        return 0

    if args.generate is not None:
        sudoku = Sudoku()
        sudoku.generate(ForwardCheck(), difficulty=args.generate)
        sudoku.board.print_board()
        if args.export is not None:
            if args.export != 'pdf' and args.export != 'txt':
                sys.stderr.write('Not supported file type!\n')
                return 1
            export = save_file.formats[args.export]
            export(sudoku.board)
        return 0

    arg_parser.print_help()
    return 1

if __name__ == '__main__':
    SystemExit(main())