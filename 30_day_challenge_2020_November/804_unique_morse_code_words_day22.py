################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201122
# Problem link      : https://leetcode.com/problems/unique-morse-code-words/
################################################################

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mors = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lets = 'abcdefghijklmnopqrstuvwxyz'
        trans = {lets[i]:mors[i] for i in range(26)}
        mors_words = [''.join([trans[c] for c in word]) for word in words]
        return len(set(mors_words))
    
    
    # # @lee215
    # def uniqueMorseRepresentations(self, words):
    #     d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
    #          "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    #     return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})
        