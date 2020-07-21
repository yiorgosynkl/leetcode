################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200721
# Problem link      : https://leetcode.com/problems/word-search/
################################################################

class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         rows, cols = len(board), len(board[0])
#         avoid = set()
        
#         def explore(row, col, word, avoid):
#             if word == '':
#                     return True
#             cell_id = row*cols + col
#             if 0 <= row < rows and 0 <= col < cols and cell_id not in avoid and board[row][col] == word[0]: 
#                 avoid.add(cell_id)
#                 for i, j in [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]:
#                     if explore(i, j, word[1:], avoid): return True
#                 avoid.remove(cell_id)
#             return False
        
#         for row in range(rows):
#             for col in range(cols):
#                 if explore(row, col, word, avoid): return True
#         return False
                
        
    # mutate input board
    def exist(self, board, word):
        if not board:
            return False
        n, m = len(board), len(board[0])
        
        def dfs(i,j, word):
            if not word:
                return True
            if i < 0 or i >= n or j < 0 or j >= m or word[0] != board[i][j]:
                return False
            letter, board[i][j] = board[i][j], '#'
            # res = any([dfs(k, l, word[1:]) for k, l in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]]) # inefficient
            res = dfs(i+1, j, word[1:]) or dfs(i, j+1, word[1:]) or dfs(i-1, j, word[1:]) or dfs(i, j-1, word[1:])
            board[i][j] = letter
            return res
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, word):
                    return True
        return False
            
        