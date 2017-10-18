
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
list3 = [True,False]

# example of len
print 'answer should be\t2'
print 'answer is\t\t', len(list3)
print '------------'

# example of len
print 'answer should be\t0'
print 'answer is\t\t', len([])
print '------------'

# example of concatenation
print "answer should be\t[1, 2, 3, 4, 'a', 'b', 'c', 'd', True, False]"
print 'answer is\t\t', list1 + list2 + list3
print '------------'

# example of indexing
print 'answer should be\t1'
print 'answer is\t\t', list1[0]
print '------------'

# example of indexing
print 'answer should be\t4'
print 'answer is\t\t', list1[3]
print '------------'

# example of indexing (out of range)
print 'answer should be\toops, that index is out of range'
try:
    print 'answer is\t\t', list3[100]
except:
    print 'oops, that index is out of range'
print '------------'

# example of checking if value in list
print 'answer should be\tTrue'
print 'answer is\t\t', 3 in list1
print '------------'

# example of slicing
print 'answer should be\t[1, 2]'
print 'answer is\t\t', list1[0:2]
print '------------'

# example of finding index
print 'answer should be\t0'
print 'answer is\t\t', list2.index('a')
print '------------'

# example of counting occurrences
print 'answer should be\t0'
print 'answer is\t\t', list1.count('a')
print '------------'

# notice that with the operations below, we are just printing the same list
# every time, so in contrast to the operations above it is really the value 
# of the list itself that is changing 

# example of append
list1.append(5)
print 'answer should be\t[1, 2, 3, 4, 5]'
print 'answer is\t\t', list1
print '------------'

# example of remove
list1.remove(1)
print 'answer should be\t[2, 3, 4, 5]'
print 'answer is\t\t', list1
print '------------'

# example of setting value at index
list1[0] = 6
print 'answer should be\t[6, 3, 4, 5]'
print 'answer is\t\t', list1
print '------------'

# example of extend
list1.extend(list3)
print 'answer should be\t[6, 3, 4, 5, True, False]'
print 'answer is\t\t', list1
print '------------'

# example of sort
list1.sort()
# if you're curious about this, it's because roughly False = 0 and True = 1
print 'answer should be\t[False, True, 3, 4, 5, 6]'
print 'answer is\t\t', list1
print '------------'

# example of reverse
list2.reverse()
print "answer should be\t['d', 'c', 'b', 'a']"
print 'answer is\t\t', list2
print '------------'


