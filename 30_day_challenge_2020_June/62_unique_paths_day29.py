################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200629
# Problem link      : https://leetcode.com/problems/unique-paths/
################################################################

import math

class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     grid = [[1 for _ in range(n)] for _ in range(m)]
    #     for i in reversed(range(m-1)):
    #         for j in reversed(range(n-1)):
    #             grid[i][j] = grid[i+1][j] + grid[i][j+1]
    #     return grid[0][0]
        
    # combinatorial, (m-1) times Down move, (n-1) times Right move
    # choose the spots of (m-1) Down moves from total of (m+n-2) moves 
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2, m-1)

