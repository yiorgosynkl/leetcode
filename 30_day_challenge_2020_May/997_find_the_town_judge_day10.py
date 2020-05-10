################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200510
# Problem link      : https://leetcode.com/problems/majority-element/
################################################################

class Solution:
    # in_degree == N - 1 and out_degree == 0
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        degs = [[0,0] for _ in range(N + 1)] # (in_degree, out_degree)
        for a, b in trust:
            degs[a][1] += 1
            degs[b][0] += 1
        res = []
        for idx, val in enumerate(degs):
            in_deg, out_deg = val
            if in_deg == N - 1 and out_deg == 0:
                res.append(idx)
        return res[0] if len(res) == 1 else -1
    
        # in_degree - out_degree = N - 1, solution by lee215
        def findJudge(self, N, trust):
            count = [0] * (N + 1) # count = in degree - out_degree
            for i, j in trust:
                count[i] -= 1
                count[j] += 1
            for i in range(1, N + 1):
                if count[i] == N - 1:
                    return i
            return -1
            
        