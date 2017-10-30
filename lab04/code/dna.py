
# REVERSE
# input:    a strand of dna (as string)
# output:   the reverse strand (as string)
def reverse(dna):
    # store reverse as list to allow mutability, use dummy values initially
    reverse_list = ['0'] * len(dna)
    # now fill in dummy values by going through dna forwards and filling in
    # reverse_list backwards
    for i in range(1,len(dna)+1):
        reverse_list[-i] = dna[i-1]
    # now form list into string
    reverse_dna = ''.join(reverse_list)
    return reverse_dna

# COMPLEMENT  
# input:    a strand of dna (as string)
# output:   the complement strand (as string)
def complement(dna,base_mapping):
    comp_dna = ''
    for char in dna:
        if char in base_mapping.keys():
            comp_dna += base_mapping[char]
        else:
            return 'error: non-dna character in string'
    return comp_dna

# REVERSE_COMPLEMENT
# input:    a strand of dna (as string)
# output:   the reverse complement (as string)
def reverse_complement(dna,base_mapping):
    # store reverse as list to allow mutability, use dummy values initially
    reverse_list = ['0'] * len(dna)
    # now fill in dummy values by going through dna forwards and filling in
    # reverse_list backwards
    for i in range(1,len(dna)+1):
        char = dna[i-1]
        if char in base_mapping.keys():
            reverse_list[-i] = base_mapping[char]
        else:
            return 'error: non-dna character in string'
    reverse_comp_dna = ''.join(reverse_list)
    return reverse_comp_dna

#a -> t, t -> a, g -> c, c -> g
base_mapping = {'a' : 't', 't' : 'a', 'g' : 'c', 'c' : 'g'}

# generate some strands of dna to test
dna1 = 'atgcaattgcaattcgtagc'
dna2 = 'ggbtca'
dna3 = 'atatccgtagctt'
dna4 = ''
dna5 = 'atttgcagcaattgcaatatggcatattgcatcgtattaacgc'

print 'dna strand is\t\t', dna1
print 'reverse should be\t', dna1[::-1]
print 'reverse is\t\t', reverse(dna1)
print '------------'

# hardcoded expected results obtained by doing it by hand
print 'complement should be\t', 'tacgttaacgttaagcatcg'
print 'complement is\t\t', complement(dna1,base_mapping)
print '------------'

# hardcoded expected results obtained from reverse-complement.com
print 'reverse complement should be\t', 'gctacgaattgcaattgcat'
print 'reverse complement is\t\t', reverse_complement(dna1,base_mapping)
print '------------'

print 'dna strand is\t\t', dna2
print 'reverse should be\t', dna2[::-1]
print 'reverse is\t\t', reverse(dna2)
print 'complement is\t\t', complement(dna2,base_mapping)
print 'reverse complement is\t', reverse_complement(dna2,base_mapping)
print '------------'

print 'dna strand is\t\t', dna3
print 'reverse should be\t', dna3[::-1]
print 'reverse is\t\t', reverse(dna3)
print 'complement is\t\t', complement(dna3,base_mapping)
print 'reverse complement is\t', reverse_complement(dna3,base_mapping)
print '------------'

print 'dna strand is\t\t', dna4
print 'reverse should be\t', dna4[::-1]
print 'reverse is\t\t', reverse(dna4)
print 'complement is\t\t', complement(dna4,base_mapping)
print 'reverse complement is\t', reverse_complement(dna4,base_mapping)
print '------------'

print 'dna strand is\t\t', dna5
print 'reverse should be\t', dna5[::-1]
print 'reverse is\t\t', reverse(dna5)
print 'complement is\t\t', complement(dna5,base_mapping)
print 'reverse complement is\t', reverse_complement(dna5,base_mapping)
print '------------'


