################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200601
# Problem link      : https://leetcode.com/problems/invert-binary-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque 

class Solution:
    # iterative
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     queue = deque()
    #     if root: queue.append(root)
    #     while queue:
    #         node = queue.popleft()
    #         node.left, node.right = node.right, node.left
    #         if node.left: queue.append(node.left)
    #         if node.right: queue.append(node.right)
    #     return root
        
    # recursive
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     def invert(node):
    #         if not node: return 
    #         invert(node.left)
    #         invert(node.right)
    #         node.left, node.right = node.right, node.left
    #         return node
    #     return invert(root)
                
        
    # recursive short
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if not node: return 
            node.left, node.right = invert(node.right), invert(node.left)
            return node
        return invert(root)    
            