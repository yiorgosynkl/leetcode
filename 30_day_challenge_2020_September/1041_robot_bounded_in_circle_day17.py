################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200917
# Problem link      : https://leetcode.com/problems/robot-bounded-in-circle/
################################################################

class Solution:
    # def isRobotBounded(self, ins: str) -> bool:
    #     # change in direction => cirlce
    #     if (ins.count('R') - ins.count('L')) % 4 != 0:     
    #         return True
    #     # no change in position => circle
    #     moves, place, i = [[0, 1], [1, 0], [0, -1], [-1, 0]], [0, 0], 0
    #     for c in ins:
    #         if c == 'R': i = (i+1) % 4
    #         elif c == 'L': i = (i-1) % 4
    #         else: place = [sum(x) for x in zip(place, moves[i])]
    #     if place == [0, 0]:
    #         return True
    #     return False
        
    # @lee215
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx # rotate the move vector 90 (or rotate NESW horizon by -90 and you see the formula appear)
            if i == 'L': dx, dy = -dy, dx # rotate the move vector -90 (or rotate NESW horizon by +90 and you see the formula appear)
            if i == 'G': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)