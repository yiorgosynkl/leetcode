################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200615
# Problem link      : https://leetcode.com/problems/search-in-a-binary-search-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def searchBST(self, root: TreeNode, val: int) -> TreeNode: # recursive
    #     if root == None: return None
    #     if val < root.val : return self.searchBST(root.left, val)
    #     if root.val < val: return self.searchBST(root.right, val)
    #     return root # if root.val == val
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode: # iterative
        while root:
            if root.val == val:
                return root
            else:
                root = root.left if val < root.val else root.right
        return None

    # def searchBST(self, root: TreeNode, val: int) -> TreeNode: # recursive onliner
    #     return self.searchBST(root.left, val) if root and val < root.val else self.searchBST(root.right, val) if root and root.val < val else root
