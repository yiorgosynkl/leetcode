################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201227
# Problem link      : https://leetcode.com/problems/jump-game-iv/
################################################################

from collections import deque
from collections import defaultdict
import math

class Solution:                   
    # def minJumps(self, arr: List[int]) -> int:
    #     ps = defaultdict(set) # portals
    #     for i, v in enumerate(arr):
    #         ps[v].add(i)
    #     group, seen, c = set([0]), set(), 0
    #     while group:
    #         ngroup = set() 
    #         for i in group:
    #             if i not in seen:
    #                 seen.add(i)
    #                 if i == len(arr) - 1:
    #                     return c
    #                 if i > 0: ngroup.add(i-1)
    #                 if i < len(arr) - 1: ngroup.add(i+1)
    #                 ngroup = ngroup.union(ps[arr[i]])
    #                 # ps[arr[i]] = set()  # these neighbours have been already accessed
    #         group = ngroup
    #         c += 1
    #     return -1                   
  
    
    # def minJumps(self, arr: List[int]) -> int:
    #     ps = defaultdict(set) # portals
    #     for i, v in enumerate(arr):
    #         ps[v].add(i)
    #     group, seen, c = [0], { 0 }, 0
    #     while group:
    #         ngroup = []
    #         for i in group:
    #             if i == len(arr) - 1: return c
    #             if i > 0 and i-1 not in seen: 
    #                 seen.add(i-1)
    #                 ngroup.append(i-1)
    #             if i < len(arr) - 1 and i+1 not in seen: 
    #                 seen.add(i+1)
    #                 ngroup.append(i+1)
    #             for j in ps[arr[i]]:
    #                 if j not in seen:
    #                     seen.add(j)
    #                     ngroup.append(j)
    #                 ps[arr[i]] = set()  # these neighbours have been already accessed
    #         group = ngroup
    #         c += 1
    #     return -1  
    
#     # @Babichev
#     def minJumps(self, arr):
#         n = len(arr)
#         d = defaultdict(list)
#         for i, num in enumerate(arr):
#             d[num].append(i)
            
#         queue = deque([(0, 0)])
#         visited, visited_groups = set(), set()
        
#         while queue:
#             steps, index = queue.popleft()
#             if index == n - 1: return steps
            
#             for neib in [index - 1, index + 1]:
#                 if 0 <= neib < n and neib not in visited:
#                     visited.add(neib)
#                     queue.append((steps + 1, neib))
            
#             if arr[index] not in visited_groups:
#                 for neib in d[arr[index]]:
#                     if neib not in visited:
#                         visited.add(neib)
#                         queue.append((steps + 1, neib))
#                 visited_groups.add(arr[index])
                
    # # clean code                
    # def minJumps(self, arr):
    #     n = len(arr)
    #     d = defaultdict(list)
    #     for i, v in enumerate(arr):
    #         d[v].append(i)
            
    #     queue, seen = deque([(0, 0)]), set()
        
    #     while queue:
    #         steps, index = queue.popleft()
    #         if index == n - 1: return steps
            
    #         for neib in [index - 1, index + 1] + d[arr[index]]:
    #             if 0 <= neib < n and neib not in seen:
    #                 seen.add(neib)
    #                 queue.append((steps + 1, neib))
    #         d[arr[index]] = []  # avoid later lookup, reduces complexity dramatically

    #     return -1
        

    def minJumps(self, arr) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store layers from start
        visited = {0, n-1}
        step = 0

        other = [n-1] # store layers from end

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = []

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1