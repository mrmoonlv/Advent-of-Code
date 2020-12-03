#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10000)

class Walker:
    f = open("data.txt", "r")
    lines = f.read().splitlines()
    x = 1
    y = 1
    step_right = 1
    step_down = 1
    trees = 0
    result = 1
    trajectory_trees = []
    current_trajectory = 0
    w = len(lines[0])
    h = len(lines)
    trajectories = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2],
    ]

    def controlTower(self):
        if(self.current_trajectory >= len(self.trajectories)):
            print("All flights finished. Counting trajectories trees...")
            print(self.trajectory_trees)

            for trees in self.trajectory_trees:
                self.result = self.result * trees

            print("Number of trees encountered on each of the listed slopes", self.result)
            sys.exit()

        print("===Control tower", "Set new flight===")
        self.x = 1
        self.y = 1
        trajectory = self.trajectories[self.current_trajectory]
        self.step_right = trajectory[0]
        self.step_down = trajectory[1]
        self.walk()

    def land(self):
        print("Ship landed with current trajectory:", self.current_trajectory+1)
        print(self.trees, "encountered in trajectory:", self.current_trajectory+1)
        print("======================")
        self.current_trajectory += +1
        self.trajectory_trees.append(self.trees)
        self.trees = 0
        self.controlTower()

    def walk(self):
        if(self.y+self.step_down > self.h):
            self.land()

        if(self.x+self.step_right > self.w):
            self.x = self.x+self.step_right - self.w
        else:
            self.x = self.x + self.step_right

        self.y = self.y + self.step_down

        if(self.lines[self.y-1][self.x-1] == '#'):
            self.trees += +1

        self.walk()


walker = Walker()
walker.controlTower()
