
mystr = 'secu2002'

mylen = 0
for x in mystr:
    mylen = mylen + 1

print 'length of string should be\t8'
print 'length of string is\t\t', mylen
print '------------'

mylist = [1,2,3,4,5]

# do both sum and len in same loop
mylen = 0
mysum = 0
for x in mylist:
    # add 1 to length (one more element)
    mylen += 1
    # add item value to sum
    mysum += x

print 'length of list should be\t5'
print 'length of list is\t\t', mylen
print '------------'

print 'sum of list should be\t15'
print 'sum of list is\t\t', mysum
print '------------'

# now iterate using ranges instead
r = range(0,len(mylist))
mysum = 0
for i in r:
    mysum += mylist[i]

print 'sum of list should be\t15'
print 'sum of list is\t\t', mysum
print '------------'

r = range(0,len(mylist),2)
other_sum = 0
for i in r:
    other_sum += mylist[i]

print 'sum of every other element should be\t9'
print 'sum of every other element is\t\t', other_sum
print '------------'
