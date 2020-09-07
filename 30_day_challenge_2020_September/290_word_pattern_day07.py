################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200907
# Problem link      : https://leetcode.com/problems/word-pattern/
################################################################

class Solution:
    def wordPattern(self, pattern: str, phrase: str) -> bool:
        map1, map2 = {}, {} # 1 to 1 mapping using to dictionaries
        phrase = phrase.split()
        if len(pattern) != len(phrase):
            return False
        for let, word in zip(pattern, phrase):
            if (let in map1 and map1[let] != word) or (word in map2 and map2[word] != let):
                return False
            map1[let], map2[word] = word, let
        return True
        
    # @StefanPochmann
    def wordPattern(self, s: str, t: str):
        t = str.split()
        return map(s.find, s) == map(t.index, t)
    
    def wordPattern(self, s: str, t: str):
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

    def wordPattern(self, pattern: str, phrase: str) -> bool:
        map_index = {}
        words = phrase.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in map_index:
                map_index[char_key] = i
            
            if char_word not in map_index:
                map_index[char_word] = i 
            
            if map_index[char_key] != map_index[char_word]:
                return False
        return True
