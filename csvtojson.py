import csv
import json
import os

csvFilePath = os.path.join(os.getcwd(), "h1b.csv")
jsonFilePath = os.path.join(os.getcwd(), 'parsed1.json')

data = {}
i = 0
with open(csvFilePath, encoding="utf8") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        if i > 50: break
        id1 = rows['id']
        data[id1] = rows
        i += 1

with open(jsonFilePath, "w", encoding="utf8") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
