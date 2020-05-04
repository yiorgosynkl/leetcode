################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200504
# Problem link      : https://leetcode.com/problems/number-complement/
################################################################

class Solution:
    def findComplement(self, num: int) -> int:
        return 2 ** num.bit_length() - 1 - num
    
    # shift-right and bitwise or will find the mask 
    # XOR will mask will find the complementary number
    # int findComplement(int num) {
    #     int mask = num;
    #     mask |= mask >> 1;
    #     mask |= mask >> 2;
    #     mask |= mask >> 4;
    #     mask |= mask >> 8;
    #     mask |= mask >> 16;
    #     return num ^ mask;
    # }
