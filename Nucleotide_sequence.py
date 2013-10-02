import string
import doctest


class NucleotideSequence:
    '''The NucletideSequence class is meant to handle some DNA or RNA sequence'''
    # general complement dictionnary
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'T',
                   'T': 'A'}
    valid = set(complements)

    def __init__(self, sequence):
        assert  isinstance(sequence, str)
        assert len(sequence) > 0
        self.sequence = sequence
        self.base_counts = {}
        if set(sequence).difference(self.valid) != set():
            raise InvalidBaseException("Invalid base; bases: " + ''.join(set(sequence).difference(self.valid)))
        
    
    def base_count(self, base):
        '''Given a base return the umber of time 
        the base occurs in the sequence'''
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count
        # functon testing
        assert base_count('ATCGATCATA', 'A') == 4
        assert base_count('ATTATAATA', 'G') == 0
        assert base_count('AUUATAATA', 'U') == 2

    def gc_content(self):
        '''Given a sequence return the GC content of that sequence'''
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)
        # functon testing
        assert gc_count('ATATATA') == 0
        assert gc_count('ATATAGGGCC') == 0.5
        assert gc_count('GCCGCGCCCG') == 1


    def reverse_complement(self):
        '''Given a sequence return the reverse compement of that sequence'''
        complements = {'G': 'C',
                       'C': 'G',
                       'A': 'T',
                       'T': 'A'}
        rev_c = ""
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
            
        return rev_c
        # functon testing
        assert gc_count('ATATATA') == 'TATATAT'
        assert gc_count('ATCG') == 'CGAT'
        assert gc_count('ACUGAC') == 'GUCAGU'


# create a new class object based on NucleotideSequence
class DNA_sequence(NucleotideSequence):
    '''Class that inherit from  NucletideSequence class 
    and is meant to handle some DNA sequence'''
    # Exception example
    pass

class RNA_sequence(NucleotideSequence):
    '''Class that inherit from  NucletideSequence class 
    and is meant to handle some RNA sequence, main 
    difference is that the complements dictionnary deals with U'''
    # Exception example
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'U',
                   'U': 'A'}
    #specific assertion to a subclass, redefine the constructor, re import first from the class object
    def __init__(self, sequence):
        NucleotideSequence.__init__(self, sequence)
        assert not 'T' in sequence

# only run this block if we're
# executing this script directly;
# don't run if importing!
if __name__ == "__main__":
    doctest.testmod()

