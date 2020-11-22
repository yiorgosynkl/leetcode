################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201122
# Problem link      : https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
################################################################

class Solution:
    def minimumDeletions(self, s: str) -> int:
        aaf, bbf = s.count('a'), 0 # number of 'a' after pointer, number of 'b' before pointer (these will get erased)
        ans = aaf + bbf 
        for c in s: # this is actually dp, at some point there will be the switch between 0 and 1 aaf + bbf will be changed
            aaf -= int(c == 'a')
            bbf += int(c == 'b')
            ans = min(ans, aaf + bbf)
        return ans

    
    # # Whenever encounter a pair of "ba", cancel both of them and count the number of cancellations, @rock
    # def minimumDeletions(self, s: str) -> int:
    #     cnt, stack = 0, []
    #     for c in s:
    #         if stack and stack[-1] == 'b' and c == 'a':
    #             stack.pop()
    #             cnt += 1
    #         else:
    #             stack.append(c)
    #     return cnt
    # def minimumDeletions(self, s: str) -> int:
    #     cnt, bs = 0, 0 # count 'ba' pairs
    #     for c in s:
    #         if bs > 0 and c == 'a':
    #             bs -= 1
    #             cnt += 1
    #         elif c == 'b':
    #             bs += 1
    #     return cnt
