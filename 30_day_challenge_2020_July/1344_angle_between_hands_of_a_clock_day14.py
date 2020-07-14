################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200714
# Problem link      : https://leetcode.com/problems/angle-between-hands-of-a-clock/
################################################################

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_turn = minutes / 60 # 0 to 1
        hour_turn = ( hour % 12 / 12 + minutes_turn / 12 ) # 0 to 1
        dif_turn = abs(minutes_turn - hour_turn) * 360
        return min(dif_turn, 360 - dif_turn)
    
    # math solution 
    # def angleClock(self, hour, minutes):
    #     H_place = 30*hour + 0.5*minutes # 360 / 12 = 30 degrees per hour, 30 / 60 = 0.5 degree per minute
    #     M_place = 6*minutes # 360 / 60 = 6 degrees per minute
    #     diff = abs(H_place - M_place)
    #     return diff if diff <= 180 else 360 - diff 
    # def angleClock(self, hour, minutes):
    #     return min(abs(30*hour-5.5*minutes),360-abs(30*hour-5.5*minutes))

        