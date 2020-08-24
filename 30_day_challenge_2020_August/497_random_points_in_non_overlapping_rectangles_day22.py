################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200822
# Problem link      : https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
################################################################

import bisect
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = []
        self.n_points = 0
        self.limits = []
        for x1, y1, x2, y2 in rects:
            self.rects.append((x1,y1,x2,y2))
            self.n_points += (x2-x1+1)*(y2-y1+1)
            self.limits.append(self.n_points)

    def pick(self) -> List[int]:
        num = random.randint(0, self.n_points-1)
        idx = bisect.bisect_right(self.limits, num)
        x1, y1, x2, y2 = self.rects[idx]
        num, dy = (self.limits[idx] - 1) - num, y2 - y1 + 1
        x3, y3 = x1 + (num // dy), y1 + (num % dy)
        return [x3, y3]

# second solution 
class Solution:

    def __init__(self, rects):
        self.rects, self.ranges, sm = rects, [], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self):
        x1, y1, x2, y2 = self.rects[bisect.bisect_left(self.ranges, random.randint(1, self.ranges[-1]))]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()