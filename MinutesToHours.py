#!/usr/bin/env python3
import sys
def Hours(MIN):
    if MIN < 0:
        raise ValueError("Input number cannot be negative")
    else:
        print("The time is {} H, {} M".format(int(MIN)//60,int(MIN)%60) )
try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")
