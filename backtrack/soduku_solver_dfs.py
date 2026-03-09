from collections import defaultdict

def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    def could_place(d, row, col):
        """
        Check if one could place a number d in (row, col) cell
        """
        return not (
            d in rows[row]
            or d in columns[col]
            or d in boxes[box_index(row, col)]
        )

    def place_number(d, row, col):
        """
        Place a number d in (row, col) cell
        """
        rows[row][d] += 1
        columns[col][d] += 1
        boxes[box_index(row, col)][d] += 1
        board[row][col] = str(d)

    def remove_number(d, row, col):
        """
        Remove a number that didn't lead to a solution
        """
        rows[row][d] -= 1
        columns[col][d] -= 1
        boxes[box_index(row, col)][d] -= 1
        if rows[row][d] == 0:
            del rows[row][d]
        if columns[col][d] == 0:
            del columns[col][d]
        if boxes[box_index(row, col)][d] == 0:
            del boxes[box_index(row, col)][d]
        board[row][col] = "."

    def place_next_numbers(row, col):
        """
        Call backtrack function in recursion to continue to place numbers
        till the moment we have a solution
        """
        if col == N - 1 and row == N - 1:
            sudoku_solved[0] = True
        else:
            if col == N - 1:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)

    def backtrack(row=0, col=0):
        """
        Backtracking
        """
        if board[row][col] == ".":
            for d in range(1, 10):
                if could_place(d, row, col):
                    place_number(d, row, col)
                    place_next_numbers(row, col)
                    if sudoku_solved[0]:
                        return
                    remove_number(d, row, col)
        else:
            place_next_numbers(row, col)

    n = 3
    N = n * n
    box_index = lambda row, col: (row // n) * n + col // n

    rows = [defaultdict(int) for _ in range(N)]
    columns = [defaultdict(int) for _ in range(N)]
    boxes = [defaultdict(int) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] != ".":
                d = int(board[i][j])
                place_number(d, i, j)

    sudoku_solved = [False]
    backtrack()



board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

result = [   
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]

solveSudoku(board)
assert board == result, f"Expected {result}, got {board}"
print("Test passed!")