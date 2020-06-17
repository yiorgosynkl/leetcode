################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200617
# Problem link      : https://leetcode.com/problems/surrounded-regions/
################################################################

class Solution:
    # Stefan Pochmann
    def solve(self, board):
        if not any(board): return

        m, n = len(board), len(board[0])
        save = [ij for k in range(max(m,n)) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]    
    
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board:
#             return
#         rows = len(board)
#         cols = len(board[0])
#         def expand(r, c, old_ch, new_ch):
#             if 0 <= r <= rows-1 and 0 <= c <= cols-1 and board[r][c] == old_ch:
#                 board[r][c] = new_ch
#                 for i,j in [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]:
#                     expand(i, j, old_ch, new_ch)
#         # fix borders
#         for r in range(rows):
#             if board[r][0] == 'O': expand(r,0,'O','-')
#             if board[r][cols-1] == 'O': expand(r,cols-1,'O','-')
#         for c in range(cols):
#             if board[0][c] == 'O': expand(0,c,'O','-')
#             if board[rows-1][c] == 'O': 
#                 expand(rows-1,c,'O','-')   
#         # insiders
#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == 'O': expand(r,c,'O','X')
#         # fix borders
#         for r in range(rows):
#             if board[r][0] == '-': expand(r,0,'-','O')
#             if board[r][cols-1] == '-': expand(r,cols-1,'-','O')
#         for c in range(cols):
#             if board[0][c] == '-': expand(0,c,'-','O')
#             if board[rows-1][c] == '-': expand(rows-1,c,'-','O')                      
        