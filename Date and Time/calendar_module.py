################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                          #
################################################################################################

import calendar

mm, dd, yy = map(int, input().split())

print (calendar.day_name[calendar.weekday(yy,mm,dd)].upper())
