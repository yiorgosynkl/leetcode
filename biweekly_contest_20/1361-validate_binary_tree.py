################################################################
# Project           : leetcode
# Program name      : 1361-validate_binary_tree.py
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200224
# Description       : return true if and only if all the given nodes form exactly one valid binary tree
################################################################

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        queue = [0]
        explored = set([])
        valid = True
        while queue:
            # print('queue: ', queue)
            # print('explored: ', explored)
            head = queue.pop(0)
            if head in explored: 
                valid = False
                break
            left = leftChild[head]
            right = rightChild[head]
            if left >= 0: queue.append(left)
            if right >= 0: queue.append(right)
            explored.add(head)
        if (valid) and (len(explored) == n):
            return True
        return False