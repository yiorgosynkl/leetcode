################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201101
# Problem link      : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def getDecimalValue(self, head: ListNode) -> int:
    #     ans = 0
    #     while head:
    #         ans <<= 1 # shift left (that means multiply by two)
    #         ans |= head.val # bitwise or with 0 or 1
    #         head = head.next
    #     return ans
    
    # @rock, walrus operator
    def getDecimalValue(self, head: ListNode) -> int:
        ans = head.val
        while head := head.next:
            ans = ans << 1 | head.val
        return ans