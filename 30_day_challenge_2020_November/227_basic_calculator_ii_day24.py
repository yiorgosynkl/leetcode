################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201124
# Problem link      : https://leetcode.com/problems/basic-calculator-ii/
################################################################

class Solution:
#     def calculate(self, s: str) -> int:
#         sk = deque([]) # stack
#         s = s.replace(' ', '')
#         i = 0
#         while i < len(s):
#             if s[i] in {'+', '-', '*', '/'}:
#                 sk.append(s[i])
#                 i += 1
#             num = ''
#             while i < len(s) and s[i] not in {'+', '-', '*', '/'}:
#                 num += s[i]
#                 i += 1
#             num = int(num)
#             if sk and sk[-1] in {'*', '/'}: # multiply or divide immidiately
#                 do = sk.pop()
#                 num2 = sk.pop()
#                 if do == '*':
#                     num = num2 * num
#                 else: # do == '/'
#                     num = num2 // num
#             sk.append(num)
#         ans = sk.popleft()
#         while sk: # then subtract or add
#             do = sk.popleft()
#             num = sk.popleft()
#             if do == '-':
#                 ans -= num
#             else: # do == '+'
#                 ans += num 
#         return ans
    
    def calculate(self, s):
        if not s: return '0'
        stack, num, sign = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord('0')
            if s[i] in "+-*/" or i == len(s)-1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    stack.append(tmp//num+1 if tmp//num < 0 and tmp%num != 0 else tmp//num)
                sign = s[i]
                num = 0
        return sum(stack)
