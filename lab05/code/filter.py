
# LOOP_FILTER
# input: a numeric list mylist and a number n
# output: a list containing all elements in mylist greater than n
def loop_filter(mylist,n):
    filtered_list = []
    for x in mylist:
        if x > n:
            filtered_list.append(x)
    return filtered_list

print '------------'
print 'TESTS FOR LOOP_FILTER'

print 'should be\t[]'
print 'is\t\t', loop_filter([],1)

print 'should be\t[]'
print 'is\t\t', loop_filter([1,2,3,4,5],5)

print 'should be\t[7, 8, 9]'
print 'is\t\t', loop_filter([1,2,3,7,8,9],6)

# LAMBDA_FILTER
# input: a numeric list mylist and a number n
# output: a list containing all elements in mylist greater than n
def lambda_filter(mylist,n):
    return filter(lambda x : x > n, mylist)

print '------------'
print 'TESTS FOR LAMBDA_FILTER'

print 'should be\t[]'
print 'is\t\t', lambda_filter([],5)

print 'should be\t[]'
print 'is\t\t', lambda_filter([1,2,3,4,5],5)

print 'should be\t[7, 8, 9]'
print 'is\t\t', lambda_filter([1,2,3,7,8,9],5)

