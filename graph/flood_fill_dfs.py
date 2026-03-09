def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    ori_color = image[sr][sc] 
    row_count = len(image)
    col_count = len(image[0])

    if ori_color == color:
        return image

    def dfs(r, c):
        if r < 0 or r >= row_count or c < 0 or c >= col_count:
            return
        if image[r][c] != ori_color:
            return
        image[r][c] = color
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image

image1 = [[1,1,1],[1,1,0],[1,0,1]]
sr1 = 1
sc1 = 1
color1 = 2

print(floodFill(image1, sr1, sc1, color1))
# Output: [[2,2,2],[2,2,0],[2,0,1]]

image2 = [[0,0,0],[0,0,0]]
sr2 = 0
sc2 = 0
color2 = 0

print(floodFill(image2, sr2, sc2, color2))
# Output: [[0,0,0],[0,0,0]]


