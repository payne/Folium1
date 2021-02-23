import csv
import json

# Set up variables
batchTot = 91
allLocations = []
locationsTotal = {}

# Get info for every json batch file
for i in range(1, batchTot + 1):
    with open("jsonFiles/batch" + str(i) + ".json", "r") as read_file:
        batch = json.load(read_file)
        # Check if file is not a dict with no data
        if type(batch) is not dict:
            for person in range(len(batch)):
                try:
                    allLocations.append(batch[person]['current_location']['name'])
                except TypeError:
                    pass


# Create a dictionary with the frequency of recursers locations
for place in allLocations:
    if place not in locationsTotal:
        locationsTotal[place] = 1
    else:
        locationsTotal[place] += 1

# Create csv file based on dictionary of recursers location frequency
with open('RClocationFreq2.csv', 'w', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    for key, value in locationsTotal.items():
        writer.writerow([key, value])
