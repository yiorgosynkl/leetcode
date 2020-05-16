################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200516
# Problem link      : https://leetcode.com/contest/biweekly-contest-26/problems/count-good-nodes-in-binary-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, maxim):
            if node == None:
                return 
            if node.val >= maxim:
                self.ans += 1
            dfs(node.left, max(maxim, node.val))
            dfs(node.right, max(maxim, node.val))
            return
        dfs(root, root.val)
        return self.ans