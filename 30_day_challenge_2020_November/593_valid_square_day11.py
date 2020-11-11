################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201111
# Problem link      : https://leetcode.com/problems/valid-square/
################################################################

class Solution:
#     def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
#         # left rotate list n times
#         def rot(l, n):
#             return l[n:] + l[:n]

#         # returns sides between consecutive points
#         def get_square_sides(l):
#             return [ ((i[0] - j[0])**2 + (i[1] - j[1])**2) for i, j in zip(l, rot(l, 1))] # rotate by one
#         # return if sides of triangle form a right angle (input: list with three sides)
#         def is_right_angle_sides(square_sides):
#             a, b, c = sorted(square_sides)
#             return (a + b == c)

#         # return if points of triangle form a right angle (input: list with three points)
#         def is_right_angle_points(points):
#             square_sides = get_square_sides(points)
#             return is_right_angle_sides(square_sides)
        
#         def sort_points(points):
#             l = [p1, p2, p3, p4]
#             up = sorted(l, key = lambda x: (x[1], x[0]))[0] # the uppermost (if equality the rightmost)
#             right = sorted(l, key = lambda x: (x[0], -x[1]))[0] # the rightmost (if equality the downmost)
#             down = sorted(l, key = lambda x: (-x[1], -x[0]))[0] # the downmost (if equality the leftmost)
#             left = sorted(l, key = lambda x: (-x[0], x[1]))[0] # the leftmost (if equality the uppermost)
#             return [up, right, down, left]
        
#         def all_equal(l):
#             return l.count(l[0]) == len(l) if len(l) > 1 else True

#         # sort elements
#         l = sort_points([p1, p2, p3, p4])
#         square_sides = get_square_sides(l)
#         if not all_equal(square_sides) or 0 in square_sides: return False
#         angles = [is_right_angle_points([a, b, c]) for a, b, c in list(zip(l, rot(l,1), rot(l,2)))]
#         if not all(angles): return False
#         return True    
    
    # check if edges are equal and if diagonals are equal
    # could brute force, but it's better to sort them
    # we start from left to right (if there is equality, sort from down to up!!)
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def ds(pA, pB): # squared distance
            return (pA[0]-pB[0])**2 + (pA[1]-pB[1])**2
        def all_equal(sides):
            return sides.count(sides[0]) == len(sides)
        a, b, c, d = sorted([p1, p2, p3, p4], key = lambda t: (t[0], -t[1]))
        edges, diagonals = [ds(a, b), ds(b, d), ds(d, c), ds(c, a)], [ds(a, d), ds(b, c)]
        if all_equal(edges) and all_equal(diagonals) and 0 not in edges and 0 not in diagonals: 
            return True
        return False
    
    # # @lee215
    # # there are 3 distances (edges, diagonals and 0 from point to itself)
    # # we also check that points are unique
    # def validSquare(self, p1, p2, p3, p4):
    #     points = [p1, p2, p3, p4]
    #     return len({(a[0]-b[0])**2 + (a[1]-b[1])**2 for a in points for b in points}) == 3 and \
    #            len(set(map(tuple, points))) == 4
    # def validSquare(self, *p):
    #     return len(set((a[0]-b[0])**2 + (a[1]-b[1])**2 for a in p for b in p)) == 3 and len(set(map(tuple, p))) == 4


