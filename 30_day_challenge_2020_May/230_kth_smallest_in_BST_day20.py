################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200520
# Problem link      : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder traversal of BST is an array sorted in the ascending order
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans = None
        self.count = 0
        def dfs(node):
            if node and not self.ans:
                dfs(node.left)
                self.count += 1
                if self.count == k:
                    self.ans = node.val
                dfs(node.right)
        dfs(root)
        return self.ans
    
# Instead of recursion, it could be converted into iteration, with the help of stack. 
# This way one could speed up the solution because there is no need to build the 
# entire inorder traversal, and one could stop after the kth element.
# class Solution:
#     def kthSmallest(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: int
#         """
#         stack = []
        
#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             k -= 1
#             if not k:
#                 return root.val
#             root = root.right

# import bisect

# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         self.ll = []
#         def dfs(node):
#             if node:
#                 dfs(node.left)
#                 dfs(node.right)
#                 bisect.insort(self.ll, node.val)
#         dfs(root)
#         return self.ll[k - 1]
            
        
        