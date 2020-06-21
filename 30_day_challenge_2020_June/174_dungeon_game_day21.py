################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200621
# Problem link      : https://leetcode.com/problems/dungeon-game/
################################################################

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dungeon[m-1][n-1] = max(0, -dungeon[m-1][n-1])
        for j in reversed(range(n-1)):
            dungeon[m-1][j] = max(0,dungeon[m-1][j+1] - dungeon[m-1][j])
        for i in reversed(range(m-1)):
            dungeon[i][n-1] = max(0,dungeon[i+1][n-1] - dungeon[i][n-1])
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                dungeon[i][j] = min(max(0,dungeon[i][j+1] - dungeon[i][j]), max(0,dungeon[i+1][j] - dungeon[i][j]))
        print(dungeon)
        return dungeon[0][0]+1