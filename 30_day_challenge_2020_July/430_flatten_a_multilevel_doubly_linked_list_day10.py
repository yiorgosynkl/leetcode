################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200710
# Problem link      : https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
################################################################

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node': 
        def levelup(head):
            left, right, tail = head, head.next, head
            while left:
                right = left.next
                if left.child:
                    child_head, child_tail = levelup(left.child)
                    left.next, child_head.prev  = child_head, left
                    if right:
                        child_tail.next, right.prev = right, child_tail
                    left.child = None
                    tail = left
                tail, left = left, right
            return head, tail

        if not head: return head
        head, tail = levelup(head)    
        return head
