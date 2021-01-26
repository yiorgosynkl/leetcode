################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210126  - Bloomberg interview
# Problem link      : https://leetcode.com/problems/min-stack/
################################################################

class Solution:
#     def getId(self, row, col):
#         return row * self.n_cols + col # id range [0, n_rows * n_cols - 1]

#     def getCoords(self, idd):
#         return (idd // self.n_cols, idd % self.n_cols)
    
#     def discover(self, x):
#         if x not in self.lands:
#             return
#         self.lands.remove(x)
#         row, col = self.getCoords(x)
#         if row > 0:
#             self.discover(self.getId(row - 1, col))
#         if row < self.n_rows - 1:
#             self.discover(self.getId(row + 1, col))
#         if col > 0:
#             self.discover(self.getId(row, col - 1))
#         if col < self.n_cols - 1:
#             self.discover(self.getId(row, col + 1))
#         return
    
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if grid == []:
#             return 0
#         self.n_rows = len(grid)
#         self.n_cols = len(grid[0])
#         self.lands = set([])
#         for row in range(self.n_rows):
#             for col in range(self.n_cols):
#                 if grid[row][col] != "0":
#                     self.lands.add(self.getId(row, col)) # id range [0, n_rows * n_cols - 1]
#         count = 0
#         while self.lands:
#             x = next(iter(self.lands))
#             self.discover(x)
#             count += 1
#         return count

    # @yiorgosynkl, dfs to grid graph
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                for k,l in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    dfs(k,l)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    cnt += 1
        return cnt
    
#     # @yiorgosynkl, bfs to grid graph
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m, n = len(grid), len(grid[0])
#         def bfs(r, c):
#             q = deque([(r,c)])
#             while q:
#                 i, j = q.popleft()
#                 if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
#                     grid[i][j] = '0'
#                     for k,l in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
#                         q.append((k,l))
#         cnt = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     bfs(i,j)
#                     cnt += 1
#         return cnt
    
    # # great concise programming    
    # def numIslands(self, grid):
    #     def sink(i, j):
    #         if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
    #             grid[i][j] = '0'
    #             map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
    #             return 1
    #         return 0
    #     return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

# tips
# 1. change grid to arbitrary character '#' instead of having extra lands set
# 2. first call function and then do the check if coords are valid
# 3. map function for less writing
