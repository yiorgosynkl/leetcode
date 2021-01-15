################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210115
# Problem link      : https://leetcode.com/problems/get-maximum-in-generated-array/
################################################################

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1: return n
        arr = [0, 1] + [0]*(n-1)
        ans = 1
        for i in range(2, n+1):
            arr[i] = arr[i//2] + (i%2)*arr[i//2+1]
            ans = max(ans, arr[i])
        return ans
    
#     # less memory
#     def getMaximumGenerated(self, n: int) -> int:
#         if n <= 1: return n
#         q, ans = deque([1]), 1 
#         for i in range(2, n, 2):
#             q.append(q[0])
#             q.append(q[0] + q[1])
#             ans = max(ans, q[-1])
#             q.popleft()
#         return ans
        