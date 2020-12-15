/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20201215
* Problem link      : https://leetcode.com/problems/squares-of-a-sorted-array/
****************************************************************/

#include <stdlib.h>     /* abs */
#include <math.h>       /* pow */

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> sq(nums.size());
        int le = 0, ri = nums.size() - 1;
        for (int df = nums.size() - 1; df >= 0; df--){
            if (abs(nums[le]) >= abs(nums[ri])){
                sq[df] = pow(nums[le++],2);
            } else {
                sq[df] = pow(nums[ri--],2);
            }
        }
        return sq;
    }
};