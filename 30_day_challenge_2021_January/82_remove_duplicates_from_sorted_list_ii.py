################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210105
# Problem link      : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
#     # removes duplicates, still holds one
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         ptr = head
#         while ptr and ptr.next:
#             if ptr.next and ptr.next.val == ptr.val:
#                 ptr.next = ptr.next.next
#             else:
#                 ptr = ptr.next
#         return head
    
    # @yiorgosynkl, removes all duplicates
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        back = out = ListNode(-101, head)
        front = out.next
        while back and front:
            if front.next and front.val == front.next.val:
                while front.next and front.val == front.next.val:
                    front = front.next
                front = front.next
                back.next = front
            else:
                back = front
                front = front.next
        return out.next
    
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node 
        # before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist 
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next 
            # otherwise, move predecessor
            else:
                pred = pred.next 
                
            # move forward
            head = head.next
            
        return sentinel.next        
                
        
        