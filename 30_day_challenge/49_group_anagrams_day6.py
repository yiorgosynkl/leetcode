class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      anagrams = defaultdict(list)
      for word in strs:
        anagrams[''.join(sorted(word))].append(word)
      return list(anagrams.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         match = {}
#         for val in strs:
#             key = ''.join(sorted(val))
#             if key in match.keys():
#                 match[key].append(val)
#             else:
#                 match[key] = [val]
#         return [ll for ll in match.values()]
