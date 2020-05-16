################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200516
# Problem link      : https://leetcode.com/problems/odd-even-linked-list/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_head = head
        even_head = head.next
        alpha = odd_head
        bravo = even_head
        times = 0
        while bravo.next:
            alpha.next = bravo.next
            alpha, bravo = bravo, alpha.next
            times += 1
        alpha.next = bravo.next
        if times % 2 == 1:
            bravo.next = even_head
        else:
            alpha.next = even_head
        return odd_head
    
    # other consice solution
    # def oddEvenList(self, head):
    #     dummy1 = odd = ListNode(0)
    #     dummy2 = even = ListNode(0)
    #     while head:
    #         odd.next = head
    #         even.next = head.next
    #         odd = odd.next
    #         even = even.next
    #         head = head.next.next if even else None
    #     odd.next = dummy2.next
    #     return dummy1.next
