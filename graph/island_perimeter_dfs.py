def islandPerimeter(grid: list[list[int]]) -> int:
    row_count = len(grid)
    col_count = len(grid[0])

    res = 0
    visited = set()
    def dfs(r:int, c:int) -> bool:
        nonlocal res
        if r < 0 or r >= row_count or c < 0 or c >= col_count:
            return False
        if grid[r][c] == 0:
            return False
        # prevent infinite loop 
        if (r, c) in visited:
            return True
        visited.add((r, c))
        # each island has 4 sides
        res += 4
        # if found neighbor island, each reduce 2 connected sides
        if dfs(r-1, c): res-=1
        if dfs(r+1, c): res-=1
        if dfs(r, c+1): res-=1
        if dfs(r, c-1): res-=1
        return True

    for r in range(row_count):
        for c in range(col_count):
            if grid[r][c] == 1:
                dfs(r, c)
                return res

grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid1)) # 16

grid2 = [[1]]
print(islandPerimeter(grid2)) # 4

grid3 = [[1,0]]
print(islandPerimeter(grid3)) # 4

        