import re

data = [line.strip() for line in open("input.txt", "r")]


# Part 1

count = 0

for line in data:
    (left_half, right_half) = line.split(":")
    (lower_limit, upper_limit) = left_half[0:-2].split("-")
    character = left_half[-1]
    password = right_half.strip()

    char_count = password.count(character)

    if char_count <= int(upper_limit) and char_count >= int(lower_limit):
        count += 1

print(f"The answer to the first part is {count}")


# Part 2

count_2 = 0

for line in data:
    (left_half, right_half) = line.split(":")
    (first_index, second_index) = left_half[0:-2].split("-")
    character = left_half[-1]
    password = right_half.strip()

    # this is super ugly code, but only one of the positions can have the character
    # please don't judge me, I just want the answer
    if (password[int(first_index) - 1] == character) and (
        password[int(second_index) - 1] == character
    ):
        continue

    if (password[int(first_index) - 1] == character) or (
        password[int(second_index) - 1] == character
    ):
        count_2 += 1

print(f"The answer to the second part is {count_2}")