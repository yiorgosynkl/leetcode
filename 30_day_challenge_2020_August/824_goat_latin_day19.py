################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200819
# Problem link      : https://leetcode.com/problems/goat-latin/
################################################################

class Solution:
    def toGoatLatin(self, S: str) -> str:
        def convert(word, num):
            end = 'maa' + 'a'*num
            if not word: 
                return ending
            vowels = ('a','e','i','o','u','A','E','I','O','U')
            if word[0].startswith(vowels): 
                return word + end
            else:
                return word[1:] + word[0] + end
        return ' '.join([convert(word,num) for num, word in enumerate(S.split())])

#     # @lee215
#     def toGoatLatin(self, S):
#         vowel = set('aeiouAEIOU')
#         def latin(w, i):
#             if w[0] not in vowel:
#                 w = w[1:] + w[0]
#             return w + 'ma' + 'a' * (i + 1)
#         return ' '.join(latin(w, i) for i, w in enumerate(S.split()))
    
#     # oneliner
#     def toGoatLatin(self, S):
#         return ' '.join((w if w[0].lower() in 'aeiou' else w[1:] + w[0]) + 'ma' + 'a' * (i + 1) for i, w in enumerate(S.split()))

