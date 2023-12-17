DNA_String = ""
CodonSequence = ""
promoter = 'TATAAA'
Stop_Sequence_1 = 'TAA'
Stop_Sequence_2 = 'TAG'
Stop_Sequence_3 = 'TGA'
Current_Codon = ""
Current_Amino_Acid = ""
Stop_Codon = 0
DNA_Sequence = ""
Protein_Sequence = ""
i = 0

DNAsequenceX_file = open("/Users/miltonandrews/Downloads/DNAsequenceX.txt", "r")

#import re

#  By including this line from the FASTA file here, the first liner is being skipped
#  (don't want it in the DNA search string)
DNAsequenceX_file.readline()

while DNAsequenceX_file:
    line  = DNAsequenceX_file.readline().replace('\n', '')
    if line == "":
        break
    DNA_String = DNA_String + line
DNAsequenceX_file.close()

index = DNA_String.find(promoter)
# index = re.findall(promoter, DNA_String)
#print(re.search(promoter, DNA_String))

# Add 10 to index because assignment stipulates that DNA code begins 10 nucleotides after the promoter region ends
index = index + 15

print(index)

while Stop_Codon == 0:
    Current_Codon = DNA_String[index + 1] + DNA_String[index + 2] + DNA_String[index + 3]
    index = index + 3

    # If the first letter of the codon is T
    if (Current_Codon[0] == 'T'):

        # If the second letter of the codon is T
        if (Current_Codon[1] == 'T'):
            # If the third letter if the codon is any of the following then perform assignment
            if (Current_Codon[2] == 'T' or 'C'):
                Current_Amino_Acid = 'F'
            else:
                if (Current_Codon[2] == 'A' or 'G'):
                    Current_Amino_Acid = 'L'

         # If the second letter of the codon is C - Note Codons beginning in TC are always going to be Serine
        if (Current_Codon[1] == 'C'):
            Current_Amino_Acid = 'S'

         # If the second letter of the codon is A
        if (Current_Codon[1] == 'A'):
            if (Current_Codon[2] == 'T' or 'C'):
                Current_Amino_Acid = 'Y'
            else:
                if (Current_Codon[2] == 'A' or 'G'):
                    Stop_Codon = 1

        # If the second letter of the codon is G
        if (Current_Codon[1] == 'G'):
            # If the third letter of the codon is any of the following then perform assignment
            if (Current_Codon[2] == 'G'):
                Current_Amino_Acid = 'W'
            else:
                if (Current_Codon[2] == 'A'):
                    Stop_Codon = 1
                else:
                    Current_Amino_Acid = 'C'

    # If the first letter of the codon is C
    if (Current_Codon[0] == 'C'):

        # If the second letter of the codon is T - Note Codons beginning in CT are always going to be Leucine
        if (Current_Codon[1] == 'T'):
            Current_Amino_Acid = 'L'

        # If the second letter of the codon is C - Note Codons beginning in CC are always going to be Proline
        if (Current_Codon[1] == 'C'):
            Current_Amino_Acid = 'P'

        # If the second letter of the codon is A
        if (Current_Codon[1] == 'A'):
            if (Current_Codon[2] == 'T' or 'C'):
                Current_Amino_Acid = 'H'
            if (Current_Codon[2] == 'A' or 'G'):
                Current_Amino_Acid = 'G'

        # If the second letter of the codon is G - Note Codons beginning in CC are always going to be Argenine
        if (Current_Codon[1] == 'G'):
            Current_Amino_Acid = 'R'

    # If the first letter of the codon is A
    if (Current_Codon[0] == 'A'):

        # If the second letter of the codon is T
        if (Current_Codon[1] == 'T'):
            # If the third letter if the codon is G then it is Methionine otherwise it is always going to be Isoleucine
            if (Current_Codon[2] == 'G'):
                Current_Amino_Acid = 'M'
            else:
                Current_Amino_Acid = 'I'
        # If the second letter of the codon is C - Note Codons beginning in AC are always going to be Threonine
        if (Current_Codon[1] == 'C'):
                Current_Amino_Acid = 'T'

        # If the second letter of the codon is G
        if (Current_Codon[1] == 'G'):
            if (Current_Codon[2] == 'T' or 'C'):
                Current_Amino_Acid = 'S'
            if (Current_Codon[2] == 'A' or 'G'):
                Current_Amino_Acid = 'R'

    # If the first letter of the codon is G
    if (Current_Codon[0] == 'G'):

        # If the second letter of the codon is T - Note Codons beginning in TG are always going to be Valine
        if (Current_Codon[1] == 'T'):
            Current_Amino_Acid = 'V'
        # If the second letter of the codon is C - Note Codons beginning in GC are always going to be Alanine
        if (Current_Codon[1] == 'C'):
            Current_Amino_Acid = 'A'
        # If the second letter of the codon is A
        if (Current_Codon[1] == 'A'):
            if (Current_Codon[2] == 'T' or 'C'):
                Current_Amino_Acid = 'Q'
        # If the second letter of the codon is G - Note Codons beginning in GG are always going to be Glycine
        if (Current_Codon[1] == 'G'):
            Current_Amino_Acid = 'G'






    # These two lines are specific to the stop codon and will be replaced when I complete the above assignments
    if (Current_Codon[0] == 'T' and Current_Codon[1] == 'G' and Current_Codon[2] == 'A'):
        Stop_Codon = 1

    print(Current_Amino_Acid)
    print(Current_Codon)
    Protein_Sequence = Protein_Sequence + Current_Amino_Acid
    DNA_Sequence = DNA_Sequence + Current_Codon

print(DNA_String)
print(index)
print(DNA_Sequence)
print(Protein_Sequence)

i = 1
while i != (len(DNA_Sequence) + 1):
    if (i % 70) == 0:
        print()
    else:
        print(DNA_Sequence[i-1],end="")
    i = i + 1

print()

i = 1
while i != (len(Protein_Sequence) + 1):
    if (i % 70) == 0:
        print()
    else:
        print(Protein_Sequence[i-1],end="")
    i = i + 1
