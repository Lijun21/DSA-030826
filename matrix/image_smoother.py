"""
https://leetcode.com/problems/image-smoother/?envType=problem-list-v2&envId=matrix
"""

def imageSmoother(img:list[list[int]])->list[list[int]]:

    r_count = len(img)
    c_count = len(img[0])

    grid = [[0]*c_count for _ in range(r_count)]

    def get_value(r:int, c:int)->int:
        # this is array, not range, also range last element is exclusive 
        # r_range = [max(r-1, 0), min(r+1, r_count-1)]
        # c_range = [max(c-1, 0), min(c+1, c_count-1)]

        r_range = range(max(r-1, 0), min(r+2, r_count))
        c_range = range(max(c-1, 0), max(c+2, c_count))

        total = 0
        count = 0
        # iterate through range 
        for fr in r_range:
            for fc in c_range:
                total += img[fr][fc]
                count += 1
        return total // count

    for r in range(r_count):
        for c in range(c_count):
            grid[r][c] = get_value(r, c)
    return grid