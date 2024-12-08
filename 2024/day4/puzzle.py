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
            elif direction == "backword":
                index_value = matrix[row_index][column_index - i]
            elif direction == "top":
                index_value = matrix[row_index - i][column_index]
            elif direction == "down":
                index_value = matrix[row_index + i][column_index]

            xmas_string = xmas_string + index_value
        except IndexError:
            return False

    if xmas_string == "XMAS":
        # print("Found on row number:", row_index)
        return True


xmas_count = 0
for row_index, row in enumerate(matrix):
    for column_index, col in enumerate(row):
        if col == "X":
            if checkforXmas(matrix, row_index, column_index, "forward"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "backword"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "top"):
                xmas_count += 1

            if checkforXmas(matrix, row_index, column_index, "down"):
                xmas_count += 1

utils.print_output(xmas_count, "How many times does XMAS appear?")
