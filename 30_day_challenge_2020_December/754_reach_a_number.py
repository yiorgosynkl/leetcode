
################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201228
# Problem link      : https://leetcode.com/problems/reach-a-number/
################################################################

class Solution:
    # def reachNumber(self, target: int) -> int:
    #     LMT = 10**9 + 1
    #     nxt, c = set([0]), 1
    #     while True:
    #         nxt = set(i+c for i in nxt if i+c < LMT).union(set(i-c for i in nxt if i - c > -LMT))
    #         if target in nxt:
    #             return c
    #         c += 1

    # def reachNumber(self, target: int) -> int:
    #     k, s, t, d = 0, 0, abs(target), 0
    #     # sum should surpass target
    #     # the delta (sum - target) should be divisible by 2 so we can turn some signs negative
    #     while s < t or d % 2 == 1: 
    #         k += 1
    #         s += k
    #         d = s-t
    #     return k
        
    # def reachNumber(self, target):
    #     t = abs(target)
    #     n = math.floor(math.sqrt(2*t))
    #     while True:
    #         delta = ((n+1)*n)/2 - t 
    #         if delta >= 0:  
    #             if delta%2==0:
    #                 return n
    #         n+=1
        
    # time: O(1)
    def reachNumber(self, target):
        bound = ceil(sqrt(2*abs(target)+0.25) - 0.5)
        if target % 2 == 0:
            if bound % 4 == 1: bound += 2
            if bound % 4 == 2: bound += 1
        else:
            if bound % 4 == 3: bound += 2
            if bound % 4 == 0: bound += 1       
        return bound
        