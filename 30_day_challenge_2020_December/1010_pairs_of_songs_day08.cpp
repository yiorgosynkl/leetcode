/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20201208
* Problem link      : https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
****************************************************************/

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int> c(60);
        int res = 0;
        for (int t : time){
            res += c[(60 - t % 60) % 60]; // second % for special case where t = 0 => 60 - t = 60
            // res += t > 0 ? c[60 - t % 60] : c[0];
            c[t % 60]++;
        }
        return res;
    }
};