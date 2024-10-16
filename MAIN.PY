# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()

# Function to check if placing a number is valid
def is_valid(board, row, col, num):
    # Check if num is not in the current row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if num is not in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if num is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Function to find the next empty spot (represented by 0)
def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

# Main function to solve the Sudoku using backtracking
def solve_sudoku(board):
    empty_pos = find_empty(board)

    # If no empty spot is found, the puzzle is solved
    if not empty_pos:
        return True

    row, col = empty_pos

    # Try numbers 1-9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number if valid
            board[row][col] = num

            # Recursively attempt to solve the rest of the board
            if solve_sudoku(board):
                return True

            # If solution does not work, backtrack
            board[row][col] = 0

    # Trigger backtracking
    return False

# Test Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku puzzle to solve:")
print_board(board)

# Solve the Sudoku puzzle
if solve_sudoku(board):
    print("Sudoku puzzle solved:")
    print_board(board)
else:
    print("No solution exists.")
