# Sudoku solver and generator

This project implements backtrack algorithm together with MRV and LCV heuristics. To decrease the number of backtrack operations, the forward checking method is used.

## How to run the program

### Requirements
- Python 3.8+

### Commands
- `main.py -s <file>` - solves sudoku puzzle (see [sudoku_example](./sudoku_example) file)
- `main.py -g <difficulty>` - generates sudoku puzzle (difficulty determines number of filled cells)

> If `-s` flag is specified without argument, board will be read from standard input.

### Optional flags
- `-p/--plain` - prints plain board (just numbers)
- `-c/--count`- prints backtrack operations count
