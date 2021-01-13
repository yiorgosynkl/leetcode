################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210113
# Problem link      : https://leetcode.com/problems/boats-to-save-people/
################################################################

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ps = sorted(people)
        boats, lo, hi = 0, 0, len(ps) - 1
        while lo <= hi:
            if lo < hi and ps[lo] + ps[hi] <= limit:
                lo += 1
            hi -= 1
            boats += 1
        return boats
                
    # @lee215
    def numRescueBoats(self, people, limit):
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit: j -= 1
            i += 1
        return i