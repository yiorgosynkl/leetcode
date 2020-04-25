################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200409
# Problem link      : https://leetcode.com/problems/backspace-string-compare/
################################################################

def stringy(S: str) -> str:
    stack = []
    for c in S:
        if c !='#':
            stack.append(c)
        elif stack:
            stack.pop()
    return ''.join(stack)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return stringy(S) == stringy(T)
