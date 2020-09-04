################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200904
# Problem link      : https://leetcode.com/problems/partition-labels/
################################################################

class Solution:
    # def partitionLabels(self, s: str) -> List[int]:
    #     last, splits = {}, [1]*len(s) # last index of a letter, split points, 
    #     for i, c in enumerate(s):
    #         if c in last.keys():
    #             for j in range(last[c],i):
    #                 splits[j] = 0
    #         last[c] = i
    #     ans = [-1] + [i for i, num in enumerate(splits) if num == 1]
    #     ans = [n - p for n, p in zip(ans[1:], ans[:-1])] 
    #     return ans
    # suppose splits between all of the letters, delete the unnecessary
    # n_splits -= i - last[c] # doesn't work because we subtract same split point multiple times
    
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)} # find last instance of each letter
        hi = lo = 0 # lo, hi are start and end of one part
        ans = []
        for i, c in enumerate(S):
            hi = max(hi, last[c])
            if i == hi:
                ans.append(i - lo + 1)
                lo = i + 1
        return ans
    
    # @StefanPochmann O(n^2) clean solution
    # def partitionLabels(self, s):
    #     sizes = []
    #     while s:
    #         i = 1
    #         while set(s[:i]) & set(s[i:]):
    #             i += 1
    #         sizes.append(i)
    #         s = s[i:]
    #     return sizes