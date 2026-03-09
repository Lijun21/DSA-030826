from collections import defaultdict

# given a valid suduku board n x n, it has valid solution, solve it! return the solved board
def sudoku_solver(board:list[list[str]])->None:
    n = len(board)

    r_store = defaultdict(set)
    c_store = defaultdict(set)
    sub_store = defaultdict(set)

    for r in range(n):
        for c in range(n):
            if board[r][c] == '.':
                continue
            d = board[r][c]
            r_store[r].add(d)
            c_store[c].add(d)
            sub_store[(r//3, c//3)].add(d)

    def is_valid(s:str, r:int, c:int)->bool:
        if s in r_store[r] or s in c_store[c] or s in sub_store[(r//3, c//3)]:
            return False
        return True

    def find_empty() -> tuple | None:
        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    return (r, c)
        return None

    stack = []
    empty = find_empty()
    if not empty: return 
    stack.append((empty[0], empty[1], 1))

    while stack:
        r, c, d = stack.pop()

        # undo previously placed value at this cell before trying next digit
        if board[r][c] != '.':
            prev = board[r][c]
            board[r][c] = '.'
            r_store[r].remove(prev)
            c_store[c].remove(prev)
            sub_store[(r//3, c//3)].remove(prev)

        if d > 9:
            continue  # exhausted all digits, backtrack to previous cell

        if is_valid(str(d), r, c):
            board[r][c] = str(d)
            r_store[r].add(str(d))
            c_store[c].add(str(d))
            sub_store[(r//3, c//3)].add(str(d))

            stack.append((r, c, d+1))  # save backtrack point
            nxt = find_empty()
            if not nxt:
                return  # solved
            stack.append((nxt[0], nxt[1], 1))
        else:
            stack.append((r, c, d+1))  # try next digit

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

sudoku_solver(board)
assert board == result, f"Expected {result}, got {board}"
print("Test passed!")