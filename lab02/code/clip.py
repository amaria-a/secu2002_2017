
# first clip string with just first and last three characters
mystr = 'friday is the start of the weekend'
newstr = mystr[0:3] + mystr[-3:]

print 'answer should be\tfriend'
print 'answer is\t\t', newstr
print '------------'

# now swap first three characters of two strings and concatenate
mystr1 = 'sarah'
mystr2 = 'enrico'
# so first three characters of string 2 + remaining ones of string 1
newstr1 = mystr2[:3] + mystr1[3:]
# then first three characters of string 1 + remaining ones of string 2
newstr2 = mystr1[:3] + mystr2[3:]
# now concatenate with space in between
newcatstr = newstr1 + ' ' + newstr2

print 'answer should be\tenrah sarico'
print 'answer is\t\t', newcatstr
