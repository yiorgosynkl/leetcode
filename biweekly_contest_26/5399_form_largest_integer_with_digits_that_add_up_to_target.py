################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200516
# Problem link      : https://leetcode.com/contest/biweekly-contest-26/problems/form-largest-integer-with-digits-that-add-up-to-target/
################################################################
            
import bisect

class Solution:
    def largestNumber(self, costs: List[int], target: int) -> str:
        def string_insert(s, c):
            s_list = [i for i in s[::-1]]
            bisect.insort(s_list, c)
            return ''.join(s_list)[::-1]
        dp = [""]
        for tar in range(1, target + 1):
            best_s = ""
            for idx, cost in enumerate(costs):
                if tar - cost >= 0:
                    s = string_insert(dp[tar - cost], str(idx + 1))
                    if len(s) > len(best_s) or (len(s) == len(best_s) and s > best_s):
                        if len(s) > 1 or tar - cost == 0:
                            best_s = s
            dp.append(best_s)
        return dp[target] if dp[target] != "" else "0"
                