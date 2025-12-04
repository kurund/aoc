import csv
import sys

sys.path.append("../helper")
import utils

utils.challenge_day("4")

sample = True
# sample = False
input_file = "input_sample.txt" if sample else "input.txt"

# part 1
# lets build the matrix of letters
matrix = []
with open(input_file, mode="r") as file:
    lines = file.readlines()
    for line in lines:
        matrix.append(list(line.strip()))

print(matrix)


def checkforXmas(matrix, row_index, column_index, direction):
    xmas_string = "X"
    index_value = ""
    for i in range(1, 4):
        try:
            if direction == "forward":
                index_value = matrix[row_index][column_index + i]
            elif direction == "backward":
                if column_index - i < 0:
                    return False
                index_value = matrix[row_index][column_index - i]
            elif direction == "top":
                if row_index - i < 0:
                    return False
                index_value = matrix[row_index - i][column_index]
            elif direction == "bottom":
                index_value = matrix[row_index + i][column_index]
            elif direction == "top-left":
                if column_index - i < 0 or row_index - i < 0:
                    return False
                index_value = matrix[row_index - i][column_index - i]
            elif direction == "top-right":
                if row_index - i < 0:
                    return False
                index_value = matrix[row_index - i][column_index + i]
            elif direction == "bottom-left":
                if column_index - i < 0:
                    return False
                index_value = matrix[row_index + i][column_index - i]
            elif direction == "bottom-right":
                index_value = matrix[row_index + i][column_index + i]

            # print(index_value)
            xmas_string = xmas_string + index_value
        except IndexError:
            return False

    # print(xmas_string)
    if xmas_string == "XMAS":
        # print("Found on row number:", row_index)
        # print("Found on col number:", column_index)
        return True


xmas_count = 0
for row_index, row in enumerate(matrix):
    for column_index, col in enumerate(row):
        if col == "X":
            if checkforXmas(matrix, row_index, column_index, "forward"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "backward"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "top"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "bottom"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "top-left"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "top-right"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "bottom-left"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "bottom-right"):
                xmas_count += 1

utils.print_output(xmas_count, "How many times does XMAS appear?")

# part 2


def checkForMas(matrix, row_index, column_index):
    try:
        if row_index - 1 < 0 or column_index - 1 < 0:
            return False
        top_left = matrix[row_index - 1][column_index - 1]
        if (
            top_left == "M"
            and matrix[row_index - 1][column_index + 1] == "S"
            and matrix[row_index + 1][column_index - 1] == "M"
            and matrix[row_index + 1][column_index + 1] == "S"
        ):
            return True
    except IndexError:
        return False

    return False


xmas_count = 0
for row_index, row in enumerate(matrix):
    for column_index, col in enumerate(row):
        if col == "A":
            if checkForMas(matrix, row_index, column_index):
                xmas_count += 1

            # except IndexError:
            #     return False
            #

utils.print_output(xmas_count, "How many times does XMAS appear?")
