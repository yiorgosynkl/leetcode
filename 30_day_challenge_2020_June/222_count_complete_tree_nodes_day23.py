################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200623
# Problem link      : https://leetcode.com/problems/count-complete-tree-nodes/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int: 
        # recursive optimised for complete binary tree
        def height(root: TreeNode):
            return -1 if not root else 1 + height(root.left)
        h = height(root)
        if h < 0: return 0
        return (1 << h) + self.countNodes(root.right) if h - 1 == height(root.right) else (1 << h-1) + self.countNodes(root.left)
    
    
    # def countNodes(self, root: TreeNode) -> int:
    #     if not root: return 0
    #     q, count = [root], 0 # bfs
    #     while q:
    #         node = q.pop()
    #         count += 1
    #         if node.left: q.append(node.left)
    #         if node.right: q.append(node.right)
    #     return count
    
    # def countNodes(self, root: TreeNode) -> int: # recursive
    #     return 0 if not root else 1 + self.countNodes(root.left) + self.countNodes(root.right)
