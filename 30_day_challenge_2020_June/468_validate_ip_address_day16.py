################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200616
# Problem link      : https://leetcode.com/problems/validate-ip-address/
################################################################

class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s):
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False
        def isIPv6(s):
            if len(s) > 4: return False
            try: return int(s, 16) >= 0 and s[0] != '-'
            except: return False
            
        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")): 
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")): 
            return "IPv6"
        return "Neither"

    # def validIPAddress(self, IP: str) -> str:
    #     hexset = set(['a','b','c','d','e','f','A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9'])
    #     decset = set(['0','1','2','3','4','5','6','7','8','9'])
    #     if ':' in IP:
    #         s = IP.split(':')
    #         if len(s) != 8:
    #             return "Neither"
    #         for subs in s:
    #             for ch in subs:
    #                 if ch not in hexset:
    #                     return "Neither"
    #             if subs == '' or len(subs) > 4 or int(subs, 16) > 65536 or int(subs, 16) < 0:
    #                 return "Neither"
    #         return "IPv6"
    #     elif '.' in IP:
    #         s = IP.split('.')
    #         if len(s) != 4:
    #             return "Neither"
    #         for subs in s:
    #             for ch in subs:
    #                 if ch not in decset:
    #                     return "Neither"
    #             if subs == '' or int(subs) > 255 or int(subs) < 0 or (int(subs) != 0 and subs[0] == '0') or (int(subs) == 0 and subs != '0'):
    #                 return "Neither"
    #         return "IPv4"
    #     return "Neither"
        


'''
Testcases to consider
"2001:0db8:85a3:0:0:8A2E:0370:7334"
"2001:db8:85a3:0::8a2E:0370:7334"
"2001:0db8:85a3:00000:0:8A2E:0370:7334"
"00.0.0.0"
"1.0.1."
"1e1.4.5.6"
"172.16.254.0"
"172.16.256.1"
"172.16.254.01"
'''