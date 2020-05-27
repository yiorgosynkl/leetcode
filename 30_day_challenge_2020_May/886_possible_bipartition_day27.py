################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200527
# Problem link      : https://leetcode.com/problems/possible-bipartition/
################################################################

from collections import defaultdict

class Solution:
    # idea
    # if graph is bipartite that true, else false
    # bipartite => only even circles exist
    # bfs and try 2-color the graph
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for a,b in dislikes:
            adj[a-1].add(b-1)
            adj[b-1].add(a-1)
        colors = [0] + [-1]*(N-1)
        queue, not_explored = [0], set([i for i in range(1,N)])
        while queue or not_explored:
            if not queue: # when multipe unconnected graph
                queue.append(not_explored.pop())
                continue
            node = queue.pop(0)
            for nbr in adj[node]:
                if colors[nbr] == colors[node]:
                    return False
                colors[nbr] = colors[node] ^ 1 # put the oposite color
                if nbr in not_explored:
                    not_explored.remove(nbr)
                    queue.append(nbr)
        return True
