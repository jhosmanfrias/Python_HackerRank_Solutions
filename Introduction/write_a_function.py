#################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                           #
#################################################################################################


def is_leap(year):
    leap = False
    
    year_mod_4   = year % 4
    
    year_mod_100 = year % 100
    
    year_mod_400 = year % 400
    
    if year_mod_4 == 0:
        if year_mod_100 == 0 and year_mod_400 != 0:
            return False
        else:
            return True
    
    return leap

year = int(input())
print(is_leap(year))
