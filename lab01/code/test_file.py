
## THESE ARE EXERCISES COPIED OVER FROM THE INTERACTIVE INTERPRETER ##

# basic numeric operations
4 + 1 #will return 5
10 - 8 #will return 2
10 * 10 #will return 100

# long type
4314813413471839471 * 5475841975184314 
#will return 23627236404577409575254243845257894L

# int division
4 / 2 #will return 2
10 / 5 #will return 2
10 / 4 #will return 2

# float type
float(10) / 4 #will return 2.5
float(10) / float(4) #will return 2.5
10.0 / 4 #will return 2.5
10 / 4.0 #will return 2.5

# ^ operator
10 ^ 2 #will return 8
7 ^ 3 #will return 4

# ** operator
10 ** 2 #will return 100
7 ** 3 #will return 343

# order of operations
4 + 6 * 5 #will return 34
(4 + 6) * 5 #will return 50

# types
type(5) #will return <type 'int'>
type(2.5) #will return <type 'float'>
isinstance(10 / 4, int) #will return True
type(isinstance(5, int)) #will return <type 'bool'>

# assignment
x = 5
x #will return 5
type(x) #will return <type 'int'>
x + 1 #will return 6
x - 3 #will return 2

# assignment, part ii
x = 5
y = 6
x = y + 3
x #will return 9
y = y - 5
y #will return 1
x + y #will return 10

