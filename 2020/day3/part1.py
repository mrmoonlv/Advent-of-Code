#!/usr/bin/env python3

import sys

class Walker:
    f = open("data.txt", "r")
    lines = f.read().splitlines()
    x = 1
    y = 1
    squares = 0
    trees = 0
    w = len(lines[0])
    h = len(lines)
    landed = 0

    def walk(self):
        if(self.y+1 > self.h):
            self.land()

        if(self.x+3 > self.w):
            self.x = self.x+3 - self.w
        else:
            self.x = self.x + 3


        self.y = self.y + 1

        if(self.lines[self.y-1][self.x-1] == '.'):
            self.squares += +1
        else:
            self.trees += +1

    def land(self):
        print("Ship landed")
        print(self.trees, "encountered")
        print("======================")
        sys.exit()

walker = Walker()

while True:
    walker.walk()



