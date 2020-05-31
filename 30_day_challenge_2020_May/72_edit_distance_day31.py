################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200531
# Problem link      : https://leetcode.com/problems/edit-distance/
################################################################

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)] 
        for i in range(0, rows+1):
            dp[i][0] = i
        for j in range(0, cols+1):
            dp[0][j] = j
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else 1 + min(dp[i-1][j-1], dp[i][j-1],dp[i-1][j])
        return dp[rows][cols]            
        