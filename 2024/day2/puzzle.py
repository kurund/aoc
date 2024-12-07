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
    safe = 0
    if checkIfIncrementing(row):
        safe = 1
    elif checkIfDecrementing(row):
        safe = 1

    return safe


df["safe"] = df.apply(checkForSafePart1, axis=1)

utils.print_output(df["safe"].sum(), "How many reports are safe?")
