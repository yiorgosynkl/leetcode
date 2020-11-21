################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201121
# Problem link      : https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
################################################################

import bisect

class Solution:    
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def spec(ds: List[str], lim: str): # count special case for equal num of digits
            eq = ds.count(lim[0]) # check if first digit of lim exists
            ls = bisect.bisect(ds, lim[0]) - eq # check how many are smaller than first digits
            if len(lim) == 1: return ls + eq
            return ls * (len(ds)**(len(lim)-1)) + ( spec(ds, lim[1:]) if eq else 0 )
        ds, lim = sorted(digits), str(n)
        count_less = sum(len(ds)**i for i in range(1, len(lim))) # count combinations for numbers with less digits
        count_equal = spec(ds, lim) # count combinations for numbers with equal num of digits
        return count_less + count_equal    

    # # @lee215
    # def atMostNGivenDigitSet(self, D, N):
    #     N = str(N)
    #     n = len(N)
    #     res = sum(len(D) ** i for i in range(1, n))
    #     i = 0
    #     while i < len(N):
    #         res += sum(c < N[i] for c in D) * (len(D) ** (n - i - 1))
    #         if N[i] not in D: break
    #         i += 1
    #     return res + (i == n)
    
#     # dp solution (https://codeforces.com/blog/entry/53960)    
#     def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
#         D = list(map(int, D))
#         N = list(map(int, str(N)))

#         @functools.lru_cache(None)
#         def dp(i, isPrefix, isBigger):
#             if i == len(N):
#                 return not isBigger
#             if not isPrefix and not isBigger:
#                 return 1 + len(D) * dp(i + 1, False, False)
#             return 1 + sum(dp(i + 1, isPrefix and d == N[i], isBigger or (isPrefix and d > N[i])) for d in D)

#         return dp(0, True, False) - 1

    # # official dp solution
    # def atMostNGivenDigitSet(self, D, N):
    #     S = str(N)
    #     K = len(S)
    #     dp = [0] * K + [1]
    #     # dp[i] = total number of valid integers if N was "N[i:]"

    #     for i in xrange(K-1, -1, -1):
    #         # Compute dp[i]

    #         for d in D:
    #             if d < S[i]:
    #                 dp[i] += len(D) ** (K-i-1)
    #             elif d == S[i]:
    #                 dp[i] += dp[i+1]

    #     return dp[0] + sum(len(D) ** i for i in xrange(1, K))


    # # bijective base B official solution (really interesting)
    # def atMostNGivenDigitSet(self, D, N):
    #     B = len(D) # bijective-base B
    #     S = str(N)
    #     K = len(S)
    #     A = []  #  The largest valid number in bijective-base-B.

    #     for c in S:
    #         if c in D:
    #             A.append(D.index(c) + 1)
    #         else:
    #             i = bisect.bisect(D, c)
    #             A.append(i)
    #             # i = 1 + (largest index j with c >= D[j], or -1 if impossible)
    #             if i == 0:
    #                 # subtract 1
    #                 for j in xrange(len(A) - 1, 0, -1):
    #                     if A[j]: break
    #                     A[j] += B
    #                     A[j-1] -= 1

    #             A.extend([B] * (K - len(A)))
    #             break

    #     ans = 0
    #     for x in A:
    #         ans = ans * B + x
    #     return ans
