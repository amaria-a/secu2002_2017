
from datetime import datetime as dt
import csv
import utilities

# read in contents of file
prefix = '../../../data/'
f = open(prefix + 'shapeshift.csv','r')

# parse lines into spreadsheet-type format, with each line as dict
# containing start time as time, free text field as text
r = csv.DictReader(f,delimiter=',')
spreadsheet = []
for row in r:
    date = dt.fromtimestamp(float(row['timestamp'])).date()
    row['date'] = date
    spreadsheet.append(row)

# now order the spreadsheet according to the date/time
spreadsheet.sort(key = lambda x : x['date'])

# now compare binary and linear search with several examples

date = '05/10/2017'
date = dt.strptime(date,'%d/%m/%Y').date()
x = utilities.bin_find(date,spreadsheet)
y = utilities.lin_find(date,spreadsheet)
print '---------------'

date = '12/11/2017'
date = dt.strptime(date,'%d/%m/%Y').date()
x = utilities.bin_find(date,spreadsheet)
y = utilities.lin_find(date,spreadsheet)
print '---------------'

date = '02/12/2017'
date = dt.strptime(date,'%d/%m/%Y').date()
x = utilities.bin_find(date,spreadsheet)
y = utilities.lin_find(date,spreadsheet)
print '---------------'

