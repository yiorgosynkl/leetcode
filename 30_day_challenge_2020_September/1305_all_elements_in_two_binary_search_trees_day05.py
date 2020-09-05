################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200905
# Problem link      : https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            return dfs(root.left) + [root.val] + dfs(root.right) if root else []
 
        def combine(sa1, sa2): # sorted array 1 and 2
            res = []
            while sa1 and sa2:
                if sa1[0] <= sa2[0]:
                    res.append(sa1[0])
                    sa1 = sa1[1:]
                else:
                    res.append(sa2[0])
                    sa2 = sa2[1:]     
            return res + sa1 + sa2
        
        # merge using deque
        # def combine(sa1, sa2): # sorted array 1 and 2
        #     ans, dq1, dq2, = [], collections.deque(sa1), collections.deque(sa2)
        #     while dq1 or dq2:    
        #         if not dq2:
        #             ans.append(dq1.popleft())
        #         elif not dq1:
        #             ans.append(dq2.popleft())    
        #         else:
        #             ans.append(dq1.popleft() if dq1[0] < dq2[0] else dq2.popleft())
        #     return ans  
        
        # return combine(dfs(root1), dfs(root2))

        return sorted(dfs(root1) + dfs(root2)) # timsort works in O(n), @StefanPochmann 
