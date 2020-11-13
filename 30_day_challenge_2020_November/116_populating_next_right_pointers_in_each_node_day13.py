################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201113
# Problem link      : https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
################################################################

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return None
        lvl = deque([root]) # nodes of previous and current level [list]
        ans = []
        while lvl:
            nxt = deque([]) # nodes of next level
            prv_node = None
            while lvl:
                cur_node = lvl.popleft()
                if cur_node.left: nxt.append(cur_node.left)
                if cur_node.right: nxt.append(cur_node.right)
                if prv_node: prv_node.next = cur_node
                prv_node = cur_node
            prv_node.next = None
            lvl = nxt
        return root
