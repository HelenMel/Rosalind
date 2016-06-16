import readFile

line = readFile.lineFromFile('rosalind_rna.txt')
resultLine = ""
for i in range(0, len(line)):
    char = line[i]
    if line[i] == 'T':
        char = 'U'
    resultLine += char
print resultLine
