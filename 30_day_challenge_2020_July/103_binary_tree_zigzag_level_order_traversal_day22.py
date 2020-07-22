################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200708
# Problem link      : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        prv = [root] if root else []
        ans = []
        while prv:
            lvl, nxt = [], []
            while prv:
                node = prv.pop()
                lvl.append(node.val)
                if len(ans) % 2 == 1: # rightmost node, add children from right to left (so the leftmost child will be at the end of the stack prv)
                    if node.right: nxt.append(node.right)
                    if node.left: nxt.append(node.left)
                else: # leftmost node
                    if node.left: nxt.append(node.left)
                    if node.right: nxt.append(node.right)
            ans.append(lvl)
            prv = nxt
        return ans
        