/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20201204
* Problem link      : https://leetcode.com/problems/the-kth-factor-of-n/
****************************************************************/

class Solution {
public:
    // // O(n) implementation
    // int kthFactor(int n, int k) {
    //     for (int d = 1; d <= n / 2; ++d)
    //         if (n % d == 0 && --k == 0)
    //             return d;
    //     return k == 1 ? n : -1;
    // }
    
    // complexity: O(n^0.5) , space: O(1)
    int kthFactor(int n, int k) {
        int d = 1;
        for (; d * d < n; ++d)
            if (n % d == 0 && --k == 0)
                return d;
        if (d * d == n && --k == 0)
            return d;
        for (d = d - 1; d >= 1; --d) {
            if (n % d == 0 && --k == 0)
                return n / d;
        }
        return -1;
    }
};