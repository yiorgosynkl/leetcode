################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200626
# Problem link      : https://leetcode.com/problems/sum-root-to-leaf-numbers/
################################################################

from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # dfs with stack 
    # def sumNumbers(self, root: TreeNode) -> int:
    #     if root == None: return 0
    #     stack, ans = [(root, 0)], 0
    #     while stack:
    #         node, val = stack.pop()
    #         if node.left == None and node.right == None:
    #             ans += val*10 + node.val
    #         else:
    #             if node.left: stack.append((node.left, val*10 + node.val))
    #             if node.right: stack.append((node.right, val*10 + node.val))
    #     return ans
    
    # bfs with queue
    # def sumNumbers(self, root: TreeNode) -> int:
    #     if root == None: return 0
    #     q, ans = deque([(root, 0)]), 0
    #     while q:
    #         node, val = q.popleft()
    #         if node.left == None and node.right == None:
    #             ans += val*10 + node.val
    #         else:
    #             if node.left: q.append((node.left, val*10 + node.val))
    #             if node.right: q.append((node.right, val*10 + node.val))
    #     return ans
    
    # recursive dfs with chars
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None: return 0
        self.count = 0
        def dfs(node, num):
            num += str(node.val)
            if node.left == None and node.right == None:
                self.count += int( num )
            else:
                if node.left: dfs(node.left, num )
                if node.right: dfs(node.right, num )
        dfs(root, '')
        return self.count
                        
    # recursive dfs with nums
    # def sumNumbers(self, root: TreeNode) -> int:
    #     self.ans = 0
    #     def dfs(node, val):
    #         if node:
    #             val = val*10 + node.val
    #             if not node.left and not node.right:
    #                 self.ans += val
    #             else:
    #                 dfs(node.left, val)
    #                 dfs(node.right, val)
    #     dfs(root, 0)
    #     return self.ans
        
