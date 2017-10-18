
str1 = 'this module '
str2 = 'is so '
str3 = 'much fun!'

# example of len
print 'answer should be\t9'
print 'answer is\t\t', len(str3)
print '------------'

# example of len
print 'answer should be\t0'
print 'answer is\t\t', len('')
print '------------'

# example of concatenation
print 'answer should be\tthis module is so much fun!'
print 'answer is\t\t', str1 + str2 + str3
print '------------'

# example of indexing
print 'answer should be\tt'
print 'answer is\t\t', str1[0]
print '------------'

# example of indexing
print 'answer should be\tm'
print 'answer is\t\t', str1[5]
print '------------'

# example of indexing out of range
print 'answer should be\toops, that index is out of range'
try:
    print 'answer is\t\t', str3[100]
except:
    print 'oops, that index is out of range'
print '------------'

# example of indexing + concatenation
print 'answer should be\thome'
print 'answer is\t\t', str3[3] + str2[4] + str1[5] + str1[10]
print '------------'

# example of checking if value in string
print 'answer should be\tTrue'
print 'answer is\t\t', 'm' in str1
print '------------'

# example of slicing
print 'answer should be\tmodule'
print 'answer is\t\t', str1[5:11]
print '------------'
    
# example of finding index
print 'answer should be\t1'
print 'answer is\t\t', str1.index('h')
print '------------'

# example of finding index (but for value that isn't there)
print 'answer should be\tthat character is not in the string'
try:
    print 'answer is\t\t', str1.index('y')
except:
    print 'that character is not in the string'
print '------------'

# example of counting occurrences
print 'answer should be\t2'
print 'answer is\t\t', str2.count('s')
print '------------'

# example of counting occurrences
print 'answer should be\t0'
print 'answer is\t\t', str2.count('e')
print '------------'
