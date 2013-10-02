sequence = "GTGTACGTACGGACAACTAGCAACACGTGCACAC"
is_rna = False
if 'U' in sequence:
    is_rna = True
sequence = sequence.replace('U', 'T')
g = sequence.count('G')
a = sequence.count('A')
t = sequence.count('T')
c = sequence.count('C')
base_counts = {'G': g, 'A': a, 'T': t, 'C': c}
total_length = g+a+t+c
gc_content = (g+c)/float(total_length) * 100
base_counts['U'] = base_counts['T']
del base_counts['T']
print gc_content
