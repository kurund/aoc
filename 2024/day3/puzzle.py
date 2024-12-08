import re
import sys

sys.path.append("../helper")
import utils

utils.challenge_day("3")

# sample = True
sample = False
input_file = "input_sample.txt" if sample else "input.txt"
with open(input_file, mode="r") as file:
    content = file.read()

# part 1
pattern = r"mul\(\d{0,9},\d{0,9}\)"

# Find all matches
matches = re.findall(pattern, content)
print(matches)

pattern = r"\d+"
part1Count = 0
for m in matches:
    print(m)
    # extract digits and multiply
    matches = re.findall(pattern, m)
    print(matches)
    part1Count += int(matches[0]) * int(matches[1])

utils.print_output(
    part1Count,
    "What do you get if you add up all of the results of the multiplications?",
)
