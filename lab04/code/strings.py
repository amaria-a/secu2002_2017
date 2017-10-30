
# MY_JOIN: used to join a list of strings into one
# input: a separator mysep (string) and a list of strings mylist
# output: a string consisting of the strings in mylist separated by mysep
def my_join(mysep,mylist):
    to_return = ''
    # start with empty string and add elements + mysep
    for x in mylist:
        to_return = to_return + x + mysep
    # now we have an extra separator at the end, just slice it off
    # have to be careful though in case mysep is empty string!
    # example of the ternary operator
    to_return = to_return[:-len(mysep)] if len(mysep) > 0 else to_return
    return to_return

print '------------'
print 'TESTS FOR MY_JOIN'

print 'should be\t', ''.join(['a','b','c'])
print 'is\t\t', my_join('',['a','b','c'])

print 'should be\t', ''.join([])
print 'is\t\t', my_join('',[])

print 'should be\t', 'sarah'.join(['a','b','c'])
print 'is\t\t', my_join('sarah',['a','b','c'])

print 'should be\t', '\t'.join(['a','b','c'])
print 'is\t\t', my_join('\t',['a','b','c'])

# MY_JOIN2: used to join a list of strings into one
# input: a separator mysep (string) and a list of strings mylist
# output: a string consisting of the strings in mylist separated by mysep
def my_join2(mysep,mylist):
    to_return = ''
    # start with empty string and add elements + mysep until last one
    for x in mylist[:-1]:
        to_return = to_return + x + mysep
    # now we just need to add last element manually (with no separator)
    to_return = to_return + mylist[-1]
    return to_return

print '------------'
print 'TESTS FOR MY_JOIN2'

print 'should be\t', ''.join(['a','b','c'])
print 'is\t\t', my_join2('',['a','b','c'])

print 'should be\t', ''.join([])
print 'is\t\t', my_join('',[])

print 'should be\t', 'sarah'.join(['a','b','c'])
print 'is\t\t', my_join2('sarah',['a','b','c'])

print 'should be\t', '\t'.join(['a','b','c'])
print 'is\t\t', my_join('\t',['a','b','c'])

# SORT_STRING
# input:     a string mystr
# output:    the alphabetized version of mystr
def sort_string(mystr):
    mylist = list(mystr)
    mylist.sort()
    return ''.join(mylist)

print '------------'
print 'TESTS FOR SORT_STRING'

print 'should be\tabcde'
print 'is\t\t', sort_string('edcab')

print 'should be\t'
print 'is\t\t', sort_string('')

print 'should be\t12345abcdef'
print 'is\t\t', sort_string('abcdef12345')
