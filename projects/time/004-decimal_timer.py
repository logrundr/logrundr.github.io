# Aodhan Timer & Stopwatch #

import datetime
from math import *
import sys
import os


# from https://stackoverflow.com/questions/5174810/how-to-turn-off-blinking-cursor-in-command-window
if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()


hide_cursor()

t = None
time = 0
print("0:00:00", end='\r')

def time_calculator(current_time):
    t = str(((current_time.hour + (current_time.minute / 60) + (current_time.second / 3600) + \
        (current_time.microsecond / 3600000000)) / 2.4) * 10000)
    return t

t = time_calculator(datetime.datetime.now())

while True:
    if abs(float(t) - float(time_calculator(datetime.datetime.now()))) >= 1:
        t = time_calculator(datetime.datetime.now())

        time += 1
        t1 = str(time).zfill(5)
        print(f"{t1[0]}:{t1[1]}{t1[2]}:{t1[3]}{t1[4]}", end='\r')

