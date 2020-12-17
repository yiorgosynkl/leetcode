/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20201217
* Problem link      : https://leetcode.com/problems/4sum-ii/
****************************************************************/

class Solution {
public:
    // int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
    //     unordered_map<int, int>  abSum;
    //     for (int a: A){
    //         for (int b: B){
    //             abSum[a+b]++;
    //         }
    //     }
    //     int count = 0;
    //     for (int c: C){
    //         for (int d: D){
    //             auto it = abSum.find(0 - c - d);
    //             if(it != abSum.end()) {
    //                 count += it->second;
    //             }
    //         }
    //     }
    //     return count;
    // }
    
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        int res = 0;
        unordered_map<int, int> AB;
        for (int a : A)
            for (int b : B)
                AB[a + b]++;
        for (int c : C)
            for (int d : D)
                res += AB[-c - d];
        return res;
    }
};