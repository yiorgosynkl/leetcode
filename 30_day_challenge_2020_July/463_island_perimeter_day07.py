################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200707
# Problem link      : https://leetcode.com/problems/island-perimeter/
################################################################

from itertools import product

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i,j in product(range(rows), range(cols)):
            if grid[i][j] == 1:
                for r,c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if r == -1 or r == rows or c == -1 or c == cols or grid[r][c] == 0:
                        ans += 1
        return ans

    # # @StefanPochmann
    # def islandPerimeter(self, grid):
    #     return sum(sum(map(operator.ne, [0] + row, row + [0]))
    #                for row in grid + map(list, zip(*grid)))