# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def helper(node: TreeNode) -> (int, int):
    if not node.left and not node.right:
        return (0, 0)
    (left, best_left) = helper(node.left) if node.left != None else (-1, -1)
    (right, best_right) = helper(node.right) if node.right != None else (-1, -1)
    print('{} -> {},{},{},{}'.format(node.val, left, best_left, right, best_right))
    return (max(left + 1, right + 1), max([left + right + 2, best_left, best_right]))
    
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        (path , diameter) = helper(root)
        return max(diameter, path)