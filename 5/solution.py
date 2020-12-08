from itertools import groupby
import os, sys

data = [line.strip() for line in open(os.path.join(sys.path[0], "input.txt"), "r")]
solution = open(os.path.join(sys.path[0], "solution.txt"), "w")


print(f"The answer to part 1 is {answer}")
solution.write(f"The answer to part 1 is {answer}")

solution.close()
