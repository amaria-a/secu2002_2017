
import csv

# read in contents of file, line by line
f = open('../../../data/church_metal_theft.csv','r')

# parse lines into spreadsheet-type format, with each line as dict
r = csv.DictReader(f,delimiter='|')
spreadsheet = []
for row in r:
    spreadsheet.append(row)

