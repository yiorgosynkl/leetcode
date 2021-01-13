/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20210113
* Problem link      : https://leetcode.com/problems/boats-to-save-people/
****************************************************************/

class Solution {
public:
    int numRescueBoats(vector<int> people, int limit) {
        int boats = 0, lo = 0, hi = people.size() - 1;
        sort(people.begin(), people.end()); // sort ascending
        while (lo <= hi){
            if (people[lo] + people[hi] <= limit) lo++;
            hi--; boats++;
        }
        return boats;
    }
    
    // // @lee215
    // int numRescueBoats(vector<int> people, int limit) {
    //     int i, j;
    //     sort(people.rbegin(), people.rend());
    //     for (i = 0, j = people.size() - 1; i <= j; ++i)
    //         if (people[i] + people[j] <= limit) j--;
    //     return i;
    // }
};