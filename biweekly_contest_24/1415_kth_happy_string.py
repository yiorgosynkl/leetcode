################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200418
# Problem link      : https://leetcode.com/contest/biweekly-contest-24/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
################################################################

from itertools import product

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ['a','b','c']
        count = 0
        for ss in product('abc', repeat=n):
            valid = True
            for i in range(1, len(ss)):
                if ss[i-1] == ss[i]:
                    valid = False
                    break
            if valid:
                count += 1
            if count == k:
                return ''.join(ss)
        return ''

# solution by huzecong
# class Solution:
#     def getHappyString(self, n: int, k: int) -> str:
#         strings = itertools.product(*([['a', 'b', 'c']] * n))
#         cnt = 0
#         for s in strings:
#             if any(a == b for a, b in zip(s, s[1:])):
#                 continue
#             cnt += 1
#             if cnt == k:
#                 return "".join(s)
#         return ''
