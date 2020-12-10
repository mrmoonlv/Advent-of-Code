#!/usr/bin/env python3

adapters = sorted(list(map(int, open('data.txt').read().splitlines())))
adapters.insert(0, 0)
device_volts = max(adapters) + 3
adapters.append(device_volts)
variants = {0: 1}

for adapter_index in range(1, len(adapters)):
    diff_a = 0
    if adapters[adapter_index] - 1 in variants:
        diff_a = variants[adapters[adapter_index] - 1]

    diff_b = 0
    if adapters[adapter_index] - 2 in variants:
        diff_b = variants[adapters[adapter_index] - 2]

    diff_c = 0
    if adapters[adapter_index] - 3 in variants:
        diff_c = variants[adapters[adapter_index] - 3]

    variants[adapters[adapter_index]] = sum([diff_a, diff_b, diff_c])

ways = variants[adapters[-1]]

print("Total number of distinct ways you can arrange the adapters to connect the charging outlet to your device:", ways)
assert ways == 1322306994176
