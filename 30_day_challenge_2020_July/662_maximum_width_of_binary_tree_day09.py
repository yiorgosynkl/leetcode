################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200708
# Problem link      : https://leetcode.com/problems/maximum-width-of-binary-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        upq, doq = [root], [] # upper queue and lower queue
        ans, root.val = 0, 1
        while upq:
            mini, maxi = float('inf'), float('-inf')
            while upq:
                node = upq.pop()
                mini, maxi = min(mini, node.val), max(maxi, node.val)
                if node.left: 
                    node.left.val = 2*node.val - 1
                    doq.append(node.left)
                if node.right: 
                    node.right.val = 2*node.val
                    doq.append(node.right)
            ans = max(ans, maxi-mini+1)
            upq, doq = doq, []
        return ans

#     # @StefanPochmann solution
#     def widthOfBinaryTree(self, root):
#         width = 0
#         level = [(1, root)]
#         while level:
#             width = max(width, level[-1][0] - level[0][0] + 1)
#             level = [kid
#                      for number, node in level
#                      for kid in enumerate((node.left, node.right), 2 * number)
#                      if kid[1]]
#         return width
    

#.    # ??? DFS TO CHECK LATER ??? # awice sol
#     def widthOfBinaryTree(self, root):
#         def dfs(node, depth = 0, pos = 0):
#             if node:
#                 yield depth, pos
#                 yield from dfs(node.left, depth + 1, pos * 2)
#                 yield from dfs(node.right, depth + 1, pos * 2 + 1)

#         left = {}
#         right = {}
#         ans = 0
#         for depth, pos in dfs(root):
#             left[depth] = min(left.get(depth, pos), pos)
#             right[depth] = max(right.get(depth, pos), pos)
#             ans = max(ans, right[depth] - left[depth] + 1)

#         return ans
    
#         left, self.res = {}, 0
#         def dfs(root, level = 0, pos = 0):
#             if root:
#                 if level not in left: left[level] = pos
#                 self.res = max(self.res, pos - left[level] + 1)
#                 dfs(root.left, level + 1, pos * 2)
#                 dfs(root.right, level + 1, pos * 2 + 1)
#         dfs(root)
#         return self.res
