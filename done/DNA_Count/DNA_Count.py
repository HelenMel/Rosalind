print "MEEE"
fileName = 'rosalind_dna.txt'

f = open(fileName, 'r')
line = f.read()
f.close()

letters = {}

for char in line:
    if char in letters:
        letters[char] += 1
    else:
        letters[char] = 1;

print letters
