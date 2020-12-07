import os, sys

data = [line.strip() for line in open(os.path.join(sys.path[0], "input.txt"), "r")]


## Part 1

count = 0

for (index, data) in enumerate(data):
    # skip the first interation
    if index == 0:
        continue

    if data[(index * 3) % len(data)] == "#":
        count += 1

print(f"The answer to part 1 is #{count}")

## Part 2


def count_trees(data, column_skip, odd_switch):
    county = 0

    for (index, data) in enumerate(data):
        # skip the first interation
        if index == 0:
            continue

        if odd_switch and not index % 2:
            continue

        if data[(index * column_skip) % len(data)] == "#":
            county += 1

    return county


ans1 = count_trees(data, 1, False)
ans2 = count_trees(data, 3, False)
ans3 = count_trees(data, 5, False)
ans4 = count_trees(data, 7, False)
ans5 = count_trees(data, 1, True)

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
print(f"The answer to part 2 is {ans1 * ans2 * ans3 * ans4 * ans5}")