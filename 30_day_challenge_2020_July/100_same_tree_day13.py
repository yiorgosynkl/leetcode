################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200713
# Problem link      : https://leetcode.com/problems/same-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque

class Solution:
    # recursive solution
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q # (if objects have same type) return True if not p and not q else False
    
    # # bfs solution
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     pque, qque = deque([p]), deque([q])
    #     while pque and qque:
    #         pnode, qnode = pque.popleft(), qque.popleft()
    #         if not pnode and not qnode: # both null
    #             continue
    #         elif pnode and qnode and pnode.val == qnode.val:
    #             pque.extend([pnode.left, pnode.right])
    #             qque.extend([qnode.left, qnode.right])
    #         else:
    #             return False
    #     return True if not pque and not qque else False
    
    # # tuple solution and one-liner @StefanPochmann
    # def isSameTree(self, p, q):
    #     def t(n):
    #         return n and (n.val, t(n.left), t(n.right))
    #     return t(p) == t(q)
    # def isSameTree(self, p, q):
    #     return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q

