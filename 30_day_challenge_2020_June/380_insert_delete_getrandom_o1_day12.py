################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200612
# Problem link      : https://leetcode.com/problems/insert-delete-getrandom-o1/
################################################################

from random import randint

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos.keys():
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        We copy the last element to the element that is being removed!! (genious)
        """
        if val not in self.pos.keys():
            return False
        idx, last = self.pos[val], self.nums[-1]
        self.nums[idx], self.pos[last] = last, idx
        self.nums.pop(); self.pos.pop(val)
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[randint(0, len(self.nums) - 1)]


# class RandomizedSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.db = set()
        

#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val in self.db:
#             return False
#         self.db.add(val)
#         return True
        

#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val not in self.db: 
#             return False
#         self.db.remove(val)
#         return True
        
#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         idx = randint(0, len(self.db) - 1)
#         return list(self.db)[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()