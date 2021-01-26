################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210117
# Problem link      : https://leetcode.com/problems/count-sorted-vowel-strings/
################################################################

from math import comb

class Solution:
    # #
    # # explanation of dp solution
    # # n: length of string, c: number of chars available in string (we always search c = 5)
    # # f(n, c) = f(n-1, c) + f(n-1, c-1) + ... + f(n-1, 1), first f() when I put 'a' as first letter, last f() when I put 'u' as first letter
    # # f(n, 1) = 1, when I have one character I can make one distinct word
    # # f(1, c) = c, when I have c characters I can make c distince one letter words
    # #
    # # f(n, c) = f(n-1, c) + f(n-1, c-1) + ... + f(n-1, 1) = f(n-1, c) + f(n, c-1) # shorten recursive function
    # def countVowelStrings(self, n: int) -> int:
    #     dp = [[1, 0, 0, 0, 0] for _ in range(n)]
    #     dp[0] = [1, 2, 3, 4, 5]
    #     for i in range(1, n):
    #         for j in range(1, 5):
    #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #     print(dp)
    #     return dp[n-1][4]
      
    # @yiorgosynkl, less memory
    # def countVowelStrings(self, n: int) -> int:
    #     dp = [1,2,3,4,5]
    #     for i in range(2, n+1):
    #         for j in range(1, 5):
    #             dp[j] = dp[j-1] + dp[j]
    #     return dp[4]
    
    
#     # @lee215 solutions
#     # top down (using memoization)
#     def countVowelStrings(self, n):
#         seen = {}
#         def dp(n, k):
#             if k == 1 or n == 1: return k
#             if (n, k) in seen:
#                 return seen[n, k]
#             seen[n, k] = sum(dp(n - 1, k) for k in range(1, k + 1))
#             return seen[n, k]
#         return dp(n, 5)
    
    # # bottom up
    # def countVowelStrings(self, n):
    #     dp = [[1] * 5] + [ [1]+[0]*4 for i in range(n)]
    #     for i in range(1, n+1):
    #         for k in range(1, 5):
    #             dp[i][k] = dp[i][k - 1] + dp[i - 1][k]
    #     return dp[n][4]
    
    # bottom up, less memory    
    def countVowelStrings(self, n):
        dp = [1] * 5 
        for i in range(1, n+1):
            for k in range(1, 5):
                dp[k] += dp[k - 1]
        return dp[4]

#     def countVowelStrings(self, n: int) -> int:
#         dp = [1] * 5
#         for i in range(n):
#             dp = accumulate(dp)
#         return list(dp)[-1]
    
    # # combinatorics O(1)
    # # we have got n characters and we are going to insert 4 | (that means the ranges for each letter)
    # # that means we have n + 4 binary string and we have to select exactly 4 aces (1 == |) to split the 0 characters (which are n in amount) into 5 different teams 
    # # (leftmost team of 0s will get letter 'a', ..., rightmost team of 0s will get letter 'u')
    # def countVowelStrings(self, n):
    #     return (n + 1) * (n + 2) * (n + 3) * (n + 4) / 24
