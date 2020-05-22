################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200522
# Problem link      : https://leetcode.com/problems/majority-element/
################################################################

class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        ans = ''.join([int(v)*k for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)])
        return ans

    # one-liner   
    # def frequencySort(self, s: str) -> str:
    #     return ''.join(sorted(s, key = lambda ch: s.count(ch), reverse=True))
    
    # one-liner
    # def frequencySort(self, str):
    #     """
    #     :type str: str
    #     :rtype: str
    #     """
    #     return "".join([char * times for char, times in collections.Counter(str).most_common()])