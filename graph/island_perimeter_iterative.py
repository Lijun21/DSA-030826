def islandPerimeter(grid: list[list[int]])->int:
    row_count = len(grid)
    col_count = len(grid[0])

    res = 0
    for r in range(row_count):
        for c in range(col_count):
            if grid[r][c] == 1:
                res += 4
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    res -= 2
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    res -= 2
    return res


grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid1)) # 16

grid2 = [[1]]
print(islandPerimeter(grid2)) # 4

grid3 = [[1,0]]
print(islandPerimeter(grid3)) # 4


