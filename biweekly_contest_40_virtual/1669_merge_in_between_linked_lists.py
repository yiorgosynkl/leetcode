################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201211
# Problem link      : https://leetcode.com/problems/merge-in-between-linked-lists/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # time: O(n), space: O(1), where n = size(list1) + size(list2).
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p1, p2 = list1, list2
        for _ in range(a-1):
            p1 = p1.next
        s1 = p1 # first stop point
        for _ in range(b-a+2):
            p1 = p1.next
        s2 = p1 # second stop point
        s1.next = p2 
        while p2.next != None:
            p2 = p2.next
        p2.next = s2 # connect stop points and list
        return list1
            
        