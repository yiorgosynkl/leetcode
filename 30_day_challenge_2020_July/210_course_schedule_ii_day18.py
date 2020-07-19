################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200718
# Problem link      : https://leetcode.com/problems/course-schedule-ii/
################################################################

from collections import defaultdict

class Solution:
    # dfs algorithm
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for a,b in prerequisites:
            adj[a].add(b)
        no_mark = set([i for i in range(numCourses)])
        marks = [0] * numCourses # 0 not marked, 1 temporary, 2 permanent  
        
        ans = []
        # returns True or False if possible and changes ans
        def visit(node):
            if marks[node] == 1: return False
            if marks[node] == 2: return True
            marks[node] = 1
            no_mark.remove(node)
            for nbr in adj[node]:
                if not visit(nbr): return False
            marks[node] = 2
            ans.append(node)
            return True
        
        while no_mark:
            if not visit(next(iter(no_mark))): return []

        return ans
