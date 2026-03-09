from collections import deque

def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    # starting pixel original color
    ori_color = image[sr][sc]

    r_count = len(image)
    c_count = len(image[0])

    if ori_color == color:
        return image
    
    dq = deque([(sr, sc)])

    while dq:
        r, c = dq.popleft()
        image[r][c] = color 
        if r - 1 >= 0 and image[r-1][c] == ori_color:
            dq.append((r-1, c))
        if c - 1 >= 0 and image[r][c-1] == ori_color:
            dq.append((r, c-1))
        if r + 1 <= r_count -1 and image[r+1][c] == ori_color:
            dq.append((r+1, c))
        if c + 1 <= c_count -1 and image[r][c+1] == ori_color:
            dq.append((r, c+1))

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