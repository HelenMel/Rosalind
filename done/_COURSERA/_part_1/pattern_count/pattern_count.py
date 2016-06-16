import readFile
import useful

def run():
    listOfLines = readFile.listFromInput()
    print listOfLines
    text = listOfLines[0]
    pattern = listOfLines[1]
    result = patternCount(text, pattern)
    print result
    readFile.lineToOutput(result)
    
def patternCount(text, pattern):
    count = 0
    lastElement = len(text) - len(pattern) + 1
    for i in range(0, lastElement):
        end = i + len(pattern)
        if text[i: end] == pattern:
            count += 1
    return count
