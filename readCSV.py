import os
import csv

csvPath = os.path.expanduser("~/examples/csv/cglist.csv")
with open(csvPath) as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	for row in csvReader:
		print(row)
