import sys

import pandas as pd

sys.path.append("../helper")
import utils

utils.challenge_day("2")

# provided file includes variable columns hence we cannot directly
# use dataframes. we need to add column header for max column length

# first lets find the maximum column for all the rows
# with open("input_sample.csv", "r") as temp_f:
with open("input.csv", "r") as temp_f:
    # get No of columns in each line
    col_count = [len(l.split(" ")) for l in temp_f.readlines()]

# generate column names
column_names = [i for i in range(max(col_count))]

# read csv file
# df = pd.read_csv("input_sample.csv", header=None, delimiter=" ", names=column_names)
df = pd.read_csv("input.csv", header=None, delimiter=" ", names=column_names)

utils.print_output(df, "All records")


def debug(text, data):
    showMessage = False
    # showMessage = True
    if showMessage:
        print(text, data, "\n")


# check if columns in a row are increasing
def checkIfIncrementing(row):
    for i in range(1, len(row)):
        # print("Checking increasing col i:", row[i], "col i-1:", row[i - 1])

        row_diff = row[i] - row[i - 1]
        debug("Col diff", row_diff)
        if row_diff < 1 or row_diff > 3:
            debug("Does not meet increasing criteria", "\n")
            return False

    debug("Increasing", "\n")
    return True


# check if columns in a row are decreasing
def checkIfDecrementing(row):
    for i in range(1, len(row)):
        # print("Checking decreasing col i", row[i], "row i-1", row[i - 1])

        row_diff = row[i] - row[i - 1]
        debug("Col diff", row_diff)
        if row_diff > -1 or row_diff < -3:
            debug("Does not meet decreasing criteria", "\n")
            return False

    debug("Decreasing", "\n")
    return True


# part 1
def checkForSafePart1(row):
    if checkIfIncrementing(row) or checkIfDecrementing(row):
        return 1
    return 0


df["safe"] = df.apply(checkForSafePart1, axis=1)

part1Total = df["safe"].sum()
utils.print_output(part1Total, "How many reports are safe?")

# part 2
# get only unsafe records
unsafe_data = df.loc[df["safe"] == 0].copy()
unsafe_data = unsafe_data.drop(columns=["safe"])

debug("unsafe data", unsafe_data)


def checkForSafePart2(row):
    for i in range(len(row)):
        altered_row = row.copy()
        altered_row.drop(index=i, inplace=True)
        altered_row.reset_index(drop=True, inplace=True)
        debug("altered row \n", altered_row)
        if checkForSafePart1(altered_row):
            return 1

    return 0


unsafe_data["safe"] = unsafe_data.apply(checkForSafePart2, axis=1)
part2Total = unsafe_data["safe"].sum()
debug("filetered data", unsafe_data)
utils.print_output(part1Total + part2Total, "How many reports are now safe?")
