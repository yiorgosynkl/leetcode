/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20201205
* Problem link      : https://leetcode.com/problems/can-place-flowers/
****************************************************************/

class Solution {
public:
    bool canPlaceFlowers(vector<int>& fb, int n) {
        int c = 0;
        fb.insert( fb.begin() , 0 );
        fb.push_back(0);  
        for (int i = 1; i < fb.size() - 1; i++){    // 1, ..., n-2
            if (fb[i] == 0 && fb[i-1] == 0 && fb[i+1] == 0){
               fb[i] = 1;
               c++;
            }
        }
        return c >= n;
    }
};