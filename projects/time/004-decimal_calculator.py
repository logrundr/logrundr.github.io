# Aodhan clock calculator #

from math import *


def calculator():
    time = input("What time? (12:34:56) ")
    t    = time.split(":")
    t2   = int(t[0]) + (int(t[1]) / 60) + (int(t[2]) / 3600)
    t3   = t2 / 2.4
    t4   = str(floor(t3 * 10000))
    zero = t4.zfill(5)
    print(zero[0] + ":" + zero[1] + zero[2] + ":" + zero[3] + zero[4])

    again = input("Again? (y/n)")
    if again == "y":
        calculator()
    else:
        pass


calculator()
