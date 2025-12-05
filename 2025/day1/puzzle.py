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


def part2(data, starting_position):
    print("Solving part 2!")
    # print(data)
    print("Starting position:" + " " + str(starting_position))

    # we need follow the same logic as in part1
    # however besides checking how many times
    # we got 0, we also need to count how many times
    # we passed 99 which means reset happened
    # or we might have gone to negative

    current_position = starting_position
    zero_count = 0
    reset_count = 0

    # loop through data
    for index, row in data.iterrows():
        # get the instruction ("L20" or "R20")
        instruction = row.iloc[0]

        # parse direction and value
        direction = instruction[0]  # 'L' or 'R'
        value = int(instruction[1:])  # The number after L or R

        print(f"{instruction} - Current Position: {current_position}")

        prev_reset_count = reset_count

        # check if we will pass 99 or went to negative (reset happens)
        # before calculating new position
        # we need to consider R1000 scenario when reset might happen multiple times

        previous_position = current_position

        # calculate new position
        if direction == "L":
            current_position -= value
        elif direction == "R":
            current_position += value

        # count how many times we got 0
        if current_position % 100 == 0:
            zero_count += 1

        # always count if we pass 0
        reset_count += abs(current_position // 100 - previous_position // 100)

        if direction == "L":
            # if we are on zero count 1
            if current_position % 100 == 0:
                reset_count += 1

            # decrement to prevent double counting
            if previous_position % 100 == 0:
                reset_count -= 1

        print(f"{instruction} - New Position: {current_position}")
        print(f"Incremented by: {abs(prev_reset_count- reset_count)}")
        print(f"Reset count: {reset_count}\n")

    print(f"Part 1: Count instances when we got 0: {zero_count} times")
    print(f"Part 2: Count instances when reset happened: {reset_count} times")


# part1(df, starting_position)
part2(df, starting_position)
