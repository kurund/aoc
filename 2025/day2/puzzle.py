input_text = open("input_sample.txt").read().strip()

# split by commas
all_codes = input_text.split(",")

# loop throught all code ranges
for code_range in all_codes:
    print(f" Code range: {code_range}")
    [start_range, end_range] = code_range.split("-")

    for i in range(int(end_range), int(start_range) + 1):
        print(i)
