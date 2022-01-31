##################################################################################################
# Challenge -> https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true #
# By        -> jhosmanfrias, Jan-2022                                                            #
##################################################################################################


from cmath import phase
from math import sqrt

com = input()

x = complex(com).real
y = complex(com).imag

print(sqrt(x**2+y**2))

print(phase(complex(com)))
