import readFile

def run():
    FASTADict, length = readFile.FASTAdictFromInput()
    DNA = FASTADict.values()[0]
    RNA = RNATranslate(DNA)
    iDNA = invertDNA(DNA)
    iRNA = RNATranslate(iDNA)
    stringsToProteinDescript = possibleDecryptStrings(RNA) + possibleDecryptStrings(iRNA)
    frames = set()
    for string in stringsToProteinDescript:
        currentFrames = getAllSubstringsFrom('M','!', proteinFromRNA(string))
        frames |= currentFrames
    result = setToPrintableLine(frames)
    print result
    readFile.lineToOutput(result)
    
def RNATranslate(string):
    result = ""
    for i in range(0, len(string)):
        char = string[i]
        if string[i] == 'T':
            char = 'U'
        result += char
    return result

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

def possibleDecryptStrings(string):
    return [ string, string[1:-2], string[2:-1] ]

def getAllSubstringsFrom(start, stop, string):
    stopIndex = -1;
    startIndex = stop;
    store = set()
    for i in range(1, len(string)):
        charIndex = len(string) - i;
        char = string[charIndex]
        if char == stop:
            stopIndex = charIndex
        if char == start and stopIndex > 0:
            store.add(string[charIndex : stopIndex])
    return store

def setToPrintableLine(s):
    line = ""
    for item in s:
        line += item + "\n"
    return line.rstrip("\n")

def invertDNA(string):
    result = ""
    complements = { 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', '\n': '' }
    for i in range(0, len(string)):
        j = len(string) - 1 - i
        char = string[j]
        result += complements[char]
    return result
     
