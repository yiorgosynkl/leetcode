################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200529
# Problem link      : https://leetcode.com/problems/course-schedule/
################################################################

import collections
# https://en.wikipedia.org/wiki/Topological_sorting  

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for a,b in prerequisites:
            adj[a].add(b)
        no_mark = set([i for i in range(numCourses)])
        marks = [0] * numCourses # 0 not marked, 1 temporary, 2 permanent  
        
        def visit(node):
            if marks[node] == 1: return False
            if marks[node] == 2: return True
            marks[node] = 1
            no_mark.remove(node)
            for nbr in adj[node]:
                if not visit(nbr): return False
            marks[node] = 2
            return True
        
        while no_mark:
            if not visit(next(iter(no_mark))): return False
        
        return True

#     if there is cycle, at least one element of cycle will have larger in-degree and won't enter bfs
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         edges = [[] for i in range(numCourses)]
#         degrees = [0] * numCourses # in_degree
#         for course, pre_course in prerequisites:
#             edges[pre_course].append(course)
#             degrees[course] += 1
#         # don't iterate and append list at the same loop, use queue 
#         queue = collections.deque(course for course, degree in enumerate(degrees) if not degree)
#         while queue:
#             course = queue.popleft()
#             for next_course in edges[course]:
#                 degrees[next_course] -= 1
#                 if not degrees[next_course]:
#                     queue.append(next_course)

#         return not sum(degrees)
