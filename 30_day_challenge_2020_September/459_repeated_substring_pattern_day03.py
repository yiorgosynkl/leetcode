################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200903
# Problem link      : https://leetcode.com/problems/repeated-substring-pattern/
################################################################

class Solution:
    # def repeatedSubstringPattern(self, s: str) -> bool:
    #     l, t = 1, 1 # length of substring, times it repeats
    #     while 2*l <= len(s):
    #         if len(s) % l:
    #             l, t = l + 1, 1
    #         else: # equal to zero
    #             while (t+1)*l <= len(s) and s[0:l] == s[t*l:(t+1)*l]:
    #                 t += 1
    #             if t*l == len(s):
    #                 return True
    #             else:
    #                 l, t = t*l + 1, 1
    #     return False
    # find substring, find how many times it repeats
    # if it stops repeating create the new substring at that point it stopped 
    
    # one liner (double len of s, remove first and last charachters and search for s in that)
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (2*s)[1:-1]
        # this is common trick to figure out if stringA is a rotated version of stringB
        # in this case we have a periodic string s so we check if s is a rotation of itself
        # [1:-1] forces the shift r to have value 0 < r < len(s)
        