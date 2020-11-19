################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201116
# Problem link      : https://leetcode.com/problems/decode-string/
################################################################

import re

class Solution:
    # def decodeString(self, s: str) -> str:
    #     prv, nxt, ans = 0, 0, ''
    #     while nxt < len(s):
    #         if s[nxt].isdigit() == False: # find charachters
    #             while nxt < len(s) and s[nxt].isdigit() == False:
    #                 nxt += 1
    #             ans += s[prv:nxt]
    #             prv = nxt
    #         else:  # s[nxt].isdigit() == True (nxt < len(s) will always be true) # find numbers of this level
    #             while s[nxt].isdigit() == True: 
    #                 nxt += 1
    #             times = int(s[prv:nxt])
    #             prv = nxt = nxt + 1 # skip char '['
    #             bracks = 1
    #             while bracks > 0:
    #                 nxt += 1
    #                 if s[nxt] == '[': bracks += 1
    #                 if s[nxt] == ']': bracks -= 1
    #             ans += times * self.decodeString(s[prv:nxt])
    #             prv = nxt = nxt + 1 # skip char ']'
    #     return ans
    
    # # @StefanPochmann fewliner
    # def decodeString(self, s):
    #     while '[' in s:
    #         s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
    #     return s
    
    # stack logic
    def decodeString(self, s):
        stack = []
        curNum, curStr = 0, ''
        for c in s:
            if c == '[':
                stack.append(curStr)
                stack.append(curNum)
                curNum, curStr = 0, ''
            elif c == ']':
                num = stack.pop()
                prvStr = stack.pop()
                curStr = prvStr + num*curStr
            elif c.isdigit():
                curNum = 10*curNum + int(c)
            else: # character
                curStr += c
        return curStr
