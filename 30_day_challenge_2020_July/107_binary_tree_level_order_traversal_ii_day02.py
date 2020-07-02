################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200702
# Problem link      : https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        up, down, ans = [root], [], []
        while up:
            level = []
            while up:
                node = up.pop()
                level.append(node.val)
                if node.left: down.append(node.left)
                if node.right: down.append(node.right)
            ans.append(level)
            up, down = down[::-1], up
        return ans[::-1]
            
            
            
        
        