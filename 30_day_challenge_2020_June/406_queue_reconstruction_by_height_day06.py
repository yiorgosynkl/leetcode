################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200606
# Problem link      : https://leetcode.com/problems/queue-reconstruction-by-height/
################################################################

class Solution:
    # def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    #     people = sorted(people, key=lambda per: (per[0], -per[1]), reverse=True) 
    #     print(people)
    #     indices = [idx for idx in range(len(people))]
    #     ans = [[] for _ in range(len(people))]
    #     while people:
    #         h, k = people.pop()
    #         ans[indices[k]] = [h, k]
    #         indices.pop(k)
    #     return ans
    
    # if equal heights, than he is counted taller than me
    # shorter first (min h) and than if heights are equal than choose (max k)
    # since lambda chooses the smallest than just choose (min -k) <=> (max k)
    
    # StefannPochman
    # from first-tallest (who doesn't count anybody) to last-shortest (who counts everybody)
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
