import re
import sys

sys.path.append("../helper")
import utils

utils.challenge_day("3")

sample = True
sample = False
input_file = "input_sample.txt" if sample else "input.txt"
with open(input_file, mode="r") as file:
    content = file.read()

# part 1
pattern = r"mul\(\d{0,9},\d{0,9}\)"

# Find all matches
matches = re.findall(pattern, content)

pattern = r"\d+"
part1Count = 0
for m in matches:
    # extract digits and multiply
    matches = re.findall(pattern, m)
    part1Count += int(matches[0]) * int(matches[1])

utils.print_output(
    part1Count,
    "What do you get if you add up all of the results of the multiplications?",
)

# part 2
pattern = r"(mul\(\d{0,9},\d{0,9}\))|(don't\(\))|(do\(\))"

# Find all matches
matches = re.findall(pattern, content)
print(matches)

# lets build array of only valid data
ignore_data = False
valid_data = []
for m in matches:
    if m[1] == "don't()":
        ignore_data = True

    if m[2] == "do()":
        ignore_data = False

    if ignore_data == False and m[0]:
        valid_data.append(m[0])


print(valid_data)

pattern = r"\d+"
part2Count = 0
for m in valid_data:
    # extract digits and multiply
    matches = re.findall(pattern, m)
    part2Count += int(matches[0]) * int(matches[1])

utils.print_output(
    part2Count,
    "what do you get if you add up all of the results of just the enabled multiplications?",
)
