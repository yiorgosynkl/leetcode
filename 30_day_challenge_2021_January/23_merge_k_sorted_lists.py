################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210124
# Problem link      : https://leetcode.com/problems/merge-k-sorted-lists/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import bisect
# from Queue import PriorityQueue
from heapq import heappush, heappop, heapreplace, heapify

class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     ptr = head = ListNode()
    #     k = len(lists)
    #     while True:
    #         mi = k
    #         for i, node in enumerate(lists):
    #             if node != None and ((mi == k) or node.val < lists[mi].val):
    #                 mi = i
    #         if mi == k:
    #             break
    #         ptr.next = lists[mi]
    #         ptr = ptr.next
    #         lists[mi] = lists[mi].next
    #     return head.next
    
    # # keep order using heap
    # def mergeKLists(self, lists):
    #     dummy = node = ListNode(0)
    #     h = [(n.val, i, n) for i, n in enumerate(lists) if n]
    #     heapify(h)
    #     while h:
    #         v, i, n = h[0]
    #         if n.next is None:
    #             heappop(h) #only change heap size when necessary
    #         else:
    #             heapreplace(h, (n.next.val, i, n.next)) # if node.val same, compare next value (indices)
    #         node.next = n
    #         node = node.next
    #     return dummy.next

    # recursive divide and conquer
    def mergeKLists(self, lists):
        def merge(l, r):
            dummy = p = ListNode()
            while l and r:
                if l.val < r.val:
                    p.next = l
                    l = l.next
                else:
                    p.next = r
                    r = r.next
                p = p.next
            p.next = l or r
            return dummy.next
        
        def merge1(l, r):
            if not l or not r:
                return l or r
            if l.val< r.val:
                l.next = merge(l.next, r)
                return l
            r.next = merge(l, r.next)
            return r

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return merge(l, r)
    
    