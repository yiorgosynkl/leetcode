################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200408
# Problem link      : https://leetcode.com/problems/middle-of-the-linked-list/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        count = 1
        while fast.next != None:
            count += 1
            fast = fast.next
            if count % 2 == 0:
                slow = slow.next
        return slow
        
# class Solution(object):
#     def middleNode(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next       
#         return slow