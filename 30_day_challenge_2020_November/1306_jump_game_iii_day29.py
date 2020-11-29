################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201129
# Problem link      : https://leetcode.com/problems/jump-game-iii/
################################################################

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        been, q, n = { start }, deque([start]), len(arr)
        while q:
            pos = q.popleft()
            if arr[pos] == 0:
                return True
            nxt = []
            if pos-arr[pos] >= 0: nxt.append(pos-arr[pos])
            if pos+arr[pos] < n: nxt.append(pos+arr[pos])
            for npos in nxt:
                if npos not in been:
                    q.append(npos)
                    been.add(npos)
        return False

    # @lee215
    def canReach(self, A, i):
        if 0 <= i < len(A) and A[i] >= 0:
            A[i] = -A[i] # flip number to negative to not count again (like set)
            return A[i] == 0 or self.canReach(A, i + A[i]) or self.canReach(A, i - A[i])
        return False