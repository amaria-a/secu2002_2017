
# set up some conversions to plug in later
kms_in_mile = 1.61
kgs_in_stone = 6.35

# how far is a marathon in km?
num_miles = 26.2
num_kms = kms_in_mile * num_miles
print 'should be around 42'
print 'answer is exactly', num_kms
print '------------'

# how hot is it when americans say its 108?
num_fahr = 108
num_celsius = (num_fahr - 32) * (5.0/9)
print 'should be around 42'
print 'answer is exactly', num_celsius
print '------------'

# how much do i weigh in kg if i'm 6 st 9 lbs?
num_stone = 6
num_lbs = 9
total_stone = num_stone + (num_lbs / 14.0)
num_kgs = total_stone * kgs_in_stone
print 'should be around 42'
print 'answer is exactly', num_kgs
print '------------'

# 800 meters in 2 minutes 10 seconds -> minutes per mile?
num_km = 800 / 1000.0
num_min = 2
num_sec = 10
total_min = num_min + (num_sec / 60.0)
num_miles = num_km / kms_in_mile
# this gives us the decimal minutes per mile
raw_min_per_mile = (total_min / num_miles)
# could express pace as decimal number of minutes but nicer as mins : secs
raw_sec_per_mile = (total_min / num_miles) * 60
# minutes is the quotient part of the division
min_per_mile = int(raw_sec_per_mile // 60)
# seconds is the remainder
sec_per_mile = int(raw_sec_per_mile % 60)
pace_str = str(min_per_mile) + ':' + str(sec_per_mile)
print 'should be a pace of around 4:20 per mile'
print 'answer is a pace of exactly', pace_str, 'per mile'
