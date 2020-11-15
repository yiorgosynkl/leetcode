################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201103
# Problem link      : https://leetcode.com/problems/poor-pigs/
################################################################

from math import log, ceil

class Solution:
    # n : number of buckets, md: minutesToDie, mt: minutesToTest
    def poorPigs(self, n: int, md: int, mt: int) -> int:
        t = mt // md # num of tests
        return ceil(log(n,t+1)) # (T+1)^x >= N  ==>  x >= log(N, T+1)
        
        
    # first thought is one pig for each bucket
    # second thought is pigs for n-ary search, one dies, then recursive
    # final thought encodings for each bucket in t-ary system and amount of pigs equal to digits
    # see explanations in website