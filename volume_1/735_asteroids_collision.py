class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        survivors = []
        for idx, val in enumerate(asteroids):
            if val > 0:
                # choose datastructure for quick append
                stack.append((idx, val))
            else:
                isSurvivor = True
                while stack:
                    _, pval = stack[-1]
                    # print(pval, val)
                    if pval == abs(val):
                        stack.pop()
                        isSurvivor = False
                        break
                    elif pval < abs(val):
                        stack.pop()
                    else:
                        isSurvivor = False
                        break
                if isSurvivor:
                    survivors.append(idx)
        stack = [idx for idx, _ in stack]
        # print(stack, survivors) 
        #TODO concatenate in O(n)
        return [asteroids[idx] for idx in sorted(stack + survivors)]