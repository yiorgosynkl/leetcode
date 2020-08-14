################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200814
# Problem link      : https://leetcode.com/problems/longest-palindrome/
################################################################

class Solution:
    # def longestPalindrome(self, s: str) -> int:
    #     odds = set()
    #     count = 0
    #     for i in s:
    #         if i in odds:
    #             odds.remove(i)
    #             count += 2
    #         else:
    #             odds.add(i)
    #     return count + 1 if odds else count
    #     # return len(s) - len(odds) + 1 if odds else len(s)
        
    # @Stefan Pochmann
    def longestPalindrome(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)

        