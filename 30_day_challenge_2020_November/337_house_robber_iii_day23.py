################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201123
# Problem link      : https://leetcode.com/problems/house-robber-iii/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # if not root selected than best sum of left and right (yes or no selected root) subtrees
    # if root selected than max sum of left and right (no selected root) subtree 
    # dp 2 values for each node, traverse using dfs
    def rob(self, root: TreeNode) -> int:
        # return score when, yes, selected (ys) and score when not selected (ns)
        def xrob(node): 
            if not node:
                return (0, 0)
            lys, lns = xrob(node.left) # left child score (yes or no selected)
            rys, rns = xrob(node.right) # right child score (yes or no selected)
            pys, pns = node.val + lns + rns, max(lys, lns) + max(rys, rns) # parent score  (yes or no selected)
            return (pys, pns)
        return max(xrob(root))
