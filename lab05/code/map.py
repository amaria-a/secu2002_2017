
# FAHRENHEIT
# input: temp (as int or float)
# output: temp in fahrenheit (as float)
def fahrenheit(temp):
    return (float(9)/5)*temp + 32

# standard temperatures over a week
temps = [15,20,19,16,17,24,24]
print map(fahrenheit, temps)

