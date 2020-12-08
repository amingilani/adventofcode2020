from itertools import groupby
import os, sys

data = [line.strip() for line in open(os.path.join(sys.path[0], "input.txt"), "r")]
solution = open(os.path.join(sys.path[0], "solution.txt"), "w")

joined_data = ("---").join(data)

passports_raw = joined_data.split("------")

passports = []

for passport_data in passports_raw:
    passport = []
    for passport_data_chunks in passport_data.split("---"):
        passport += passport_data_chunks.split(" ")
    passports.append(passport)


def passport_array_to_object(passport_array):
    passport = {}
    for passport_attribute_string in passport_array:
        (key, value) = passport_attribute_string.split(":")
        passport[key] = value
    return passport


passports = (passport_array_to_object(passport) for passport in passports)


def validate_passport(passport):
    return (
        passport.get("byr")
        and passport.get("iyr")
        and passport.get("eyr")
        and passport.get("hgt")
        and passport.get("hcl")
        and passport.get("ecl")
        and passport.get("pid")
    )


validate_passports = [passport for passport in passports if validate_passport(passport)]

answer = len(validate_passports)

print(f"The answer to part 1 is {answer}")


solution.write(f"The answer to part 1 is {answer}")

solution.close()
