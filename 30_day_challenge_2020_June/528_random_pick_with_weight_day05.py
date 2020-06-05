################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200605
# Problem link      : https://leetcode.com/problems/random-pick-with-weight/
################################################################

# from numpy.random import choice
import itertools
import bisect

class Solution:
#     def __init__(self, weights: List[int]):
#         self.ssum = sum(weights)
#         self.p = [w/self.ssum for w in weights]
#         self.limit = len(weights)

#     def pickIndex(self) -> int:
#         return choice(self.limit, size=1, replace=True, p=self.p)[0]
    
    def __init__(self, w):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))

#     slow
#     def __init__(self, w: List[int]):
#         self.roulette = []
#         for idx, num in enumerate(w):
#             self.roulette.extend([idx] * num)
#         self.upper = len(self.roulette) - 1

#     def pickIndex(self) -> int:
#         return self.roulette[randint(0, self.upper)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()