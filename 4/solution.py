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


# passport_data = (passport_attributes.split(" ") for passport_attributes in data)

# passports = lambda: (
#     passport_data
#     for passport_chunk in data_chunked_by_passport_slightly_cleaner()
#     for passport_data in passport_chunk
# )

# data_chunked_by_passport = (
#     list(g) for k, g in groupby(passport_data, lambda x: x != "") if k
# )


# data_chunked_by_passport_slightly_cleaner = lambda: (
#     passport_data.split(" ")
#     for passport_chunk in data_chunked_by_passport
#     for passport_data in passport_chunk
# )


# for passport in data_chunked_by_passport:
#     print(passport)

# passport_attributes
#             for passport_attributes in passport_data_split
#             for item in sublist


# print(list(passports))
# passports = (passport_list_to_object(passport) for passport in passports)

# def passport_list_to_object(passport_list):
#     passport_object = {}
#     for passport_list_item in passport_list:
#         print(passport_list_item)
#         (key, value) = passport_list_item.split(':')
#         passport_object[key] = value
#     return passport_object

# passports = (passport_list_to_object(passport) for passport in passports)


solution.write(f"The answer to part 1 is {answer}")

solution.close()
