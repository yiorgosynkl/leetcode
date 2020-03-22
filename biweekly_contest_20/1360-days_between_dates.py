################################################################
# Project           : leetcode
# Program name      : 1360-days_between_dates.py.cpp
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200223
# Description       : write a program to count the number of days between two dates.
################################################################

from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.strptime(date2, '%Y-%m-%d')
        return (abs((d1-d2).days))