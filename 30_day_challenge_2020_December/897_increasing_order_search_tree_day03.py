################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201203
# Problem link      : https://leetcode.com/problems/increasing-order-search-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.ptr = TreeNode()
        def inorder_dfs(node):
            if not node: return 
            inorder_dfs(node.left)
            self.ptr.right = node
            self.ptr = node
            self.ptr.left = None
            inorder_dfs(node.right)
            return
        inorder_dfs(root)
        return ans.right

    # # @lee215
    # def increasingBST(self, root, tail = None):
    #     if not root: return tail
    #     res = self.increasingBST(root.left, root)
    #     root.left = None
    #     root.right = self.increasingBST(root.right, tail)
    #     return res

#     # iterative dfs, each parent is paired with a null
#     def increasingBST(self, root, tail = None):
#         sk = [root] # stack
#         start = p = TreeNode()
#         while sk:
#             if sk[-1] == None:
#                 sk.pop()
#                 if sk:
#                     sk[-1].left = None
#                     p.right = sk[-1]
#                     p = sk[-1]
#                     p.left = None
#                     sk.pop()
#                     sk.append(p.right)
#             else:
#                 sk.append(sk[-1].left)
#         return start.right

#     # official solution
#     def increasingBST(self, root):
#         def inorder(node):
#             if node:
#                 yield from inorder(node.left)
#                 yield node.val
#                 yield from inorder(node.right)

#         ans = cur = TreeNode(None)
#         for v in inorder(root):
#             cur.right = TreeNode(v)
#             cur = cur.right
#         return ans.right

    # iterative dfs, move once right and then left as much as possible
    def increasingBST(self, root):
        sk, node = [], root # stack
        while node:
            sk.append(node)
            node.left, node = None, node.left # move to next and clean left child in one line
        res = p = TreeNode()
        while sk:
            node = sk.pop()
            p.right = node
            p, node = node, node.right
            while node:
                sk.append(node)
                node.left, node = None, node.left # move to next and clean left child
        return res.right
