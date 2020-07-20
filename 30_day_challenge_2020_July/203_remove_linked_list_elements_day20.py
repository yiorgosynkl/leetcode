################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200720
# Problem link      : https://leetcode.com/problems/remove-linked-list-elements/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # iterative two pointers
    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     dummy = ListNode(0, head)
    #     first, second = dummy, head # dummy node
    #     while second:
    #         if second.val == val:
    #             first.next, second = second.next, second.next
    #         else:
    #             first, second = first.next, second.next
    #     return dummy.next
    
    # iterative one pointer
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        ptr = dummy
        while ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next
    
    # recursive
    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     if not head: return head
    #     head.next = self.removeElements(head.next, val) 
    #     return head.next if head.val == val else head
        
            