import readFile

def run():
    codonString = readFile.lineFromInput()
    print codonString
    modulo = 1000000
    result = str(totalRNAStrings(codonString, modulo))
    print result
    readFile.lineToOutput(result)

def totalRNAStrings(codonString, modulo):
    RNAdict = readFile.dictWithRNACodon()
    codonsF = valuesFrequencies(RNAdict)
    total = 1
    for char in codonString:
        b = codonsF[char]
        total = multMod(total, b, modulo)
    b = codonsF["Stop"]
    total = multMod(total, b, modulo)
    return total
    

def valuesFrequencies(dict):
    frequencies = {}
    for value in dict.values():
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1
    return frequencies

# multiply two numbers and if result is bigger than mod, returns only
# remainder of the division
def multMod(a, b, n):
    if a == 0:
        a = n
    return (a * b) % n

