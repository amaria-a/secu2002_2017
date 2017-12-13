
from datetime import datetime as dt
import csv
import utilities

# read in contents of file
prefix = '../../../data/'
f = open(prefix + 'church_metal_theft.csv','r')

# parse lines into spreadsheet-type format, with each line as dict 
# containing start time as time, free text field as text
r = csv.DictReader(f,delimiter='|')
spreadsheet = []
for row in r:
    start = dt.strptime(row['start date'], '%d/%m/%Y')
    text = row['text']
    spreadsheet.append({'date' : start, 'text' : text})

# now compare binary and linear search with several examples

date = '26/02/2011'
print date
date = dt.strptime(date,'%d/%m/%Y')
x = utilities.bin_find(date,spreadsheet)
y = utilities.lin_find(date,spreadsheet)
print '---------------'

date = '06/07/2009'
print date
date = dt.strptime(date,'%d/%m/%Y')
x = utilities.bin_find(date,spreadsheet)
y = utilities.lin_find(date,spreadsheet)
print '---------------'

date = '22/04/2013'
print date
date = dt.strptime(date,'%d/%m/%Y')
x = utilities.bin_find(date,spreadsheet)
y = utilities.lin_find(date,spreadsheet)
print '---------------'

date = '15/11/2010'
print date
date = dt.strptime(date,'%d/%m/%Y')
x = utilities.bin_find(date,spreadsheet)
y = utilities.lin_find(date,spreadsheet)
print '---------------'
