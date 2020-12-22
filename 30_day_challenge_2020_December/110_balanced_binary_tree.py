################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201222
# Problem link      : https://leetcode.com/problems/balanced-binary-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def dfs(node):
            if not node:
                return 0
            left_h, right_h = dfs(node.left), dfs(node.right)
            self.res = self.res and abs(left_h - right_h) <= 1
            return max(left_h, right_h) + 1
        dfs(root)
        return self.res
    
    
    # def isBalanced(self, root):
    #     def check(root):
    #         if root is None:
    #             return 0
    #         left  = check(root.left)
    #         right = check(root.right)
    #         if left == -1 or right == -1 or abs(left - right) > 1:
    #             return -1
    #         return 1 + max(left, right)
    #     return check(root) != -1
    
    # def isBalanced(self, root):
    #     stack, node, last, depths = [], root, None, {}
    #     while stack or node:
    #         if node:
    #             stack.append(node)
    #             node = node.left
    #         else:
    #             node = stack[-1]
    #             if not node.right or last == node.right:
    #                 node = stack.pop()
    #                 left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
    #                 if abs(left - right) > 1: return False
    #                 depths[node] = 1 + max(left, right)
    #                 last = node
    #                 node = None
    #             else:
    #                 node = node.right
    #     return True
    
    # # @param {TreeNode} root
    # # @return {integer[]}
    # def isBalanced(self, root):
    #     stack, lefts, rights = [(root, None, '')], [], []
    #     while stack:
    #         node, visited, kind = stack.pop() # kind: left or right child??
    #         if node:
    #             if visited:
    #                 # add to result if visited
    #                 left_val, right_val = lefts.pop(), rights.pop()
    #                 if abs(left_val - right_val) > 1:
    #                     return False
    #                 if kind == 'l':
    #                     lefts.append(max(left_val, right_val) + 1)
    #                 else: # kind == 'r'
    #                     rights.append(max(left_val, right_val) + 1)
    #             else:
    #                 # post-order
    #                 stack.append((node, True, kind))
    #                 stack.append((node.right, False, 'r'))
    #                 stack.append((node.left, False, 'l'))
    #         else:
    #             if kind == 'l':
    #                 lefts.append(0)
    #             else: # kind == 'r'
    #                 rights.append(0)
    #     return True      
        