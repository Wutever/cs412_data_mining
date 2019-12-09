import csv
import json
import os


def get_csv(begin, end) :
    csvFilePath = os.path.join(os.getcwd(), "hotel_cleaned.csv")
    jsonFilePath = os.path.join(os.getcwd(), 'parsed1.json')

    data = {}
    i = begin
    with open(csvFilePath, encoding="utf8") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            if i > end:
                break
            data[i] = rows
            i += 1
        with open(jsonFilePath, "w", encoding="utf8") as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))


get_csv(0,100)