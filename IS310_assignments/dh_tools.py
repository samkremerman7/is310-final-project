import csv
import pandas as pd
#with open("tools_dh_proceedings.csv", "r") as input_file:
#   csv_reader = csv.reader(input_file)
#    for i in csv_reader:
#        count = int(i["2015"]) + int(i["s2016"]) + int(i["2017"]) + int(i["2018"]) + int(i["2019"])
data_df = pd.read_csv("tools_dh_proceedings.csv")
data_df["Overall"] = data_df.sum(axis=1)
for i, row in data_df.iterrows():
    print(row["Tool"], ": 2015 count:", row["2015"], ", 2019 count:", row["2019"], ", Overall count:", row["Overall"])
def tool_select(data_tools_dh, tool):
    data_tools_dh["Overall"] = data_tools_dh.sum(axis=1)
    print(data_tools_dh.loc[data_tools_dh["Tool"] == tool])
def user_tool_select():
    tool = input("Input tool name: ")
    print(data_df.loc[data_df['Tool'] == tool])