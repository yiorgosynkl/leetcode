################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201216
# Problem link      : https://leetcode.com/problems/validate-binary-search-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def dfs(node, lower, upper):
    #         if not node:
    #             return True
    #         if lower < node.val < upper:
    #             return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
    #         return False
    #     return dfs(root, -math.inf, math.inf)
    
    def isValidBST(self, root: TreeNode, lower = -math.inf, upper = math.inf) -> bool:
        if not root:
            return True
        if lower < root.val < upper:
            return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)
        return False
