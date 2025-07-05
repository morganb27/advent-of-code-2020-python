from utils import *

PUZZLE = open("input.txt").read().split("\n\n")
PART_1 = PART_2 = 0

REQUIRED = {
"byr",
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid",
}

def validate(p):
    return (
        "byr" in p and 1920 <= int(p["byr"]) <= 2002 and
        "iyr" in p and 2010 <= int(p["iyr"]) <= 2020 and
        "eyr" in p and 2020 <= int(p["eyr"]) <= 2030 and
        "hgt" in p and (
            (p["hgt"].endswith("cm") and 150 <= int(p["hgt"][:-2]) <= 193) or
            (p["hgt"].endswith("in") and 59 <= int(p["hgt"][:-2]) <= 76)
        ) and 
        "hcl" in p and p["hcl"].startswith("#") and len(p["hcl"]) == 7 and all(c in "0123456789abcdef" for c in p["hcl"][1:]) and
        "ecl" in p and p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and
        "pid" in p and len(p["pid"]) == 9 and all(c in "0123456789" for c in p["pid"])
    )

for block in PUZZLE:
    passport = dict(kv.split(":") for kv in block.split())
    print(passport)
    if REQUIRED.issubset(passport):
        PART_1 += 1
    if validate(passport):
        PART_2 += 1

print(PART_1)
print(PART_2)