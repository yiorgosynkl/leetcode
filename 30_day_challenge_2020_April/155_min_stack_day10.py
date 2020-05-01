################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200410
# Problem link      : https://leetcode.com/problems/min-stack/
################################################################

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.smin = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.smin or x <= self.smin[-1]:
            self.smin.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.smin[-1]:
            self.smin.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smin[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()