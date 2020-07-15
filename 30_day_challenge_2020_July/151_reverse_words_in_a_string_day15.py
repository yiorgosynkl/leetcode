################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200715
# Problem link      : https://leetcode.com/problems/reverse-words-in-a-string/
################################################################

class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join([ss for ss in s.split(' ')[::-1] if ss != ''])
        return ' '.join(s.split()[::-1])
