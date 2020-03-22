class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        megalist = []
        for i in range(0, n):
            megalist.append([])
        for seat in reservedSeats:
            row = seat[0] - 1
            col = seat[1] - 1
            megalist[row].append(col)
        print(megalist)        
        res = 0
        for mini in megalist:
            minires = 0
            flag = True
            for i in [1,2,3,4,5,6,7,8]:
                if i in mini:
                    flag = False
                    break
            if flag == True:
                res += 2
                continue
            flag = True
            for i in [1,2,3,4]:
                if i in mini:
                    flag = False
                    break
            if flag == True:
                res += 1
                continue
            flag = True
            for i in [3,4,5,6]:
                if i in mini:
                    flag = False
                    break
            if flag == True:
                res += 1
                continue
            flag = True
            for i in [5,6,7,8]:
                if i in mini:
                    flag = False
                    break
            if flag == True:
                res += 1
        return res
            