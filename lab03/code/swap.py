
# with these lines commented in, values should be same before and after
#x = 10
#y = 5
# with these lines commented in, values should swap
x = 5
y = 7
print 'x is', x, 'and y is', y

# swap values is x is less than y 
if x < y:
    # swap using intermediate tmp variable
    tmp = x
    x = y
    y = tmp

print 'now x is', x, 'and y is', y
