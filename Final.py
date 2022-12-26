import csv

dataset1 = []
dataset2 = []

with open ("Brightest_Stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open ("Dwarf_Stars_Final.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)



header1 = dataset1[0]
header2 = dataset2[0]

data_1 = dataset1[1:]
data_2 = dataset2[1:]

headers = header1 + header2

data = []

for index,data_row in enumerate(data_1):
    data.append(data_1[index]+data_2[index])

with open ("merged_dataset.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(data)
