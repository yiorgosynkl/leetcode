################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201104
# Problem link      : https://leetcode.com/problems/minimum-height-trees/
################################################################

from collections import defaultdict
import math 

class Solution:
#     # brute force slow
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         # adjacency list and id of root node
#         def bfs(adj, root):
#             lvl = [root] # nodes of current level [list]
#             xpl = { root } # exlored nodes {set}
#             ht = -1 # height (int)
#             while lvl:
#                 nxt = [] # nodes of next level
#                 ht += 1
#                 while lvl:
#                     node = lvl.pop()
#                     for nb in adj[node]: # find unexplored neighbors
#                         if nb not in xpl:
#                             nxt.append(nb)
#                             xpl.add(nb)
#                 lvl = nxt
#             return ht
            
#         adj = collections.defaultdict(list)
#         for s, e in edges: # undirected graph
#             adj[s].append(e)
#             adj[e].append(s)
#         min_ht, ans = math.inf, []
#         for i in range(n):
#             ht = bfs(adj, i)
#             if min_ht > ht: # found new minimum
#                 min_ht, ans = ht, []
#             if min_ht == ht: # save new root
#                 ans.append(i)
#         return ans
    

#     # return half of the diameter
#     # to find diameter we use one bfs to find longest nodes than bfs from these nodes
#     # after that we go the middle of each tree bfs and save this nodes
#     # whatever node is in both trees (starting from one corner and then from the other corner)
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         # adjacency list and id of root node
#         def bfs(adj, root, stop_ht=-1):
#             if stop_ht < 0:
#                 stop_ht = len(adj)
#             prv, lvl = [], [root] # nodes of previous and current level [list]
#             xpl = { root } # exlored nodes {set}
#             ht = -1 # height (int)
#             while lvl and ht < stop_ht:
#                 nxt = [] # nodes of next level
#                 ht += 1
#                 for node in lvl:
#                     for nb in adj[node]: # find unexplored neighbors
#                         if nb not in xpl:
#                             nxt.append(nb)
#                             xpl.add(nb)
#                 prv, lvl = lvl, nxt
#             return ht, prv
        
#         if n == 1:
#             return [0]
#         adj = collections.defaultdict(list)
#         for s, e in edges: # undirected graph
#             adj[s].append(e)
#             adj[e].append(s)
#         _, last_lvl = bfs(adj, 1) # 1st bfs
#         diam_left = last_lvl[0] # the 'leftmost' node of the diameter
#         diameter, last_lvl = bfs(adj, last_lvl[0]) # 2nd bfs
#         diam_right = last_lvl[0]  # the 'rightmost' node of the diameter
#         ans_left, ans_right = set(), set()
#         # if diameter % 2 == 0:
#         min_ht = diameter // 2 # height of minimum height tree
#         _, roots = bfs(adj, diam_left, min_ht) # 3rd bfs
#         ans_left |= set(roots) # union
#         _, roots = bfs(adj, diam_right, min_ht) # 4th bfs
#         ans_right |= set(roots) 
#         if diameter%2 == 1: # maybe it
#             min_ht = diameter // 2 + 1
#             _, roots = bfs(adj, diam_left, min_ht) # 5th bfs
#             ans_left |= set(roots) 
#             _, roots = bfs(adj, diam_right, min_ht) # 6th bfs
#             ans_right |= set(roots)
#         return list(ans_left & ans_right) # intersection

    # trim leaves and move on
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0] 
        adj = defaultdict(set)
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: newLeaves.append(j)
            leaves = newLeaves
        return leaves

    
#     # official solution    
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

#         # base cases
#         if n <= 2:
#             return [i for i in range(n)]

#         # Build the graph with the adjacency list
#         neighbors = [set() for i in range(n)]
#         for start, end in edges:
#             neighbors[start].add(end)
#             neighbors[end].add(start)

#         # Initialize the first layer of leaves
#         leaves = []
#         for i in range(n):
#             if len(neighbors[i]) == 1:
#                 leaves.append(i)

#         # Trim the leaves until reaching the centroids
#         remaining_nodes = n
#         while remaining_nodes > 2:
#             remaining_nodes -= len(leaves)
#             new_leaves = []
#             # remove the current leaves along with the edges
#             while leaves:
#                 leaf = leaves.pop()
#                 for neighbor in neighbors[leaf]:
#                     neighbors[neighbor].remove(leaf)
#                     if len(neighbors[neighbor]) == 1:
#                         new_leaves.append(neighbor)

#             # prepare for the next round
#             leaves = new_leaves

#         # The remaining nodes are the centroids of the graph
#         return leaves