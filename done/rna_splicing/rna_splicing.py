import readFile
import useful

def run():
    dna, substrings = inputData()
    #print dna
    exons = useful.removeSubstrings(dna, substrings)
    #print exons
    rna = useful.RNATranslate(exons)
    #print rna
    protein = useful.proteinFromRNA(rna)
    #print protein
    result = protein.rstrip("!")
    print result
    readFile.lineToOutput(result)
    
def inputData():
    list = readFile.listFromInput()
    dnaName = list[0][1:]
    fastaDict, len = readFile.FASTAdictFromInput()
    dna = fastaDict[dnaName]
    del fastaDict[dnaName]
    return dna, fastaDict.values()
