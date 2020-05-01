################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200501
# Problem link      : https://leetcode.com/problems/first-bad-version/
################################################################

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def search(lo, hi):
            if (lo == hi): 
                return lo
            mid = (lo + hi) // 2
            return search(lo, mid) if isBadVersion(mid) else search(mid + 1, hi)
        
        if isBadVersion(1): 
            return 1
        return search(1, n)
