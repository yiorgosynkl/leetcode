################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200915
# Problem link      : https://leetcode.com/problems/length-of-last-word/
################################################################

class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     return len(([''] + [ss for ss in s.split(' ') if ss])[-1])
    
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(' ').split(' ')[-1])

    # def lengthOfLastWord(self, s: str) -> int:
    #     end = len(s) - 1
    #     while end > 0 and s[end] == ' ': end -= 1
    #     beg = end
    #     while beg >= 0 and s[beg] != ' ': beg -= 1
    #     return end - beg