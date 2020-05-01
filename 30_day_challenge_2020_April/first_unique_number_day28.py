################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200428
# Problem link      : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/
################################################################

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.unique = OrderedDict()
        self.multi = set([])
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:
        return next(iter(self.d.keys(),-1))
        # if self.unique:
        #     return next(iter(self.unique))
        # return -1

    def add(self, num: int) -> None:
        if num not in self.multi:
            if num not in self.unique:
                self.unique[num] = 1 # the value doesn't really matter
            else:
                self.multi.add(num)    
                del self.unique[num]

# FINALLY!!!   
# the way to avoid if else value exists in dictionary
# self.dic[key] = self.dic.get(key, 0) + 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)