class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # arr1.sort()
        # arr2.sort()
        res = 0
        for el1 in arr1:
            flag = True
            for el2 in arr2:
                if abs(el2 - el1) <= d:
                    flag = False
                    break
            if flag == True:
                res += 1
        return res