import readFile


def run():
    fileInput = 'input.txt'
    fileOutput = 'output.txt'
    line = readFile.lineFromFile(fileInput)
    result = ""
    complements = { 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', '\n': '' }
    for i in range(0, len(line)):
        j = len(line) - 1 - i
        char = line[j]
        result += complements[char]
    print result
    readFile.lineToFile(fileOutput, result)
