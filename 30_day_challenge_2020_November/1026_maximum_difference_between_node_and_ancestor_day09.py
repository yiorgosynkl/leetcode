################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201109
# Problem link      : https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def maxAncestorDiff(self, root: TreeNode) -> int:
    #     self.ans = 0 # or use simple variable 
    #     def dfs(node):
    #         if not node: return None, None
    #         # nonlocal ans # and here make this statement
    #         mn_left, mx_left = dfs(node.left)
    #         mn_right, mx_right = dfs(node.right)
    #         mn = min(node.val, mn_left if mn_left != None else node.val, mn_right if mn_right != None else node.val)
    #         mx = max(node.val, mx_left if mx_left != None else node.val, mx_right if mx_right != None else node.val)
    #         self.ans = max(self.ans, abs(node.val - mn), abs(node.val - mx))
    #         return mn, mx
    #     dfs(root)
    #     return self.ans
    
    # @lee215 oneliner (pass max and min to children, at leaf nodes return difference)
    def maxAncestorDiff(self, root, mn=100000, mx=0):
        return max(self.maxAncestorDiff(root.left, min(mn, root.val), max(mx, root.val)), \
            self.maxAncestorDiff(root.right, min(mn, root.val), max(mx, root.val))) \
            if root else mx - mn
