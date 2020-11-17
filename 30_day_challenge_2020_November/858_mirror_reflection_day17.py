################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201117
# Problem link      : https://leetcode.com/problems/mirror-reflection/
################################################################

class Solution:
    # def mirrorReflection(self, p: int, q: int) -> int:
    #     ht, right = q, True # if ht: p < ht < 2p, that means 2p - ht is the actual height (reflection)
    #     while ht % p != 0:
    #         ht = (ht + q) % (2*p)
    #         right = not right
    #     if right:
    #         if ht == p:
    #             return 1
    #         else:
    #             return 0
    #     else: # left (ht == p)
    #         return 2
        
#     # official solution
#     def mirrorReflection(self, p, q):
#         from fractions import Fraction as F

#         x = y = 0
#         rx, ry = p, q
#         targets = [(p, 0), (p, p), (0, p)]

#         while (x, y) not in targets:
#             #Want smallest t so that some x + rx, y + ry is 0 or p
#             #x + rxt = 0, then t = -x/rx etc.
#             t = float('inf')
#             for v in [F(-x,rx), F(-y,ry), F(p-x,rx), F(p-y,ry)]:
#                 if v > 0: t = min(t, v)

#             x += rx * t
#             y += ry * t

#             #update rx, ry
#             if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
#                 rx *= -1
#             if y == p or y == 0:
#                 ry *= -1

#         return 1 if x==y==p else 0 if x==p else 2

    # # @lee215, actually what matters is the numbers q, p
    # def mirrorReflection(self, p: int, q: int) -> int:
    #     while p % 2 == 0 and q % 2 == 0: p, q = p / 2, q / 2 # divide until one is odd
    #     return 1 - p % 2 + q % 2 # if both odd return 1, if
    # # oneliner
    # def mirrorReflection(self, p: int, q: int) -> int:
    #     return ((p & -p) >= (q & -q)) + ((p & -p) > (q & -q))
    
#     # reflections of rooms A, B, C, D
#     def mirrorReflection(self, p, q):
#         k = 1
#         while k*q%p: k += 1
#         if k%2==1 and (k*q//p)%2==0: return 0
#         if k%2==1 and (k*q//p)%2==1: return 1
#         if k%2==0 and (k*q//p)%2==1: return 2     

    # m: the number of vertical room extensions + 1, n = the number of light reflection + 1
    # p: the length of the room, q: vertical distance that the light travels after each reflection
    # we search for n * q = m * p 
    def mirrorReflection(self, p, q):
        n, m = p, q
        while n%2 == 0 and m%2 == 0: n, m = n / 2, m / 2
        if m % 2 == 0 and n % 2 == 1: return 0
        if m % 2 == 1 and n % 2 == 1: return 1
        if m % 2 == 1 and n % 2 == 0: return 2
        return -1
