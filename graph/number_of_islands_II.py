
def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    neis = set()
    res = []
    count = 0
    for r, c in positions:
        count += 1
        if (r, c) in neis:
            count-=1
        if r - 1 > 0:
            neis.add((r-1, c))
        if r + 1 <= m -1:
            neis.add((r+1, c))
        if c - 1 > 0:
            neis.add((r, c-1))
        if c + 1 <= n -1:
            neis.add((r, c+1))
        res.append(count)
    return res

# Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
# Output: [1,1,2,3]
# Explanation:
# Initially, the 2d grid is filled with water.
# - Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
# - Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
# - Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
# - Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.




# Input: m = 1, n = 1, positions = [[0,0]]
# Output: [1]