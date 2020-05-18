################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200518
# Problem link      : https://leetcode.com/problems/permutation-in-string/
################################################################

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        target_hash = 0 # hash of s1 charachters
        window_hash = 0 # hash of rolling window of length len(s1) in s2 characters
        for i in range(len(s1) - 1):
            target_hash += hash(s1[i])
            window_hash += hash(s2[i])
        target_hash += hash(s1[len(s1) - 1])    

        for i in range(len(s1) - 1, len(s2)):
            window_hash += hash(s2[i])
            if target_hash == window_hash:
                return True
            window_hash -= hash(s2[i - len(s1) + 1])            
        return False

    # solution by awice
    # def checkInclusion(self, s1, s2):
    #     A = [ord(x) - ord('a') for x in s1]
    #     B = [ord(x) - ord('a') for x in s2]
        
    #     target = [0] * 26
    #     for x in A:
    #         target[x] += 1
        
    #     window = [0] * 26
    #     for i, x in enumerate(B):
    #         window[x] += 1
    #         if i >= len(A):
    #             window[B[i - len(A)]] -= 1
    #         if window == target:
    #             return True
    #     return False