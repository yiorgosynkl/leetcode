################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200516
# Problem link      : https://leetcode.com/contest/biweekly-contest-26/problems/consecutive-characters/
################################################################

class Solution:
    def maxPower(self, s: str) -> int:
        if s == "":
            return 0
        ans = 1
        count = 1 
        for i in range(1, len(s)):
            count = count + 1 if s[i] == s[i-1] else 1
            ans = max(ans, count)
        return ans
        