################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200517
# Problem link      : https://leetcode.com/problems/find-all-anagrams-in-a-string/
################################################################

class Solution:
    # solution by YL_LC
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        out = []
        if len(s) < len(p):
            return out
        
        hash_p = hash_s = 0
        for i in range(len(p)):
            hash_p += hash(p[i])
            hash_s += hash(s[i])

        if hash_s == hash_p:
            out.append(0)        

        for i in range(len(p),len(s)):
            hash_s += hash(s[i]) - hash(s[i - len(p)])
            if hash_p == hash_s:
                out.append(i - len(p) + 1)
        return out    
    
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         if len(s) < len(p):
#             return []
        
#         def ok(goal_dic, my_dic):
#             for key, val in goal_dic.items():
#                 if key not in my_dic or my_dic[key] != val:
#                     return False
#             return True
        
#         goal_dic = {}
#         for ch in p:
#             goal_dic[ch] = goal_dic.get(ch, 0) + 1
#         ans = []
#         my_dic = {}
#         for i in range(len(p) - 1):
#             ch = s[i]
#             my_dic[ch] = my_dic.get(ch, 0) + 1
#         for i in range(0, len(s) - len(p) + 1):
#             ch = s[i + len(p) - 1]
#             my_dic[ch] = my_dic.get(ch, 0) + 1
#             if ok(goal_dic, my_dic):
#                 ans.append(str(i))
#             ch = s[i]
#             my_dic[ch] -= 1
#         return ans
        