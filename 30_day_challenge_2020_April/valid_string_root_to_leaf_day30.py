################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200430
# Problem link      : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        def dfs(node, llist):
            if node and len(llist) == 1 and node.val == llist[0] and node.left == None and node.right == None:
                return True
            if not node or not llist:
                return False
            if node.val == llist[0]:
                return dfs(node.left, llist[1:]) or dfs(node.right, llist[1:])
            return False

        return dfs(root, arr)
    
    # def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
    #     dq = collections.deque([root])
    #     for depth, a in enumerate(arr):
    #         for _ in range(len(dq)):
    #             node = dq.popleft()
    #             if node and node.val == a:
    #                 if depth + 1 == len(arr) and node.left == node.right == None:
    #                     return True
    #                 dq.extend(child for child in (node.left, node.right) if child)
    #     return False
        