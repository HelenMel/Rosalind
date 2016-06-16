import readFile

def run():
    linesOfLines = readFile.lineFromInput()
    n = int(linesOfLines[0])
    combinations = set()
    combine(alphabet(n), "", combinations)
    result = formattedAnswer(n, combinations)
    readFile.lineToOutput(result)

def alphabet(count):
    alphabet = set()
    for i in range(1, (count + 1)):
        alphabet.add(str(i))
    return alphabet
    
def combine(alphabet, prefix, output):
    if len(alphabet) == 0:
        output.add(prefix)
    for char in alphabet:
        shortenAlphabet = list(alphabet)
        shortenAlphabet.remove(char)
        newPrefix = prefixPlusChar(prefix, char)
        combine(shortenAlphabet, newPrefix, output)
        
def prefixPlusChar(prefix, char):
    if len(prefix) == 0:
        return char
    else:
        return prefix + " "  + char

def formattedAnswer(n, combinations):
    line = str(len(combinations)) + "\n"
    for combination in combinations:
        line += combination  + "\n"
    return line.rstrip("\n")
    
