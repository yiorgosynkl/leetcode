################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210104
# Problem link      : https://leetcode.com/problems/merge-two-sorted-lists/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # @yiorgosynkl
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = head = ListNode()
        while l1 or l2:
            if not l2 or (l1 and l1.val < l2.val):
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next 
        return head.next
            
    # @StefanPochmann
    def mergeTwoLists(self, a: ListNode, b: ListNode) -> ListNode:
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a
    