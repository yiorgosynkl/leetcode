class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        print(reservedSeats)
        res = 2 * n
        while(reservedSeats):
            row = reservedSeats[0][0]
            cols = [reservedSeats[0][1]]
            reservedSeats.pop(0)
            while (reservedSeats and row == reservedSeats[0][0]):
                cols.append(reservedSeats[0][1])
                reservedSeats.pop(0)
            duos = [False, False, False, False] 
            if 2 in cols or 3 in cols:
                duos[0] = True
            if 4 in cols or 5 in cols:
                duos[1] = True
            if 6 in cols or 7 in cols:
                duos[2] = True
            if 8 in cols or 9 in cols:
                duos[3] = True
            if (duos[0] and duos[2]) or (duos[1] and duos[3]) or (duos[1] and duos[2]):
                res -= 2
            elif duos[0] or duos[1] or duos[2] or duos[3]:
                res -= 1
        return res
                
            