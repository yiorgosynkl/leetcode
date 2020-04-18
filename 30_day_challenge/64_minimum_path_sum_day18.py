class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        def update(i,j):
            if i == len(grid) - 1:
                grid[i][j] += grid[i][j+1]
            elif j == len(grid[0]) - 1:
                grid[i][j] += grid[i+1][j]
            else:
                grid[i][j] += min(grid[i][j+1], grid[i+1][j])
        
        order = [(i,j) for i in range(len(grid)) for j in range(len(grid[0]))]
        order = sorted(order, key = lambda x: x[0] + x[1]) 
        order.pop() # pop first that needs no update
        while order:
            i, j = order.pop() # pop last in O(1)
            update(i,j)
        return grid[0][0]
    
# perfect solution
#     def minPathSum(self, grid):
#         m = len(grid)
#         n = len(grid[0])
#         for i in range(1, n):
#             grid[0][i] += grid[0][i-1]
#         for i in range(1, m):
#             grid[i][0] += grid[i-1][0]
#         for i in range(1, m):
#             for j in range(1, n):
#                 grid[i][j] += min(grid[i-1][j], grid[i][j-1])
#         return grid[-1][-1]
