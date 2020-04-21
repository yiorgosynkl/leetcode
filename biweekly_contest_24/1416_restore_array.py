################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200418
# Problem link      : https://leetcode.com/contest/biweekly-contest-24/problems/restore-the-array/
################################################################

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = []
        for i in reversed(range(len(s))):
            if s[i] == '0':
                dp.append(0)
            else:
                size = 1
                count = 0
                while i + size < len(s) and int(s[i:i+size]) <= k:
                    count += dp[-size]
                    size += 1
                if i + size == len(s) and int(s[i:i+size]) <= k:
                    count += 1
                dp.append(count % (10**9 + 7))
        return dp[-1]
