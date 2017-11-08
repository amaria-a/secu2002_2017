
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

# read in contents of file, line by line
prefix = '../../data/'
f = open(prefix + 'church_metal_theft.csv','r')

# parse lines into spreadsheet-type format, with each line as dict
spreadsheet = []
for line in f:
    # split line into columns
    columns = line.split(':::')
    row = create_row(columns)
    spreadsheet.append(row)

# KEYWORD_MATCH: used to see if a number of keywords are in a string
# input: keywords (as list) and string 
# output: whether or not *any* of the keywords are in the string
def keyword_match(keywords,mystr):
    match = False
    for word in keywords:
        if word in mystr:
            match = True
            break
    return match

# example of a list comprehension: get just text field from crime data
# use lower to ensure consistency across all entries
texts = [x['text'].lower() for x in spreadsheet]

# all crimes involving lead
lead = filter(lambda x : 'lead' in x, texts)
print 'there are', len(lead), 'crimes involving lead'

# all crimes involving copper
copper = filter(lambda x : 'copper' in x, texts)
print 'there are', len(copper), 'crimes involving copper\n'

print 'LEAD'

# of the lead-based crimes, all crimes involving flashing
lead_flashing = filter(lambda x: 'flashing' in x, lead)
print 'there are', len(lead_flashing), 'crimes involving lead flashing'

# and all lead crimes involving a roof
# this is problematic though because some reports mention climbing onto the
# roof but not stealing part of the roof!
lead_roof = filter(lambda x: 'roof' in x, lead)
print 'there are', len(lead_roof), 'crimes involving lead roofing'

# all lead-based crimes that don't mention either flashing or a roof
lead_other = list(set(lead) - (set(lead_flashing) | set(lead_roof)))
print 'there are', len(lead_other), 'crimes involving lead of neither type\n'

print 'COPPER'

# use all these words to match, as people misspell lightning
copper_words = ['lightning','lightening','conductor']

# all copper-based crimes involving theft of the lightning rod
copper_rod = filter(lambda x : keyword_match(copper_words,x), copper)
print 'there are', len(copper_rod), 'crimes involving the lightning rod'

# all copper-based crimes that don't involve the lightning rod
copper_other = list(set(copper) - set(copper_rod))
print 'there are', len(copper_other), 'crimes not involving the lightning rod'

