
# BIN_FIND: find entry in data matching date using binary search
# input: date (as datetime object), data (as row of dicts)
# output: (any) entry in data with that date
def bin_find(date,data):
    # used to count number of times through loop
    count = 0
    # we start by splitting the list down the middle
    first = 0
    last = len(data) - 1
    while first <= last:
        middle = (first + last) / 2
        entry = data[middle]
        # check if value at middle is what we want
        if date == entry['date']:
            print 'number of times with binary search is\t', count
            return entry
        else:
            # check if value at middle is above what we want
            if date < entry['date']:
                # if so then the date of the pivot is too late, 
                # need to look in first half of list
                last = middle - 1
            else:
                # otherwise we need to look in second half of list because 
                # the date of the pivot is too early 
                first = middle + 1
        count += 1
    print 'number of times with binary search is\t', count
    # if we got to the end then we didn't find any matching entry
    return None

# LIN_FIND: find entry in data matching date pattern using linear search
# input: date (as datetime object), data (as list of dicts)
# output: (any) entry in data with that date range
def lin_find(date,data):
    count = 0
    # go through entries in order, return first one that matches 
    for entry in data:
        if date == entry['date']:
            print 'number of times with linear search is\t', count
            return entry
        # as an optimization, if we've passed where entry should be then we
        # know it's not there so can just return None
        if date < entry['date']:
            print 'number of times with linear search is\t', count
            return None
        count += 1
    print 'number of times with linear search is\t', count
    # if nothing matches then return None
    return None

