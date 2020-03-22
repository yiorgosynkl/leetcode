def gold(x: int) -> int:
    count = 0
    while (x != 1):
        if (x % 2 == 0):
            x = x / 2
        else:
            x = 3 * x + 1
        count += 1
    return count

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = []
        order = []
        for num in range(lo, hi + 1):
            p = gold(num)
            i = 0
            while (i < len(power) and power[i] <= p):
                i += 1
            power.insert(i, p)
            order.insert(i, num)
        print(order)
        print(power)
        return order[k - 1]
            
        