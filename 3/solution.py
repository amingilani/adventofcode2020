import os, sys

data = [line.strip() for line in open(os.path.join(sys.path[0], "input.txt"), "r")]
solution = open(os.path.join(sys.path[0], "solution.txt"), "w")


## Part 1

count = 0

for (index, line) in enumerate(data):
    # skip the first iteration
    if index == 0:
        continue

    if line[(index * 3) % len(line)] == "#":
        count += 1
print(f"The answer to part 1 is #{count}")
solution.write(f"The answer to part 1 is {count}")

## Part 2


def count_trees(data, deltay, deltax):
    county = 0

    for (line_index, line_data) in enumerate(data):
        character_index = line_index * deltay // deltax
        wrapped_character_index = character_index % len(line_data)
        # print(f"X,Y coordinates are ({character_index}, {line_index})")
        # print(f"X,Y coordinates are {character_index}, {line_index}")

        print(f"max index is {len(line_data) - 1}")
        print(f"character_index is {character_index}")
        print(f"wrapped to {wrapped_character_index}")

        if line_data[wrapped_character_index] == "#":
            county += 1

    return county


ans1 = count_trees(data, 1, 1)
ans2 = count_trees(data, 3, 1)
ans3 = count_trees(data, 5, 1)
ans4 = count_trees(data, 7, 1)
ans5 = count_trees(data, 1, 2)
final_anser = ans1 * ans2 * ans3 * ans4 * ans5

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
print(f"The answer to part 2 is {final_anser}")
solution.write(f"The answer to part 2 is {final_anser}")

solution.close()