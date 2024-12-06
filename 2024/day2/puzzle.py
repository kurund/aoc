import sys

import pandas as pd

sys.path.append("../helper")
import utils

utils.challenge_day("2")

# read csv file
df = pd.read_csv("input_sample.csv")
# df = pd.read_csv("input.csv")

utils.print_output(df, "All records")
