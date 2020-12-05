#!/usr/bin/env python3
from typing import List, Any, Callable


class FindSeat:
    f = open("data.txt", "r")
    lines = f.read().splitlines()
    row = 0
    column = 0
    id = 0
    ids = []
    seatsTaken = []

    rows = range(128)
    columns = range(8)

    def findOwnSeat(self):
        for seatID in self.ids:
            if (seatID + 1 in self.ids) and (seatID - 1 in self.ids):
                self.seatsTaken.append(seatID)

        self.seatsTaken.sort()
        diff: Callable[[Any, Any], List[Any]] = lambda l1, l2: [x for x in l1 if x not in l2]
        emptySeats = diff(self.ids, self.seatsTaken)
        emptySeats.sort()

        emptySeats.remove(emptySeats[0])
        emptySeats = emptySeats[:len(emptySeats) - 1]
        yourSeatRange = range(emptySeats[0], emptySeats[1])
        print("Your Seat ID: ", yourSeatRange[1])

    def boarding(self):
        for line in self.lines:
            self.id, self.row, self.column = 0, 0, 0
            self.rows = range(128)
            self.columns = range(8)

            r_locs = line[0:7]
            c_locs = line[7:10]

            for r_loc in r_locs:
                self.rows = getPosition(r_loc, self.rows)
                if len(self.rows) == 1:
                    for row in self.rows:
                        self.row = int(row)

            for c_loc in c_locs:
                self.columns = getPosition(c_loc, self.columns)
                if len(self.columns) == 1:
                    for column in self.columns:
                        self.column = int(column)

            self.id = self.row * 8 + self.column
            self.ids.append(self.id)
        self.findOwnSeat()


def getPosition(char, range):
    if char in ["F", "L"]:  # lower
        return range[:len(range) // 2]
    if char in ["B", "R"]:  # upper
        return range[len(range) // 2:]


FindSeat().boarding()
