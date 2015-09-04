# Sample:
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC


f = open("rosalind_dna.txt", "r")
line = f.readline()

result = {}
for letter in line:
    if letter in result:
        result[letter] += 1
    else:
        result[letter] = 1

print "{0} {1} {2} {3}".format(result["A"], result["C"], result["G"], result["T"])
