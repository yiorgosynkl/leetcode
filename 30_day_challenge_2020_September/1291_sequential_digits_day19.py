################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200919
# Problem link      : https://leetcode.com/problems/sequential-digits/
################################################################

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        nums = [int(s[st:st+lg]) for lg in range(1, 10) for st in range(0, 10-lg)] # start, length
        return list(filter(lambda x: low <= x < high, nums))
