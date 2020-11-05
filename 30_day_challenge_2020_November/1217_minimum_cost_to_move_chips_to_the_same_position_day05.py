################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201105
# Problem link      : https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
################################################################

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = sum(p%2 for p in position)
        evens = len(position) - odds
        return min(odds, evens)
        