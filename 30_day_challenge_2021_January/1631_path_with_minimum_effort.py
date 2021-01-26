################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210126
# Problem link      : https://leetcode.com/problems/path-with-minimum-effort/
################################################################

class Solution:
#     # binary search of limit
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         rs, cs = len(heights), len(heights[0])
#         mx, mn = -1, 10 ** 6
#         for r in range(rs):
#             for c in range(cs):
#                 mn = min(mn, heights[r][c])
#                 mx = max(mx, heights[r][c])
#         dif = mx - mn
  
#         # mx = max(heights[r][c] for r in range(rs) for c in range(cs))
#         # mn = min(heights[r][c] for r in range(rs) for c in range(cs))
#         # dif = mx - mn
        
#         if rs == 1 and cs == 1:
#             return 0
        
#         def explore(lim):
#             q = [(0, 0)]
#             seen = set()
#             while q:
#                 qq = []
#                 for i, j in q:
#                     for k, l in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
#                         if 0 <= k < rs and 0 <= l < cs and (k,l) not in seen and abs(heights[i][j] - heights[k][l]) <= lim:
#                             if (k,l) == (rs-1, cs-1):
#                                 return True
#                             qq.append((k,l))
#                     seen.add((i,j))
#                 q = qq
#             return False
        
#         # linear search
#         # for lim in range(dif+1):
#         #     if explore(lim):
#         #         return lim
#         # return -1
        
#         # binary search
#         lo, hi = 0, dif
#         while lo < hi:
#             mid = (lo + hi) // 2
#             if explore(mid):
#                 hi = mid
#             else:
#                 lo = mid + 1
#         return lo

    
#     # @rock
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:

#         def isPath(effort: int) -> bool:
#             seen, dq = {(0, 0)}, deque([(0, 0)])
#             while dq:
#                 x, y = dq.popleft()
#                 if (x, y) == (len(heights) - 1, len(heights[0]) - 1):
#                     return True
#                 for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
#                     if len(heights) > r >= 0 <= c < len(heights[0]) and abs(heights[r][c] - heights[x][y]) <= effort and (r, c) not in seen:
#                         seen.add((r, c))
#                         dq.append((r, c))
#             return False            
        
#         lo, hi = 0, 10 ** 6
#         while lo < hi:
#             effort = lo + hi >> 1
#             if isPath(effort):
#                 hi = effort
#             else:
#                 lo = effort + 1
#         return lo
    
    # @rock, dijkstra (different cost function that is monotonous (total path cost cannot go down))
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = map(len, (heights, heights[0]))
        efforts = [[math.inf] * n for _ in range(m)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            print(heap)
            effort, x, y = heapq.heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return effort
            for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                if m > r >= 0 <= c < n:
                    next_effort = max(effort, abs(heights[r][c] - heights[x][y]))
                    if efforts[r][c] > next_effort:
                        efforts[r][c] = next_effort
                        heapq.heappush(heap, (next_effort, r, c))
                        
    # # bellman ford
    # def minimumEffortPath(self, heights: List[List[int]]) -> int:
    #     m, n = map(len, (heights, heights[0]))
    #     efforts = [[math.inf] * n for _ in range(m)]
    #     efforts[0][0] = 0
    #     dq = deque([(0, 0, 0)])
    #     while dq:
    #         effort, x, y = dq.popleft()
    #         for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
    #             if len(heights) > r >= 0 <= c < len(heights[0]):
    #                 next_effort = max(effort, abs(heights[r][c] - heights[x][y]))
    #                 if efforts[r][c] > next_effort:
    #                     efforts[r][c] = next_effort
    #                     dq.append((next_effort, r, c))
    #     return efforts[-1][-1]
