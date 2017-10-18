
# set up a mapping from bases to their complements (a <-> t, g <-> c)
# these need to be ordered in the same way in order to enable mapping
# could also try to do this with list of pairs
base_str = 'atgc'
comp_str = 'tacg'

# generate some strand of dna
dna = 'atgcaattgcaattcgtagc'

############
# REVERSE  #
############
# store reverse as list to allow mutability, use dummy values initially
reverse_list = ['0'] * len(dna)
# now fill in dummy values by going through dna forwards and filling in
# reverse_list backwards
for i in range(1,len(dna)+1):
    reverse_list[-i] = dna[i-1]

# now form list into string
reverse_dna = ''.join(reverse_list)

# use fancy syntax to check answer
print 'reverse should be\t', dna[::-1]
print 'reverse is\t\t', reverse_dna
print '------------'

###############
# COMPLEMENT  #
###############
comp_dna = ''
for char in dna:
    # find the index of char in base_str
    i = base_str.index(char)
    # now find the associated char in the mapped string comp_str 
    # (this is why we needed the same order)
    comp_dna += comp_str[i]

# hardcoded expected results obtained by doing it by hand
print 'complement should be\t', 'tacgttaacgttaagcatcg'
print 'complement is\t\t', comp_dna
print '------------'

#######################
# REVERSE COMPLEMENT  #
#######################
# store reverse as list to allow mutability, use dummy values initially
reverse_list = ['0'] * len(dna)
# now fill in dummy values by going through dna forwards and filling in
# reverse_list backwards
for i in range(1,len(dna)+1):
    char = dna[i-1]
    j = base_str.index(char)
    reverse_list[-i] = comp_str[j]

reverse_comp_dna = ''.join(reverse_list)

# hardcoded expected results obtained from reverse-complement.com
print 'reverse complement should be\t', 'gctacgaattgcaattgcat'
print 'reverse complement is\t\t', reverse_comp_dna
