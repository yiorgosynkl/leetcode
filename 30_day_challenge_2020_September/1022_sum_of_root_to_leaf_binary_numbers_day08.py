################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200908
# Problem link      : https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # bfs
    # def sumRootToLeaf(self, root: TreeNode) -> int:
    #     q, ans = deque(), 0
    #     q.append( (root, '') )
    #     while q:
    #         node, s = q.popleft()
    #         if node.left or node.right:
    #             if node.left: q.append( (node.left, s + str(node.val)) )
    #             if node.right: q.append( (node.right, s + str(node.val)) )
    #         else:
    #             ans += int(s + str(node.val), 2)
    #     return ans
    
    # recursive, dfs
    def sumRootToLeaf(self, node: TreeNode, val = 0) -> int:
        if not node: return 0
        val = 2 * val + node.val
        if not node.left and not node.right: return val
        return self.sumRootToLeaf(node.left, val) + self.sumRootToLeaf(node.right, val)
    
    # morris (official solution)
    def sumRootToLeaf(self, root: TreeNode) -> int:
        root_to_leaf = curr_number = 0
        
        while root:  
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left: 
                # Predecessor node is one step to the left 
                # and then to the right till you can.
                predecessor = root.left 
                steps = 1
                while predecessor.right and predecessor.right is not root: 
                    predecessor = predecessor.right 
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = (curr_number << 1) | root.val                    
                    predecessor.right = root  
                    root = root.left  
                # Break the link predecessor.right = root
                # Once the link is broken, 
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number >>= 1
                    predecessor.right = None
                    root = root.right 
                    
            # If there is no left child
            # then just go right.        
            else: 
                curr_number = (curr_number << 1) | root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right
                        
        return root_to_leaf
        