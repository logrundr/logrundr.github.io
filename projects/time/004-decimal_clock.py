# Aodhan clock #

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

while True:
    current_time = datetime.datetime.now()
    t = current_time.hour + (current_time.minute / 60) + (current_time.second / 3600) + \
        (current_time.microsecond / 3600000000)
    t2 = t / 2.4
    t3 = str(floor(t2 * 10000))
    t4 = str(t3).zfill(5)
    print(f"{t4[0]}:{t4[1]}{t4[2]}:{t4[3]}{t4[4]}", end='\r')
