from itertools import combinations
import os, sys

data = [line.strip() for line in open(os.path.join(sys.path[0], "input.txt"), "r")]
solution = open(os.path.join(sys.path[0], "solution.txt"), "w")

combs = combinations(data, 2)

for (num1, num2) in combs:
    if int(num1) + int(num2) == 2020:
        print(int(num1) * int(num2))
        solution.write(f"The answer to part 2 is {int(num1) * int(num2)}")

combs = combinations(data, 3)

for (num1, num2, num3) in combs:
    if int(num1) + int(num2) + int(num3) == 2020:
        print(int(num1) * int(num2) * int(num3))
        solution.write(f"The answer to part 2 is {int(num1) * int(num2) * int(num3)}")

solution.close()
