import pandas as pd

# read csv file
# df = pd.read_csv("input_sample.csv")
df = pd.read_csv("input.csv")


starting_position = 50


def part1(data, starting_position):
    print("Solving part 1!")
    # print(data)
    print("Starting position:" + " " + str(starting_position))

    # we need to calculate the value for each row based on instruction
    # print it and pass as a input to the next row calulation
    # for eg if row value is L20 then do 50-20
    # if R20 then do 50+20
    # Note the values goes from 0-99
    # for example if starting value is 98 and row value is R20
    # then calculated value will be 18
    # for example if starting_position is 10 and row value is L20
    # then calculated value will be 90

    current_position = starting_position
    zero_count = 0

    # loop through data
    for index, row in data.iterrows():
        # get the instruction ("L20" or "R20")
        instruction = row.iloc[0]

        # parse direction and value
        direction = instruction[0]  # 'L' or 'R'
        value = int(instruction[1:])  # The number after L or R

        # calculate new position based on direction
        if direction == "L":
            current_position = (current_position - value) % 100
        elif direction == "R":
            current_position = (current_position + value) % 100

        # count how many times we got 0
        if current_position == 0:
            zero_count += 1

        print(f"Row {index}: {instruction} - Position: {current_position}")

    print(f"Count instances when we got 0: {zero_count} times")


part1(df, starting_position)
