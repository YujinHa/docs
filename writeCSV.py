import os
import csv

with open('cglist.csv', mode='w') as csvfile:
	fieldnames = ['eq','seq', 'scene', 'shot', 'note']
	writer = csv.DictWriter(csvfile, fieldnames=title)
	writer.writeheader()
	writer.writerow({'eq':'1','seq': 'CAR', 'scene': 'FOO', 'shot': '0010', 'note': 'cg car'})
	writer.writerow({'eq':'1','seq': 'CAR', 'scene': 'FOO', 'shot': '0020', 'note': 'add dust'})
	writer.writerow({'eq':'1','seq': 'CAR', 'scene': 'BAR', 'shot': '0010', 'note': 'cg car, add dust'})
