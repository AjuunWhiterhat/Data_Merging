import csv
import pandas as pd 

data = pd.read_csv("Dwarf_Stars.csv")
df = data.dropna(axis=0, how="any")
df.drop("Unnamed: 0",axis=1,inplace=True)


df["radius"] = df["radius"] * 0.102763

for index,data_row in enumerate(df["mass"]):
    data_row = float(data_row) * 0.000954588
    df["mass"][index] = data_row

for index,data_row in enumerate(df["radius"]):
    data_row = float(data_row) * 0.102763
    df["mass"][index] = data_row


df.to_csv('Dwarf_Stars_Final.csv')