################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201110
# Problem link      : https://leetcode.com/problems/flipping-an-image/
################################################################

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]: 
        return [[int(i == 0) for i in reversed(l)] for l in A]
        # return [[i ^ 1 for i in reversed(row)] for row in A]
        # return [[1-i for i in row[::-1]] for row in A]

    # # official solution
    # def flipAndInvertImage(self, A):
    #     for row in A:
    #         for i in xrange((len(row) + 1) / 2):
    #             """
    #             In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
    #             helps us find the i-th value of the row, counting from the right.
    #             """
    #             row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
    #     return A