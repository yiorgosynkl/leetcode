################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200429
# Problem link      : https://leetcode.com/problems/binary-tree-maximum-path-sum/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')

        def dive(node):
            if not node: # null node
                return 0
            lscore = dive(node.left) # left
            rscore = dive(node.right) # right
            nonlocal ans # this is the way to access global var in inner function
            ans = max(ans, lscore + rscore + node.val)
            bscore = node.val + max(lscore, rscore) # best path that ends at node
            return max(bscore, 0) # return 0 if negative
        
        dive(root)
        return ans
            
# StefanPochmann
# helper function returns:
# 1. The max sum of all paths ending in the given node (can be extended through the parent)
# 2. The max sum of all paths anywhere in tree rooted at the given node (can not be extended through the parent)
# def maxPathSum(self, root):
#     def maxsums(node):
#         if not node:
#             return [-2**31] * 2
#         left = maxsums(node.left)
#         right = maxsums(node.right)
#         return [node.val + max(left[0], right[0], 0),
#                 max(left + right + [node.val + left[0] + right[0]])]
#     return max(maxsums(root))

# StefanPochmann
# second way of accessing global variable
# def maxPathSum(self, root):
#     def maxend(node):
#         if not node:
#             return 0
#         left = maxend(node.left)
#         right = maxend(node.right)
#         self.max = max(self.max, left + node.val + right)
#         return max(node.val + max(left, right), 0)
#     self.max = None
#     maxend(root)
#     return self.max
            
# NOTE:
# actually it is a twist of Kadanes algorithm
# https://hackernoon.com/kadanes-algorithm-explained-50316f4fd8a6
