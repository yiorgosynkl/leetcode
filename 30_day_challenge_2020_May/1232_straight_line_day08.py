################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200508
# Problem link      : https://leetcode.com/problems/check-if-it-is-a-straight-line/
################################################################

class Solution:
    # to avoid dividing by zero, use multiplication
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True
    
    # one liner (solution from rock)
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)
    
    def checkStraightLine(self, coords: List[List[int]]) -> bool:
        if len(coords) < 2:
            return False
        def calc_slope(alpha, bravo, x_down):
            (alpha_x, alpha_y) = alpha
            (bravo_x, bravo_y) = bravo
            if x_down and (alpha_x - bravo_x) != 0:
                return (alpha_y - bravo_y) / (alpha_x - bravo_x)
            elif (alpha_y - bravo_y):
                return (alpha_x - bravo_x) / (alpha_y - bravo_y)
            else:
                # print('ERROR')
                return None
        
        base = coords.pop()
        temp = coords.pop()
        x_down = base[0] - temp[0] == 0
        slope = calc_slope(base, temp, x_down)
        while coords:
            temp = coords.pop()
            if slope != calc_slope(base, temp, x_down):
                return False
        return True
        