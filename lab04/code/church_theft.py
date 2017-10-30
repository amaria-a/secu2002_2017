
# CREATE_ROW: used to create dict-style row for spreadsheet
# input:    columns (as list)
# output:   row (as dict)
def create_row(columns):
    # columns are: (0) start date, 
    #              (1) start time, 
    #              (2) end date, 
    #              (3) end time, 
    #              (4) free text
    d = {'start date' : columns[0], 'start time' : columns[1],
         'end date' : columns[2], 'end time' : columns[3], 
         'text' : columns[4]}
    return d

# GET_SEASON: used to map month to season
# input:    month (as int)
# output:   season in which the month falls (as string)
def get_season(month):
    d = {12 : 'winter', 1 : 'winter', 2 : 'winter',
          3 : 'spring', 4 : 'spring', 5 : 'spring',
          6 : 'summer', 7 : 'summer', 8 : 'summer',
          9 : 'autumn', 10 : 'autumn', 11 : 'autumn'}
    if month in d.keys():
        return d[month]
    else:
        return 'you did not provide a valid month'

# GET_PRETTY_MONTH: used to map month number to word
# input:    months (as list of ints)
# output:   months (as list of strings)
def pretty_month(months): 
    d = {12 : 'December', 1 : 'January', 2 : 'February',
          3 : 'March', 4 : 'April', 5 : 'May',
          6 : 'June', 7 : 'July', 8 : 'August',
          9 : 'September', 10 : 'October', 11 : 'November'}
    pretty_months = []
    for m in months:
        if m in d:
            pretty_months.append(d[m])
        else:
            print 'entered an invalid month'
            return
    return pretty_months
 
# GET_MAX_MIN: used to get keys and values with both max and min value
# input:    d (as dict), assumed to have numeric values
# output:   keys with max value, max value, keys with min value, min value
def get_max_min(d):
    max_keys = []
    max_val = 0
    min_keys = []
    # pick any number that you know won't be exceeded
    min_val = 1000
    for key in d.keys():
        val = d[key]
        # if it's greater than max replace old max with this
        if val > max_val:
            max_keys = [key]
            max_val = val
        # if it's matching max then append (multiple keys take on max value)
        elif val == max_val:
            max_keys.append(key)
        # if it's less than min replace old min with this
        elif val < min_val:
            min_keys = [key]
            min_val = val
        # if it's matching min then append (multiple keys take on min value)
        elif val == min_val: 
            min_keys.append(key)
    return [max_keys,max_val,min_keys,min_val]

# read in contents of file, line by line
# this is hardcoded for my file system so will have to change!
prefix = '../../../data/'
f = open(prefix + 'church_metal_theft.csv','r')

# parse lines into spreadsheet-type format, with each line as dict
spreadsheet = []
for line in f:
    # split line into columns
    columns = line.split(':::')
    row = create_row(columns)
    spreadsheet.append(row)

# now create mappings to maintain number of crimes in both months and seasons
seasons = {'winter' : 0, 'spring' : 0, 'summer' : 0, 'autumn' : 0}
# this is a fancy way to create a dictionary with months as keys, 0 as value
months = dict.fromkeys(range(1,13),0)

# now go through crimes and put them into month and season buckets
for row in spreadsheet:
    # could also work according to end date
    start_date = row['start date']
    # date is as dd/mm/yyyy
    split_date = start_date.split('/')
    month = int(split_date[1])
    # count entry in both month it occurred
    months[month] += 1
    # and in season
    season = get_season(month)
    seasons[season] += 1

# now get and print all values for seasons
[max_keys,max_val,min_keys,min_val] = get_max_min(seasons)

print 'SEASONS'
print 'the maximum number of crimes in a season was\t', max_val
print 'this occurred in\t\t\t\t', ' and '.join(max_keys)
print 'the minimum number of crimes in a season was\t', min_val
print 'this occurred in\t\t\t\t', ' and '.join(min_keys)
print '------------'

# now get and print all values for months
[max_keys,max_val,min_keys,min_val] = get_max_min(months)

# pretty print month values using pretty_month
print 'MONTHS'
print 'the maximum number of crimes in a month was\t', max_val
print 'this occurred in\t\t\t\t', ' and '.join(pretty_month(max_keys))
print 'the minimum number of crimes in a month was\t', min_val
print 'this occurred in\t\t\t\t', ' and '.join(pretty_month(min_keys))

