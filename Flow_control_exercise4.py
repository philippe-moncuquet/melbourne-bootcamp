import re

filename = "/home/swc_trainee/bootcamp/day1/uniprot_sprot.fasta"
file = open(filename)

count = 0

for line in file:
    if str(line).startswith('>') and 'OS=Homo sapiens' in line:
        #print line
        count += 1

file.close()

print count
