################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200519
# Problem link      : https://leetcode.com/problems/online-stock-span/
################################################################

class StockSpanner:

    def __init__(self):
        self.stack = [(float("inf"), 0)]
        self.idx = 0
        
    def next(self, price: int) -> int:
        while self.stack[-1][0] <= price:
            self.stack.pop()
        self.idx += 1
        ans =  self.idx - self.stack[-1][1]
        tup = (price, self.idx)
        self.stack.append(tup)
        return ans

#     sol by lee215
#     def __init__(self):
#         self.stack = []

#     def next(self, price):
#         res = 1
#         while self.stack and self.stack[-1][0] <= price:
#             res += self.stack.pop()[1]
#         self.stack.append([price, res])
#         return res
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)