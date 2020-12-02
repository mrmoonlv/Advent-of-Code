#!/usr/bin/env python3

import sys

f = open("data.txt", "r")
lines = f.read().splitlines()
for aa in lines :
    a = int(aa)
    for bb in lines:
        b = int(bb)
        for cc in lines:
            c = int(cc)
            if(c == a):
                continue
            if(c == b):
                continue

            if((a+b+c == 2020)):
                print("FOUND:", a*b*c)
                sys.exit()
