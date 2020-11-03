################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201103
# Problem link      : https://leetcode.com/problems/consecutive-characters/
################################################################

class Solution:
    def maxPower(self, s: str) -> int:
        best, cnt, prv = 0, 0, None
        for cur in s:
            cnt = cnt + 1 if cur == prv else 1
            best = max(best, cnt)
            prv = cur
        return best
    
    # # @lee215 one liner
    # def maxPower(self, s: str) -> int:
    #     return max(len(list(b)) for a, b in itertools.groupby(s))

    # # @rock
    # def maxPower(self, s: str) -> int:
    #     cnt = ans = 1
    #     for i in range(1, len(s)):
    #         if s[i] == s[i - 1]:
    #             cnt += 1
    #             ans = max(cnt, ans)
    #         else:
    #             cnt = 1
    #     return ans
