################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201102
# Problem link      : https://leetcode.com/problems/insertion-sort-list/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        head2 = ListNode(0) # pointer to new lists head
        node, next_node = head, head
        while node:
            next_node = node.next # node = ListNode(head.val)
            tmp = head2
            while tmp.next and tmp.next.val < node.val:  
                tmp = tmp.next
            tmp.next, node.next = node, tmp.next
            node = next_node
        return head2.next

#     # official solution
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         pseudo_head = ListNode()

#         curr = head
#         while curr:
#             # At each iteration, we insert an element into the resulting list.
#             prev_node = pseudo_head
#             next_node = prev_node.next
#             # find the position to insert the current node
#             while next_node:
#                 if curr.val < next_node.val:
#                     break
#                 prev_node = next_node
#                 next_node = next_node.next

#             next_iter = curr.next
#             # insert the current node to the new list
#             curr.next = next_node
#             prev_node.next = curr

#             # moving on to the next iteration
#             curr = next_iter

#         return pseudo_head.next