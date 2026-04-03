"""
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/?envType=problem-list-v2&envId=matrix
"""

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0]*3 for _ in range(3)]

        for i, (r, c) in enumerate(moves):
            grid[r][c] = 1 if i % 2 == 0 else -1

        # 3 rows, 3 cols, 2 diagnals
        lines = (
            [grid[i] for i in range(3)] + 
            [[grid[r][c] for r in range(3)] for c in range(3)] +
            [[grid[i][i] for i in range(3)]] + 
            [[grid[2-i][i] for i in range(3)]]
        )

        for line in lines:
            if line == [1, 1, 1]:
                return "A"
            if line == [-1, -1, -1]:
                return "B"

        return "Draw" if len(moves) == 9 else "Pending"
        