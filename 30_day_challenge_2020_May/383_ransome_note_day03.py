################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200503
# Problem link      : https://leetcode.com/problems/ransom-note/
################################################################

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cNote = Counter(ransomNote)
        cMag = Counter(magazine)
        for ch, times in cNote.items():
            if cMag[ch] < times:
                return False
        return True

#     StefanPochmann
#     def canConstruct(self, ransomNote, magazine):
#         return not collections.Counter(ransomNote) - collections.Counter(magazine)
