################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201211
# Problem link      : https://leetcode.com/problems/maximum-repeating-substring/
################################################################

class Solution:
    # time: O(n ^ 2), space: O(n),  ( could also do binary search O(n ^ logn) )
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 1
        while True:
            if word*k not in sequence:
                break
            k += 1
        return k - 1

    # # oneliner
    # def maxRepeating(self, s, w):
    #     return sum(w * i in s for i in range(1, len(s)//len(w)+1))

#     # @lenchen1112, KMP Algorithm
#     def maxRepeating(self, sequence: str, word: str) -> int:
#         s, w = len(sequence), len(word)
#         max_repeat = s // w
#         failure = [0] * (w * max_repeat + 1)
#         repeat_words = word * max_repeat + '$'
#         result = 0

#         j = 0
#         for i in range(1, len(repeat_words)):
#             while j > 0 and repeat_words[j] != repeat_words[i]:
#                 j = failure[j-1]
#             j += repeat_words[j] == repeat_words[i]
#             failure[i] = j

#         j = 0
#         for i, c in enumerate(sequence):
#             while j > 0 and repeat_words[j] != c:
#                 j = failure[j-1]
#             j += repeat_words[j] == c
#             result = max(result, j // w)

#         return result