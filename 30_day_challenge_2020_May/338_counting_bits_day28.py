################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200528
# Problem link      : https://leetcode.com/problems/counting-bits/
################################################################

class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        while len(ans) <= num:
            ans = ans + [i+1 for i in ans]
        return ans[:num+1]

    # def countBits(self, num: int) -> List[int]:
    #     def ones(num):
    #         return (num%2 + ones(num//2)) if num else 0
    #     return [ones(i) for i in range(num+1)]