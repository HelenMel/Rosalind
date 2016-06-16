import readFile

def run():
    linesOfLines = readFile.lineFromInput()
    result = proteinFromRNA(linesOfLines)
    print result
    readFile.lineToOutput(result)

def proteinFromRNA(line):
    codon_table = readFile.dictWithRNACodon()
    expected_protein_len = len(line) / 3
    protein = ""
    while(len(line) > 0):
        rna = line[:3]
        codon = codon_table[rna]
        if codon != 'Stop':
            protein += codon
        line = line[3:]
    print "protein length " + str(len(protein)) + "should be equal to " + str(expected_protein_len)
    return protein
     
    
