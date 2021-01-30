################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210129
# Problem link      : https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    # def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    #     dic = defaultdict(list)
    #     self.mn, self.mx = 1, -1
    #     def dfs(node, row, col):
    #         if node: 
    #             dic[col].append((row, node.val))
    #             self.mn, self.mx = min(self.mn, col), max(self.mx, col)
    #             dfs(node.left, row+1, col-1)
    #             dfs(node.right, row+1, col+1)
    #     dfs(root, 0, 0)
    #     out = []
    #     for i in range(self.mn, self.mx+1):
    #         out.append([val for row, val in sorted(dic[i])])
    #     return out

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        self.mn, self.mx = 1, -1
        q = deque([(root, 0, 0)])
        while q:
            node, row, col = q.popleft()
            dic[col].append((row, node.val))
            self.mn, self.mx = min(self.mn, col), max(self.mx, col)
            if node.left: q.append((node.left, row+1, col-1))   
            if node.right: q.append((node.right, row+1, col+1))   
        out = []
        for i in range(self.mn, self.mx+1):
            out.append([val for row, val in sorted(dic[i])])
        return out
