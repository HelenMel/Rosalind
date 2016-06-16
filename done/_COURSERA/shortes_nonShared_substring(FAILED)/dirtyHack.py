
alphabet = [ 'C', 'T', 'G', 'A']

def compareTwo(Text1, Text2):
    startedLength  = 2
    while startedLength < 10:
        Lines = generateAllPossibleItemsWithLength(startedLength)
        for line in Lines:
            if line in Text1:
                if line not in Text2:
                    return line
        startedLength += 1
    return None


def generateAllPossibleItemsWithLength(length):
    Lines = [ "" ]
    for i in xrange(0, length):
        Lines = addAnyValueAtEnd(Lines)
    return Lines

def addAnyValueAtEnd(lines):
    newLines = []
    for line in lines:
        for letter in alphabet:
            newLines.append(line + letter)
    return newLines