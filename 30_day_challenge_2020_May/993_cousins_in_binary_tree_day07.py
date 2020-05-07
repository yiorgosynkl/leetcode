################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200507
# Problem link      : https://leetcode.com/problems/cousins-in-binary-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_list = []
        y_list = []
        queue = [(root, 0, None)] # (node, depth, father)
        while True:
            if not queue:
                break
            node, level, father = queue.pop(0)
            if node: # not null
                if node.val == x:
                    x_list.append((level, father))
                if node.val == y:
                    y_list.append((level, father))
                # print(node.val, level)
                queue.append((node.left, level+1, node))
                queue.append((node.right, level+1, node))
        for x_lev, x_fath in x_list:
            for y_lev, y_fath in y_list:
                if x_lev == y_lev and x_fath != y_fath:
                    return True
        return False
        
    # assuming that x or y are found once, author: rock
    # def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    #     q, depth, xDepth, yDepth = [root], 0, -1, -2
    #     while q:
    #         q2 = []
    #         depth += 1
    #         for node in q:
    #             sameParent = 0
    #             for child in (node.left, node.right):
    #                 if child:
    #                     q2.append(child)
    #                     if child.val == x:
    #                         xDepth = depth
    #                         sameParent += 1
    #                     elif child.val == y:
    #                         yDepth = depth
    #                         sameParent += 1
    #             if sameParent == 2:
    #                 return False            
    #         q = q2 
    #     return xDepth == yDepth
