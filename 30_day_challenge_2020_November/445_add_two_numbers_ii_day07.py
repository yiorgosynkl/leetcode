################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201107
# Problem link      : https://leetcode.com/problems/add-two-numbers-ii/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(l1: ListNode):
            head, tmp = None, None
            while l1:
                tmp = ListNode(l1.val)
                head, tmp.next = tmp, head
                l1 = l1.next
            return head
        def addTwoReverse(l1: ListNode, l2: ListNode) -> ListNode:
            s, c = 0, 0 # sum, carry
            head = ListNode()
            tmp = head
            while l1 or l2:
                s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
                s, c = s % 10, s // 10
                tmp.next = ListNode(s)
                tmp = tmp.next
                l1, l2 = (l1.next if l1 else l1), (l2.next if l2 else l2)
            if c > 0:
                tmp.next = ListNode(c)
                tmp = tmp.next
            return head.next
        
        return reverse(addTwoReverse(reverse(l1), reverse(l2)))
