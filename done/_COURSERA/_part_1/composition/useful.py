import readFile
import decimal

def listToPrint(list):
  return "\n".join(" ".join(format(y, '.3f') for y in rows) for rows in list)

def listStringToPrint(list):
    return " ".join(list)

def lineFromCollection(s):
    return "\n".join(s)

def RNATranslate(string):
    #result = ""
    #for i in range(0, len(string)):
    #    char = string[i]
    #    if string[i] == 'T':
    #        char = 'U'
    #    result += char
    #return result
    return string.replace('T', 'U')


def proteinFromRNA(string):
    codon_table = readFile.dictWithRNACodon()
    expected_protein_len = len(string) / 3
    protein = ""
    while(len(string) > 0):
        rna = string[:3]
        if len(rna) < 3:
             string = ""
             continue
        codon = codon_table[rna]
        if codon == 'Stop':
            protein += "!"
        else :            
            protein += codon
        string = string[3:]
    return protein

def invertDNA(string):
    result = ""
    complements = { 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', '\n': '' }
    for i in range(0, len(string)):
        j = len(string) - 1 - i
        char = string[j]
        result += complements[char]
    return result

def removeSubstrings(s, substrings):
    result = s
    for substring in substrings:
        result = result.replace(substring, '')
    return result
    
