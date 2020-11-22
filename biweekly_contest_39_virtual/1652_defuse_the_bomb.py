################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201122
# Problem link      : https://leetcode.com/problems/defuse-the-bomb/
################################################################

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        nums, n = code + code, len(code)
        ans = [0]*n
        if k > 0:
            s = sum(nums[0:k])
            for i in range(n):
                s = s - nums[i] + nums[i+k]
                ans[i] = s
        elif k < 0:
            k = -k
            s = sum(nums[n-k:n])
            for i in range(n):
                ans[i] = s
                print(ans)
                s = s - nums[i+n-k] + nums[i+n]
        return ans


    # def decrypt(self, code: List[int], k: int) -> List[int]:
    #     if k < 0: return self.decrypt(code[::-1], -k)[::-1] # nice hack
    #     n = len(code)
    #     prefix = code * 2
    #     for i in range(1, 2 * n):
    #         prefix[i] += prefix[i - 1]
    #     for i in range(n):
    #         code[i] = prefix[i + k] - prefix[i]
    #     return code