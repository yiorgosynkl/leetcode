################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200505
# Problem link      : https://leetcode.com/problems/first-unique-character-in-a-string/
################################################################

class Solution:    
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        multi = set()
        for idx, ch in enumerate(s):
            if ch not in multi:
                if ch not in unique.keys():
                    unique[ch] = idx
                else:
                    del unique[ch]
                    multi.add(ch)
        return min(unique.values()) if unique else -1
    
    # one liner
    # def firstUniqChar(self, s: str) -> int:
    #     return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
                
    # quick solution
#     def firstUniqChar(self, s: str) -> int:
#         unique = set([])
#         multi = set([])
#         for ch in s:
#             if ch not in multi:
#                 if ch in unique:
#                     unique.remove(ch)
#                     multi.add(ch)
#                 else:
#                     unique.add(ch)
#         # print(multi)
#         # print(unique)
#         for idx, ch in enumerate(s):
#             if ch in unique:
#                 return idx
#         return -1
            
                    