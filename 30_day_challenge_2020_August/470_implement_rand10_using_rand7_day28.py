################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200828
# Problem link      : https://leetcode.com/problems/implement-rand10-using-rand7/
################################################################

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    # def rand10(self):
    #     """
    #     :rtype: int
    #     """
    #     choices = [1 for _ in range(10)] # all choices enabled
    #     while sum(choices) != 1:
    #         rands = [rand7() for _ in range(10)]
    #         maxim = max([choices[i] * rands[i] for i in range(10)])
    #         choices = [choices[i] if rands[i] >= maxim else 0 for i in range(10)] # remove choices with low random number        
    #     return choices.index(1) + 1
        
    def rand10(self):
        """
        :rtype: int
        """
        ans = 41
        while ans > 40:
            ans = (rand7() - 1) * 7 + rand7() # from 1 to 49
        return ans % 10 + 1 # 49/40*2 = 2.45 calls of rand7() per rand10().
        