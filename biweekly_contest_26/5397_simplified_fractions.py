################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200516
# Problem link      : https://leetcode.com/contest/biweekly-contest-26/problems/simplified-fractions/
################################################################

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []   
        
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x 
        
        ans = []
        for down in range(2, n+1):
            for up in range(1, down):
                if gcd(down, up) == 1:
                    ans.append(str(up) + "/" + str(down))
        return ans
