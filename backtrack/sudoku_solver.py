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

    # can not use iterative way, only dfs?
    def dfs(r:int, c:int)->bool:
        # all the cells in boards has been filled, return True 
        if r == n -1 and c == n:
            return True
        if c == n:
            c = 0
            r +=1
        # cur cell filled, to fill next one return its result 
        if board[r][c] != '.':
            return dfs(r, c+1)
        # find a valid number fill in the board
        for i in range(1, n+1):
            if not is_valid(str(i), r, c):
                continue
            board[r][c] = str(i)
            r_store[r].add(str(i))
            c_store[c].add(str(i))
            sub_store[(r//3, c//3)].add(str(i))

            # if next cells all able to find valid number, return True
            if dfs(r, c+1):
                return True
            
            board[r][c] = '.'
            r_store[r].remove(str(i))
            c_store[c].remove(str(i))
            sub_store[(r//3, c//3)].remove(str(i))

        # if can not find a valid number for this cell, return False
        return False   
    dfs(0, 0)






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