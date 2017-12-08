
import csv
from matplotlib import pyplot as plt

# CREATE_AXIS: create y-axis for list of entries
# input: entries (as list)
# output: number of entries with start date in a given month (as list)
def create_axis(entries):
    yaxis = [0 for x in range(12)]
    for entry in entries:
        # pull out month from entry
        start_date = entry['start date']
        split_date = start_date.split('/')
        month = int(split_date[1])
        # add it to matching month in the axis
        yaxis[month-1] += 1
    return yaxis    

# read in contents of file
prefix = '../../../'
f = open(prefix + 'data/church_metal_theft.csv','r')

# parse lines into spreadsheet-type format, with each line as dict
r = csv.DictReader(f,delimiter='|')
spreadsheet = []
for row in r:
    row['text'] = row['text'].lower()
    spreadsheet.append(row)

# all crimes involving lead
lead = filter(lambda x : 'lead' in x['text'], spreadsheet)
lead_yaxis = create_axis(lead)

# all crimes involving copper
copper = filter(lambda x : 'copper' in x['text'], spreadsheet)
copper_yaxis = create_axis(copper)

# all crimes 
total_yaxis = create_axis(spreadsheet)

# map month numbers to their names to create x-axis
d = {12 : 'December', 1 : 'January', 2 : 'February',
     3 : 'March', 4 : 'April', 5 : 'May',
     6 : 'June', 7 : 'July', 8 : 'August',
     9 : 'September', 10 : 'October', 11 : 'November'}
xaxis = map(lambda x : d[x+1], range(12))

# get related data for all y axes, need axis data, color, label, offset
yaxes = [{'axis' : copper_yaxis, 'col' : 'red', 'lab' : 'copper', 'off' : -0.2},
         {'axis' : lead_yaxis, 'col' : 'blue', 'lab' : 'lead', 'off' : 0},
         {'axis' : total_yaxis, 'col' : 'black', 'lab' : 'total', 'off' : 0.2}]

# map all bars according to their related data
for d in yaxes:
    plt.bar(map(lambda x : x + d['off'], range(len(xaxis))), d['axis'], 
            width=0.2, align='center', color = d['col'], label=d['lab'])

plt.xlabel('Month')
plt.ylabel('Number of crimes')
# rotate the x ticks as month names are fairly long
plt.xticks(range(len(xaxis)), xaxis, fontsize=8, rotation=45)
plt.xlim([-0.5,11.5])
plt.legend(loc='best',fontsize=9)
plt.tight_layout()

plt.savefig('months.pdf')

