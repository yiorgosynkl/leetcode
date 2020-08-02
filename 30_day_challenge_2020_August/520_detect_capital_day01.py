################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200801
# Problem link      : https://leetcode.com/problems/detect-capital/
################################################################

class Solution:
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()

#     def detectCapitalUse(self, word: str) -> bool:
#         if len(word) < 2:
#             return True
#         if word[0].islower():
#             for ch in word:
#                 if ch.isupper():
#                     return False
#             return True
#         sec_lower = word[1].islower()
#         for i in range(2, len(word)):
#             if sec_lower != word[i].islower():
#                 return False
#         return True
    
#     def detectCapitalUse(self, word):
#         c = 0
#         for i in word:
#             if i == i.upper():
#                 c += 1
#         return c == len(word) or (c == 1 and word[0] == word[0].upper()) or c == 0 
