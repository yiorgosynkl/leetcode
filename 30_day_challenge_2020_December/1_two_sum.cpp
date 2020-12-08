/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20201208
* Problem link      : https://leetcode.com/problems/two-sum/
****************************************************************/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash; // number : index
        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            int num = nums[i], otherNum = target - nums[i];
            if ( hash.find(otherNum) != hash.end() ){
                res.push_back(hash[otherNum]);
                res.push_back(i);
                return res;
            }
            hash[num] = i;
        }
        return res; // code never reaches here
        
    }
};