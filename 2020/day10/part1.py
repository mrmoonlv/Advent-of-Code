#!/usr/bin/env python3

adapters = sorted(list(map(int, open('data.txt').read().splitlines())))
adapters.insert(0, 0)
device_volts = max(adapters) + 3
adapters.append(device_volts)
diff = [a - b for b, a in zip(adapters[:-1], adapters[1:])]
diff_1_jolts = diff.count(1)
diff_3_jolts = diff.count(3)
number = diff_1_jolts * diff_3_jolts

print("Number is:", number)

assert number == 2048
