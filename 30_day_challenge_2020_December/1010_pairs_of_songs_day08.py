################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201208
# Problem link      : https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
################################################################

class Solution:
    # def numPairsDivisibleBy60(self, time: List[int]) -> int:
    #     mods = [0]*60
    #     for t in time:
    #         mods[t % 60] += 1
    #     ans = sum(mods[t]*mods[60-t] for t in range(1,30)) + mods[30]*(mods[30]-1)//2 + mods[0]*(mods[0]-1)//2
    #     return ans 

    # @lee215
    def numPairsDivisibleBy60(self, time):
        c = [0] * 60
        res = 0
        for t in time:
            res += c[-t % 60]
            c[t % 60] += 1
        return res