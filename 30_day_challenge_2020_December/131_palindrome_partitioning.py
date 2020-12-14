################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201214
# Problem link      : https://leetcode.com/problems/palindrome-partitioning/
################################################################

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # def pali(s):
        #     h = len(s) // 2 # half length
        #     return int(s[:h] == s[-1:-h-1:-1])        
        def pali(s):
            return int(s == s[::-1])

        ans, sbs, n = [], [], len(s) # sbs: substrings list, contains part of answer
        mem = [[-1 for _ in range(n)] for _ in range(n)]
        
        def dfs(st):
            if st == n:
                ans.append(sbs[:])
                return
            for en in range(st, n): # start and end (inclusive) boundaries
                if mem[st][en] == -1: # calculate for first time
                    mem[st][en] = pali(s[st:en+1])
                if mem[st][en] == 1:
                    sbs.append(s[st:en+1]) 
                    dfs(en+1)
                    sbs.pop()
            return 
        dfs(0)
        return ans
            
#     # @StefanPochmann one-liner
#     def partition(self, s):
#         return [[s[:i]] + rest
#                 for i in range(1, len(s)+1)
#                 if s[:i] == s[i-1::-1]
#                 for rest in self.partition(s[i:])] or [[]]

#     # @dichen001 https://leetcode.com/problems/palindrome-partitioning/discuss/42021/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)
#     # backtracking template
#     def partition(self, s):
#         def backtrack(start, end, tmp):
#             if start == end:
#                 ans.append(tmp[:])
#             for i in range(start, end):
#                 cur = s[start:i+1]
#                 if cur == cur[::-1]:
#                     tmp.append(cur)
#                     backtrack(i+1, end, tmp)
#                     tmp.pop()
#         ans = []
#         backtrack(0, len(s), [])
#         return ans
