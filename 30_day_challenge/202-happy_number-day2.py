class Solution:
    def isHappy(self, n: int) -> bool:
        existance = set([])
        while True:
            ll = [int(digit) for digit in str(n)]
            n = sum([digit**2 for digit in ll])
            if n == 1:
                return True
            if n in existance:
                return False
            existance.add(n)
