import sys
import string

sentence = "Apple, banana, and cherry."
count = 0


myset = set(sentence.lower())
print myset

lowercase = set(string.lowercase)
#uppercase = set(string.uppercase)

lo

for i in range(0,len(myset)):
    letter = myset[i]
    if letter == "," or letter == ".":
        print "symbol found"
    else:
        count += 1
        
print count

# get your input sentence
import sys
import string
my_sentence = "Jenny, Perry, and Winifred are the names of three cats."
my_sentence = my_sentence.lower()
characters = set(my_sentence)
alphabet = string.lowercase
letters = characters.intersection(alphabet)
print len(letters)
