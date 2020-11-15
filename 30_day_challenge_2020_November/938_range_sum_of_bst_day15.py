################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201115
# Problem link      : https://leetcode.com/problems/range-sum-of-bst/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(root: 'Node'):
            if not root: return 0
            return  dfs(root.right) + dfs(root.left) + (root.val if low <= root.val <= high else 0)
        return dfs(root) 
        
    # # iterative, @rock
    # def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    #     stk, sm = [root], 0
    #     while stk:
    #         node = stk.pop()
    #         if node:
    #             if node.val > L:
    #                 stk.append(node.left)    
    #             if node.val < R:
    #                 stk.append(node.right)
    #             if L <= node.val <= R:
    #                 sm += node.val    
    #     return sm        