################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200824
# Problem link      : https://leetcode.com/problems/sum-of-left-leaves/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # def sumOfLeftLeaves(self, root: TreeNode) -> int:
    #     self.ans = 0
    #     def dfs(node):
    #         if not node: return
    #         if node.left and not node.left.left and not node.left.right:
    #             self.ans += node.left.val
    #         dfs(node.left)
    #         dfs(node.right)
    #         return 
    #     dfs(root)
    #     return self.ans

    # recursive short solutions by @others
    # def sumOfLeftLeaves(self, root):
    #     if not root: return 0
    #     if root.left and not root.left.left and not root.left.right:
    #         return root.left.val + self.sumOfLeftLeaves(root.right)
    #     return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)   # isn't leave

    # def sumOfLeftLeaves(self, root, isLeft=False):
    #     if not root: return 0
    #     if not (root.left or root.right): return root.val * isLeft
    #     return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)
                        
#     def sumOfLeftLeaves(self, root: TreeNode) -> int:
#         def bfs(node):
#             if not node: return 0
#             upq, doq = [(node,'r')], [] # up queue, down queue (next level)
#             ans = 0
#             while upq:
#                 while upq:
#                     node, pos = upq.pop()
#                     if not node.left and not node.right and pos == 'l':
#                         ans += node.val
#                     if node.left: doq.append((node.left, 'l'))
#                     if node.right: doq.append((node.right, 'r'))
#                 upq, doq = doq, []
#             return ans
#         return bfs(root)
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def bfs(node):
            if not node: return 0
            q = deque([[node,'r']])
            ans = 0
            while q:
                node, pos = q.popleft()
                if not node.left and not node.right and pos == 'l':
                    ans += node.val
                if node.left: q.append([node.left, 'l'])
                if node.right: q.append([node.right, 'r'])
            return ans
        return bfs(root)
            