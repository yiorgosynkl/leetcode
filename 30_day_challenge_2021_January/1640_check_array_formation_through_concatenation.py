################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20210101
# Problem link      : https://leetcode.com/problems/check-array-formation-through-concatenation/
################################################################

class Solution:
    # @yiorgosynkl
    # def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    #     match = { num : i for i, piece in enumerate(pieces) for num in piece }
    #     c = 0   # counter
    #     while c < len(arr):
    #         if arr[c] not in match:
    #             return False
    #         piece_idx = match[arr[c]]
    #         for num in pieces[piece_idx]:
    #             if c == len(arr) or arr[c] != num:
    #                 return False
    #             c += 1
    #     return True
        
    # # @eric496  
    # def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    #     mp = {x[0]: x for x in pieces}
    #     res = []
    #     for num in arr:
    #         res += mp.get(num, [])
    #     return res == arr
    
#     # @DBabichev 
#     # each piece should be a substring of arr_str 
#     # (because we have exactly the same amount of nums and all pieces are unique)
#     # time: O(n^2)
#     def canFormArray(self, arr, pieces):
#         arr_str = "!".join(map(str, arr)) + "!"
#         return all("!".join(map(str, p)) + "!" in arr_str for p in pieces) 
    
    # @DBabichev 
    def canFormArray(self, arr, pieces):
        d = {x[0]: x for x in pieces}
        return list(chain(*[d.get(num, []) for num in arr])) == arr 
    
    
    # def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    #     d = {x[0]:x for x in pieces}
    #     L = [d.get(i,[]) for i in arr]
    #     return arr == reduce(list.__add__, L) # flatten array
