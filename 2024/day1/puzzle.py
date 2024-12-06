import sys

import pandas as pd

sys.path.append("../helper")
import utils

utils.challenge_day("1")

# read csv file
# df = pd.read_csv('input_sample.csv')
df = pd.read_csv("input.csv")

# utils.print_output(df, 'All records')

# split into 2 dataframes
left_side = df.iloc[:, [0]]
right_side = df.iloc[:, [1]]


# Part 1
def part1(left_side, right_side):

    # lets sort both array's in descending order
    sorted_left_side = left_side.sort_values(
        by=left_side.columns[0], ascending=False
    ).reset_index(drop=True)
    sorted_right_side = right_side.sort_values(
        by=right_side.columns[0], ascending=False
    ).reset_index(drop=True)

    # utils.print_output(sorted_left_side, 'Sorted left side')
    # utils.print_output(sorted_right_side, 'Sorted right side')

    # create new dataframe left side - right side
    final_df = sorted_left_side["left_side"] - sorted_right_side["right_side"]

    # convert all to positive
    final_df = final_df.abs()
    # utils.print_output(final_df, 'Convert to positive output')

    # calculate the sum
    utils.print_output(final_df.sum(), "What is the total distance between your lists")


# Part 2
def part2(left_side, right_side):
    # count the occurrences of each value in right_side df
    right_counts = right_side["right_side"].value_counts()

    # now let's map the counts to left_side values
    left_side["count"] = left_side["left_side"].map(right_counts).fillna(0).astype(int)

    # multiply left_side * count
    left_side["multiply"] = left_side["left_side"] * left_side["count"]

    # utils.print_output(left_side, 'Left side')

    # calculate the sum
    utils.print_output(left_side["multiply"].sum(), "What is their similarity score?")


# run functions
part1(left_side, right_side)
part2(left_side, right_side)
