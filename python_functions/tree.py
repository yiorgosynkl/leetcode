# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder(root): # dfs
    return [root.val] + dfs(root.left) + dfs(root.right) if root else []

def inorder(root): # dfs
    return dfs(root.left) + [root.val] + dfs(root.right) if root else []

def postorder(root): # dfs
    return dfs(root.left) + dfs(root.right) + [root.val] if root else []