################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210112
# Problem link      : https://leetcode.com/problems/add-two-numbers/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     s, c = 0, 0 # sum, carry
    #     head = ListNode()
    #     tmp = head
    #     while l1 or l2:
    #         s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
    #         s, c = s % 10, s // 10
    #         tmp.next = ListNode(s)
    #         tmp = tmp.next
    #         l1, l2 = (l1.next if l1 else l1), (l2.next if l2 else l2)
    #     if c > 0:
    #         tmp.next = ListNode(c)
    #         tmp = tmp.next
    #     return head.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s, c = 0, 0 # sum, carry
        head = ListNode()
        tmp = head
        while l1 or l2 or c:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            c, s = divmod(s, 10)
            tmp.next = ListNode(s)
            tmp = tmp.next
            l1, l2 = (l1.next if l1 else l1), (l2.next if l2 else l2)
        return head.next

    # # @StefanPochmann (lists -> ints -> lists)
    # def addTwoNumbers(self, l1, l2):
    #     def toint(node):
    #         return node.val + 10 * toint(node.next) if node else 0
    #     def tolist(n):
    #         node = ListNode(n % 10)
    #         if n > 9:
    #             node.next = tolist(n / 10)
    #         return node
    #     return tolist(toint(l1) + toint(l2))
    
    # # arbitrarily many lists could be passed
    # def addTwoNumbers(self, l1, l2):
    #     addends = l1, l2
    #     dummy = end = ListNode(0)
    #     carry = 0
    #     while addends or carry:
    #         carry += sum(a.val for a in addends)
    #         addends = [a.next for a in addends if a.next]
    #         end.next = end = ListNode(carry % 10)
    #         carry /= 10
    #     return dummy.next
