################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210102
# Problem link      : https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Follow up: Solve the problem if repeated values on the tree are allowed. (this is also solved below)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(ori, clo):
            if not ori: return None
            if ori.val == target.val: return clo
            ans = dfs(ori.left, clo.left)
            if ans != None: return ans
            ans = dfs(ori.right, clo.right)
            if ans != None: return ans
            return None
        return dfs(original, cloned)
    

    # # @K_kkkyle
    # def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    #     def it(node):
    #         if node:
    #             yield node
    #             yield from it(node.left)
    #             yield from it(node.right)
    #     for n1, n2 in zip(it(original), it(cloned)):
    #         if n1 == target:
    #             return n2
            
    # # stack way
    # def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    #     if not original or not cloned: return None
    #     stack = [(original,cloned)]
    #     while stack:
    #         org, clone = stack.pop()
    #         if org == target: 
    #             return clone
    #         if org.left:
    #             stack.append((org.left, clone.left))
    #         if org.right:
    #             stack.append((org.right, clone.right))

    # # save the path
    # def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    #     path = []
    #     def traverse(x):
    #         if not x: 
    #             return False
    #         if x is target:
    #             return True
    #         if traverse(x.left):
    #             path.append(True)
    #             return True
    #         if traverse(x.right):
    #             path.append(False)
    #             return True
    #         return False

    #     traverse(original)
    #     pointer = cloned
    #     for x in reversed(path):
    #         if x:
    #             pointer = pointer.left
    #         else:
    #             pointer = pointer.right
    #     return pointer