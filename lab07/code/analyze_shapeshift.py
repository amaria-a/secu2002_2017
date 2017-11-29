
import pickle

# load the data we saved in scrape_shapeshift.py
entries = pickle.load(open('shapeshift.p','rb'))

# count the number using ethereum as the input currency
num_eth_in = len(filter(lambda x : x['curIn'] == 'ETH', entries))
print 'the number of txs with ethereum in is:', num_eth_in

# count the number using bitcoin as the output currency
num_btc_out = len(filter(lambda x : x['curOut'] == 'BTC', entries))
print 'the number of txs with bitcoin out is:', num_btc_out

# count the number trading zcash to bitcoin
num_zec_btc = len(filter(lambda x : x['curIn'] == 'ZEC' and x['curOut'] == 'BTC', entries))
print 'the number of txs trading zcash to bitcoin is:', num_zec_btc

print '------------'
print '---BONUS----'
print '------------'

# ADD_TO_DICT: incorporate entry into dictionary that might not already have key
# inputs: d (dictionary), key, val (default = 1)
# output: dictionary d with key added
def add_to_dict(d,key,val=1):
    # if the key is there just add the value to the existing one
    if key in d:
        d[key] += val
    # if not then create the key and map it to the value
    else:
        d[key] = val
    return d

# initialize empty dictionaries
dict_in = {}
dict_out = {}

# go through every entry and pull out relevant information
for entry in entries:
    cur_in = entry['curIn']
    cur_out = entry['curOut']
    # cast amount as float so we can perform numeric operations
    in_val = float(entry['amount'])
    # now incorporate input currency and amount into dict_in
    dict_in = add_to_dict(dict_in,cur_in,in_val)
    # and incorporate count of output currency into dict_out
    dict_out = add_to_dict(dict_out,cur_out)

# get the max entry on the input side
max_entry = (None,-10)
for (k,v) in dict_in.items():
    if v > max_entry[1]:
        max_entry = (k,v)

print 'the currency with the most input coins was', max_entry[0]
print 'there were', max_entry[1], 'units put into the service'

# get the max entry on the output side
max_entry = (None,-10)
for (k,v) in dict_out.items():
    if v > max_entry[1]:
        max_entry = (k,v)

print 'the currency used the most as output was', max_entry[0]
print 'it was used', max_entry[1], 'times'
print '------------'

# alternatively, could use fancy keyed max to get entries
max_entry = max(dict_in.items(), key = lambda x : x[1])
print 'the currency with the most input coins was', max_entry[0]
print 'there were', max_entry[1], 'units put into the service'

max_entry = max(dict_out.items(), key = lambda x : x[1])
print 'the currency used the most as output was', max_entry[0]
print 'it was used', max_entry[1], 'times'
