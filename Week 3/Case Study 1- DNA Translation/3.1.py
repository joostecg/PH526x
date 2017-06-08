
#not preferred method
inputfile = "dna.txt"
f = open(inputfile, "r")
seq = f.read()
seq = seq.replace("\n","")
seq = seq.replace("\r","")
print(seq)

#preferred method for opening file

inputfile = "dna.txt"

def read_seq(inputfile):
    """Reads and returns the input sequence with special characters removed"""
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n","")
    seq = seq.replace("\r","")
    return seq

def translate(seq):
    """Translate a string containing a necleotide sequence into a string containing the corresponding sequence if aminoacids. Nucleotides are translated in triplets using the table dictionary: each amino acid is encoded with a string of length 1."""
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    #check that the sequence is divisible by 3
    protein = ""
    if len(seq) % 3 == 0:
        #loop over the sequence
        for i in range(0, len(seq), 3):
            #extract a single codon
            codon = seq[i : i+3]
            protein += table[codon]
            #lookup codon and store result
    return protein


prt = read_seq("protein.txt")
dna = read_seq("dna.txt")

len(dna) % 3
translate(dna[20:935])
prt

translate(dna[20:935]) == prt       #check whether dna matches protein download

print(seq)

translate(dna[20:938])[:-1]     #alternative to just remove last character from returned string instead of sending one sequence less
prt

translate(dna[20:938])[:-1] == translate(dna[20:935])


translate("ATA")
translate("AAA")

#testing

table["CAA"]

table["CCT"]

table["GCC"]

7/3
6/3
7%3 #modula oprator
6%3
138%13
len(seq) % 3
for s in seq:
    print(s)
seq[0:3]
seq[3:6]
range(0,11,3)
list(range(0,11,3))

#Questions
inputfile = "dnaQ3.txt"
f = open(inputfile, "r")
seqQ3 = f.read()

seqQ3 = seqQ3.replace("\n","")
seqQ3 = seqQ3.replace("\r","")

seq[40:50]