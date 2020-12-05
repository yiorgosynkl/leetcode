################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201205
# Problem link      : https://leetcode.com/problems/can-place-flowers/
################################################################

class Solution:
    # !when enough spots found, stop!
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        fb = [0] + flowerbed + [0]
        for i in range(1, len(fb) - 1):
            if fb[i] == fb[i-1] == fb[i+1] == 0:
                fb[i] = 1
                n -= 1
                # i += 1 # could also increment i by one
            if n == 0: return True 
        return False
