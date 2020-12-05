#!/usr/bin/env python3

class FindSeat:
    f = open("data.txt", "r")
    lines = f.read().splitlines()
    row = 0
    column = 0
    id = 0
    ids = []
    rows = range(128)
    columns = range(8)

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
            print(line, ": row:", self.row, ", column:", self.column, ', seat ID:', self.id)

        print("The highest seat ID on a boarding pass is:", max(self.ids))


def getPosition(char, range):
    if char in ["F", "L"]:  # lower
        return range[:len(range) // 2]
    if char in ["B", "R"]:  # upper
        return range[len(range) // 2:]


FindSeat().boarding()
