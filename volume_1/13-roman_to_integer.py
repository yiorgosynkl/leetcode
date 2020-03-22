################################################################
# Project           : leetcode
# Program name      : 13-roman_to_integer.py
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200311
# Description       : convert roman numerals to integer numbers (base 10)
################################################################

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        map1 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        map2 = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        idx = 0
        while (idx < len(s)):
            if (idx < len(s) - 1 and (s[idx] + s[idx + 1]) in map2):
                res += map2[s[idx] + s[idx + 1]]
                idx += 2
            else:
                res += map1[s[idx]]
                idx += 1                 
        return res
