################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200706
# Problem link      : https://leetcode.com/problems/plus-one/
################################################################

class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     carry = 1
    #     for i in reversed(range(len(digits))):
    #         num = digits[i] + carry
    #         digits[i], carry = num % 10, num // 10
    #     if carry:
    #         digits.insert(0, 1)
    #     return digits
    
    # recursive
    def plusOne(self, dgs: List[int]) -> List[int]:
        return [1] if not dgs else self.plusOne(dgs[:-1]) + [0] if dgs[-1] == 9 else dgs[:-1] + [dgs[-1] + 1]