class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        cinema = []
        for r in range(0, n):
            cinema.append([True, True, True, True])
        for s in reservedSeats:
            if s[1] == 2 or s[1] == 3:
                cinema[s[0] - 1][0] = False
            elif s[1] == 4 or s[1] == 5:
                cinema[s[0] - 1][1] = False
            elif s[1] == 6 or s[1] == 7:
                cinema[s[0] - 1][2] = False
            elif s[1] == 8 or s[1] == 9:
                cinema[s[0] - 1][3] = False     
        res = 0
        for r in cinema:
            if r[0] == True and r[1] == True and r[2] == True and r[3] == True:
                res += 2
            elif (r[0] == True and r[1] == True) or (r[1] == True and r[2] == True) or (r[2] == True and r[3] == True):
                res += 1
        return res
            