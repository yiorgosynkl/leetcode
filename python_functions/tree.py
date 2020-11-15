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

# binary tree bfs
from collections import deque

def bfs(root: 'Node'):
    lvl = deque([root] if root else []) # nodes of previous and current level [list]
    while lvl:
        nxt = deque([]) # nodes of next level
        while lvl:
            node = lvl.popleft()
            if node.left: nxt.append(node.left)
            if node.right: nxt.append(node.right)
            ans.append(node.val)
        lvl = nxt
    return ans

def dfs(root: 'Node'):
    if root:
        dfs(root.right)
        dfs(root.left)
    print(root.val)
    return ans

# create graph from list of edges
# number of nodes, edges between nodes
from collections import defaultdict

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