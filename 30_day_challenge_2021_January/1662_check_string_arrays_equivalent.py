################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210108
# Problem link      : https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
################################################################

class Solution:
    # def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    #     return ''.join(word1) == ''.join(word2)
    
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def gen(word: List[str]):
            for s in word:
                for c in s:
                    yield c
            yield None
        return all(c1 == c2 for c1, c2 in zip(gen(word1), gen(word2)))
        # for c1, c2 in zip(gen(word1), gen(word2)):
        #     if c1 != c2:
        #         return False
        # return True
