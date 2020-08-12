################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200812
# Problem link      : https://leetcode.com/problems/pascals-triangle-ii/
################################################################

import math 

class Solution:
    # recursive solution
    # def getRow(self, rowIndex: int) -> List[int]:
    #     if rowIndex == 0: return [1]
    #     if rowIndex == 1: return [1, 1]
    #     prev = self.getRow(rowIndex - 1)
    #     return [1] + [i+j for i,j in zip(prev[:-1], prev[1:])] + [1]    
    
    # def getRow(self, rowIndex: int) -> List[int]:
    #     prv, nxt = [0,1,0], [0]
    #     for _ in range(rowIndex):
    #         for i in range(len(prv) - 1):
    #             nxt.append(prv[i] + prv[i+1])
    #         nxt.append(0)
    #         prv, nxt = nxt, [0]
    #     return prv[1:-1]
                            

    # math solution
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]*(rowIndex+1)
        for i in range(0,rowIndex+1):
            row[i] = (math.factorial(rowIndex))//(math.factorial(i)*math.factorial(rowIndex-i))
        return row