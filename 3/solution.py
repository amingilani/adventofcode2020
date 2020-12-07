import os, sys

data = [line.strip() for line in open(os.path.join(sys.path[0], "input.txt"), "r")]


count = 0

for (index, data) in enumerate(data):
    # skip the first interation
    if index == 0:
        continue

    if data[(index * 3) % len(data)] == "#":
        count += 1

print(count)
