# https://leetcode.com/problems/max-area-of-island/
def maxAreaOfIsland(grid: list[list[int]]) -> int:
    r_count = len(grid)
    c_count = len(grid[0])

    res = 0
    visited = set()
    def dfs(r:int, c:int)->int:
        if r >= r_count or r < 0 or c >= c_count or c < 0:
            return 0
        if grid[r][c] != 1:
            return 0
        if (r, c) in visited:
            return 0
        visited.add((r, c))
        return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c+1) + dfs(r, c-1)

    # for r in range(r_count):
    #     for c in range(c_count):
    #         if grid[r][c] == 1:
    #             count = dfs(r, c)
    #             res = max(res, count)
    # return res

    # 
    return max(dfs(r, c)
            for r in range(len(grid))
            for c in range(len(grid[0])))

grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid1)) # Output: 6

grid2 = [[0,0,0,0,0,0,0,0]]
print(maxAreaOfIsland(grid2)) # Output: 0
