################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201118
# Problem link      : https://leetcode.com/problems/merge-intervals/
################################################################

class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     intervals = sorted(intervals, key=lambda x: (x[0],x[1]))
    #     ans, idx = [], 0
    #     while idx < len(intervals):
    #         start, end = intervals[idx][0], intervals[idx][1]
    #         idx += 1
    #         while idx < len(intervals):
    #             if intervals[idx][0] <= end:
    #                 end = max(intervals[idx][1], end)
    #                 idx += 1
    #             else:
    #                 break
    #         ans.append([start, end])
    #     return ans

    # @StefanPochmann
    # sort intervals be begining, if one overlaps with the previous combine them
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key = lambda i: i[0]):
            if out and i[0] <= out[-1][1] :
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out.append(i)
        return out
