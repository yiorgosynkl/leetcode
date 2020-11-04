# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder(root): # dfs
    return [root.val] + dfs(root.left) + dfs(root.right) if root else []

def inorder(root): # dfs
    return dfs(root.left) + [root.val] + dfs(root.right) if root else []

def postorder(root): # dfs
    return dfs(root.left) + dfs(root.right) + [root.val] if root else []

from collections import defaultdict

# create graph from list of edges
# number of nodes, edges between nodes
def create_adj(n, edges):
    adj = defaultdict(set)
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)

def bfs(adj, root):
    prv, lvl = [], [root] # nodes of previous and current level [list]
    xpl = { root } # exlored nodes {set}
    ht = -1 # height (int)
    while lvl and ht < stop_ht:
        nxt = [] # nodes of next level
        ht += 1
        for node in lvl:
            for nb in adj[node]: # find unexplored neighbors
                if nb not in xpl:
                    nxt.append(nb)
                    xpl.add(nb)
        prv, lvl = lvl, nxt
    return ht, prv # return height and nodes of last lvl