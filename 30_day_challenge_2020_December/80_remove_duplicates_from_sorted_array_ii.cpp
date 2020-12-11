/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20201211
* Problem link      : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
****************************************************************/

class Solution {
public:
    // int removeDuplicates(vector<int>& nums) {
    //     if (nums.size() < 2)
    //         return nums.size();
    //     int s = 2, f = 2; // slow, fast pointer
    //     while (f < nums.size()){
    //         if (nums[s-2] < nums[f]) { // if 2nd last number is different than new one
    //             nums[s] = nums[f];
    //             s += 1;
    //         }
    //         f += 1;
    //     }
    //     return s;
    // }
    
    // @StefanPochmann
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        for (int n : nums)
            if (i < 2 || n > nums[i-2])
                nums[i++] = n;
        return i;
    }
};