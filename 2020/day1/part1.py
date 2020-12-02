#!/usr/bin/env python3

import sys

f = open("data.txt", "r")
lines = f.read().splitlines()
for aa in lines :
    a = int(aa)
    for bb in lines:
        b = int(bb)
        if(a == b):
            continue
        if((a+b == 2020)):
            print("FOUND:", a*b)
            sys.exit()
