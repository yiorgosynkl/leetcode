################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200913
# Problem link      : https://leetcode.com/problems/insert-interval/
################################################################

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sn, en = newInterval
        ss, ee = sn, en # initialize values, start and end of new entry
        ans = []
        intervals = intervals[::-1]
        while intervals and (intervals[-1][1] < sn): # no interlapping with newInterval
            ans.append(intervals.pop())
        while intervals and not (intervals[-1][1] < sn or en < intervals[-1][0]):
            s, e = intervals.pop()
            ss, ee = min(ss, s), max(ee, e)
        ans.append([ss, ee])
        while intervals and (en < intervals[-1][0]): # no interlapping with newInterval
            ans.append(intervals.pop())
        return ans
    
#     # @Stefan Pochmann 
#     def insert(self, intervals, newInterval):
#         s, e = newInterval[0], newInterval[1]
#         left = [i for i in intervals if i[1] < s]
#         right = [i for i in intervals if i[0] > e]
#         if left + right != intervals:
#             s = min(s, intervals[len(left)][0])
#             e = max(e, intervals[~len(right)][1]) # ~ means revert every bit, therefore, ~x means -x-1
#         return left + [[s, e]] + right
    
#     def insert(self, intervals, newInterval):
#         s, e = newInterval[0], newInterval[1]
#         parts = merge, left, right = [], [], []
#         for i in intervals:
#             parts[(i[1] < s) - (i[0] > e)].append(i) # wtf
#         if merge:
#             s = min(s, merge[0][0])
#             e = max(e, merge[-1][1])
#         return left + [[s, e]] + right