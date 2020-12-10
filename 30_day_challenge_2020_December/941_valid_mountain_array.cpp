/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20201210
* Problem link      : https://leetcode.com/problems/valid-mountain-array/
****************************************************************/

class Solution {
public:
// bool validMountainArray(vector<int>& arr) {
//     int n = arr.size();
//     int i = 0, j = n - 1;
//     for (; i + 1 < n; i++ ){
//         if (arr[i] >= arr[i+1])
//             break;
//     }
//     for (; j > 0; j-- ){
//         if (arr[j-1] <= arr[j])
//             break;
//     }        
//     return (n >= 3 && 0 < i && i == j && j < n-1);
// }

// @lee215
bool validMountainArray(vector<int>& A) {
    int n = A.size(), i = 0, j = n - 1;
    while (i + 1 < n && A[i] < A[i + 1]) i++;
    while (j > 0 && A[j - 1] > A[j]) j--;
    return i > 0 && i == j && j < n - 1;
}

};

