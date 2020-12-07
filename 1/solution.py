from itertools import combinations

data = [line.strip() for line in open("input.txt", "r")]
combs = combinations(data, 2)

for (num1, num2) in combs:
    if int(num1) + int(num2) == 2020:
        print(int(num1) * int(num2))