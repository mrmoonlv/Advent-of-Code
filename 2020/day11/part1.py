#!/usr/bin/env python3
import copy


def getSeats():
    data = []
    for line in open('data.txt').read().splitlines():
        row = []
        for seat in line:
            row.append(seat)
        data.append(row)

    return data


def getAroundSeats(y, x, seat_plan):
    around_seats = []
    width = len(seat_plan[0]) - 1
    height = len(seat_plan) - 1

    if y - 1 >= 0 and x <= width:
        around_seats.append((y - 1, x))
    if y - 1 >= 0 and x + 1 <= width:
        around_seats.append((y - 1, x + 1))
    if y <= height and x + 1 <= width:
        around_seats.append((y, x + 1))
    if y + 1 <= height and x + 1 <= width:
        around_seats.append((y + 1, x + 1))
    if y + 1 <= height and x <= width:
        around_seats.append((y + 1, x))
    if y + 1 <= height and x - 1 >= 0:
        around_seats.append((y + 1, x - 1))
    if y <= height and x - 1 >= 0:
        around_seats.append((y, x - 1))
    if y - 1 >= 0 and x - 1 >= 0:
        around_seats.append((y - 1, x - 1))

    return around_seats


def seatTaken(y, x, seat_plan):
    if seat_plan[y][x] == "#":
        return True
    else:
        return False


def isGoodSeat(y, x, seat_plan):
    air_quality = 0

    for y, x in getAroundSeats(y, x, seat_plan):
        if seat_plan[y][x] == "#":
            air_quality += 1

    if air_quality == 0:
        return True
    return False


def isBadSeat(y, x, seat_plan):
    air_quality = 0

    for y, x in getAroundSeats(y, x, seat_plan):
        if seat_plan[y][x] == "#":
            air_quality += 1

    if air_quality >= 4:
        return True
    return False


def seating(seat_plan):
    new_seats = copy.deepcopy(seat_plan)
    y = 0
    x = 0
    width = len(seat_plan[0])
    height = len(seat_plan)

    while x < width and y < height:
        if seat_plan[y][x] != '.':
            if not seatTaken(y, x, seat_plan):
                if isGoodSeat(y, x, seat_plan):
                    new_seats[y][x] = "#"

            elif seatTaken(y, x, seat_plan):
                if isBadSeat(y, x, seat_plan):
                    new_seats[y][x] = 'L'

        if x >= width - 1:
            y += 1
            x = 0
        else:
            x += 1

    return new_seats, sum(x.count("#") for x in new_seats)


seats = getSeats()
rounds = []
taken_seats = 0
while True:
    seats, taken_seats = seating(seats)
    rounds.append(taken_seats)
    if rounds.count(taken_seats) == 3:
        break

print("Found:", taken_seats)
assert taken_seats == 2483
