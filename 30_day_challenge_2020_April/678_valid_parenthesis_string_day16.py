def convert(ch):
    if ch == '(':
        return ')'
    elif ch == ')':
        return '('
    else:
        return ch
    
def check(s: str):
    count = 0
    for ch in s:
        count += -1 if ch == ')' else 1
        if count < 0: 
            return False
    return True

class Solution:
    def checkValidString(self, s: str) -> bool:
        s_rev = ''.join([convert(i) for i in s[::-1]])
        return (check(s) and check(s_rev))
    
# nice solution
# def checkValidString(self, s):
#         cmin = cmax = 0
#         for i in s:
#             if i == '(':
#                 cmax += 1
#                 cmin += 1
#             if i == ')':
#                 cmax -= 1
#                 cmin = max(cmin - 1, 0)
#             if i == '*':
#                 cmax += 1
#                 cmin = max(cmin - 1, 0)
#             if cmax < 0:
#                 return False
#         return cmin == 0
        