/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20210122
* Problem link      : https://leetcode.com/problems/determine-if-two-strings-are-close/
****************************************************************/

class Solution {
public:
    // bool closeStrings(string word1, string word2) {
    //     vector<int>w1(26,0),w2(26,0);
    //     set<char>s1,s2;
    //     for(char c:word1){
    //         w1[c-'a']++;
    //         s1.insert(c);
    //     }
    //     for(char c:word2){
    //         w2[c-'a']++;
    //         s2.insert(c);
    //     }
    //     sort(begin(w1),end(w1));
    //     sort(begin(w2),end(w2));
    //     return w1==w2&&s1==s2;
    // }
    
    bool closeStrings(string word1, string word2) {
        vector<int> freq1(26,0),freq2(26,0),let1(26,0),let2(26,0); // frequencies and letters of each word
        for(char c:word1)
            freq1[c-'a']++,let1[c-'a'] = 1;
    
        for(char c:word2)
            freq2[c-'a']++,let2[c-'a'] = 1;
        
        sort(begin(freq1),end(freq1));  // sort frequencies
        sort(begin(freq2),end(freq2));
        return freq1==freq2&&let1==let2;
    }

};
