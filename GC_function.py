def count(letter, string):
    letter = letter.upper()
    string = string.upper()
    count_letter = string.count(letter)
    return (count_letter)


#string = 'ATCGATACTA'
#test = count('A', string)
#print test

#GC content function
def GC_content(seq):
    seq = seq.upper()
    #print str(seq)
    seq_length = len(str(seq))
    Gcount = count('C', seq)
    #print Gcount
    Ccount = count('G', seq)
    #print Ccount
    GC_cont = (float(Gcount + Ccount) / seq_length)*100
    return (GC_cont)


string = "ATCGATCATATGACGCGCATATGCATACATCGAGGGGA"

result = GC_content(string)
print result

'''
# recursive solution
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
        







# fibonacci number
def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a

'''




