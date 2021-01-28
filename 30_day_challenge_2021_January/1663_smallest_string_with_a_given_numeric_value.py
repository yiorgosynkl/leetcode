################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210128
# Problem link      : https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
################################################################

class Solution:
    # def getSmallestString(self, n: int, k: int) -> str:
    #     beg = ''
    #     while n > 1 and (n-1)*26 >= (k-1):
    #         beg += 'a'
    #         n -= 1
    #         k -= 1
    #     end = 'z' * (n-1)
    #     k -= 26*(n-1)
    #     n = 1
    #     mid = chr(ord('a')+k) 
    #     return beg + mid + end
    
    # # @rock
    # def getSmallestString(self, n: int, k: int) -> str:
    #     k -= n  # suppose that all are 'a', so now the cost left to cover is k-n
    #     ca, i = ['a'] * n, n - 1
    #     while i >= 0 and k > 0:
    #         cost = min(k, 25) # starting from the end give maximum possible cost to the last letter 
    #         ca[i] = chr(ord('a') + cost)
    #         k -= cost
    #         i -= 1
    #     return ''.join(ca)    

    # @rock   
    def getSmallestString(self, n: int, k: int) -> str:
        # with k - n we switch to 0-index notation, now divmod gives us the answer immidately
        z, r = divmod(k - n, 25)    # z: numbers of z neccesary, r is the numeric value of the middle letter
        return ('' if z == n else 'a' * (n - z - 1) + chr(ord('a') + r)) + 'z' * z

        