################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200420
# Problem link      : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
################################################################

from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dive(node, bounds):
            (lo, hi) = bounds
            while preorder and lo < preorder[0] and preorder[0] < hi: 
                # maximum 2 loops, happens automatically for preorder
                child = TreeNode(preorder.pop(0))
                if child.val < node.val:
                    node.left = child
                    dive(child, (lo, node.val))
                else:
                    node.right = child
                    dive(child, (node.val, hi))
        root = TreeNode(preorder.pop(0))
        dive(root, (-inf, +inf))
        return root




    
# quick clean solutions by lee215
# def bstFromPreorder(self, A): # find where val splits preorder and share pieces to children
#     if not A: return None
#     root = TreeNode(A[0])
#     i = bisect.bisect(A, A[0])
#     root.left = self.bstFromPreorder(A[1:i])
#     root.right = self.bstFromPreorder(A[i:])
#     return root

# i = 0
# def bstFromPreorder(self, A, bound=float('inf')):
#     if self.i == len(A) or A[self.i] > bound:
#         return None
#     root = TreeNode(A[self.i])
#     self.i += 1
#     root.left = self.bstFromPreorder(A, root.val)
#     root.right = self.bstFromPreorder(A, bound)
#     return root

# my stack solution
# def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
#     # first element always the root
#     root = TreeNode(preorder[0])
#     upper = 1000000
#     stack = [(root, upper)] # node and upper bound of it
#     for num in preorder[1:]:
#         while True:
#             if num < stack[-1][0].val:
#                 new = TreeNode(num)
#                 upper = stack[-1][0].val
#                 stack[-1][0].left = new
#                 stack.append((new, upper))
#                 break
#             elif num < stack[-1][1]: #and num > hi
#                 new = TreeNode(num)
#                 upper = stack[-1][1]
#                 stack[-1][0].right = new
#                 stack.append((new, upper))                    
#                 break
#             else:
#                 stack.pop()
#     return root
        