def sudoku_solver_iterative(board):
    def find_empty():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    return (r, c)
        return None

    def is_valid(s, r, c):
        if s in [board[r][cc] for cc in range(9)]: return False
        if s in [board[rr][c] for rr in range(9)]: return False
        br, bc = (r//3)*3, (c//3)*3
        for dr in range(3):
            for dc in range(3):
                if board[br+dr][bc+dc] == s: return False
        return True

    # stack stores (row, col, next_digit_to_try)
    stack = []
    pos = find_empty()
    if not pos: return
    stack.append((*pos, 1))

    while stack:
        r, c, d = stack.pop()
        if d > 9:  # exhausted all digits → backtrack
            board[r][c] = '.'
            continue
        if is_valid(str(d), r, c):
            board[r][c] = str(d)
            stack.append((r, c, d + 1))  # save backtrack point
            nxt = find_empty()
            if not nxt:
                return  # solved
            stack.append((*nxt, 1))
        else:
            stack.append((r, c, d + 1))  # try next digit


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

sudoku_solver_iterative(board)
assert board == result, f"Expected {result}, got {board}"
print("Test passed!")