import csv
import json

file_path = "employees.csv"

with open(file_path, mode='r') as csvfile:

    csvreader = csv.reader(csvfile)
    # read first row field names
    fields = next(csvreader)
    rows = []
    for row in csvreader:
        data_as_dict = {}
        i = 0
        for value in row:
            data_as_dict[fields[i]] = value
            i += 1
        rows.append(data_as_dict)
    json_data = json.dumps(rows, indent=4)
    print(json_data)
    print("Total number of row in csv file: %d" % (csvreader.line_num))
    # removing data from rows
    rows.clear()

print("Complete...")