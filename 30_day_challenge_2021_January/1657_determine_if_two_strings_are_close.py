################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210122
# Problem link      : https://leetcode.com/problems/determine-if-two-strings-are-close/
################################################################

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # requirements:
        # * should contain the same exactly the same symbols
        # * should contain the same multiset of frequencies of numbers
        c1, c2 = Counter(word1), Counter(word2)
        return set(c1.keys()) == set(c2.keys()) and sorted(list(c2.values())) == sorted(list(c1.values()))        
    
    # @DBabichev
    def closeStrings(self, w1, w2):
        return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())
