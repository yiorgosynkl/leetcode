################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200501
# Problem link      : https://leetcode.com/problems/jewels-and-stones/
################################################################

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)

    # J.count is the function that gets each element of S as input
    # def numJewelsInStones(self, J, S):
    #     return sum(map(J.count, S)) 

    # def numJewelsInStones(self, J, S):
    #     return sum(map(S.count, J)) 