import readFile

def run():
    linesOfLines = readFile.listFromInput()
    print linesOfLines
    output = []
    print "total " + str(len(linesOfLines[1]))
    occurrence(linesOfLines[0], linesOfLines[1], 0, output)
    result = outputLine(output)
    print result
    readFile.lineToOutput(result)
    
def occurrence(substring, string, i, output):
    if len(string) < len(substring):
        return
    if substring == string[:len(substring)]:
        print "append " + str(i) 
        output.append(i)
    i += 1
    shortenString = string[1:]
    occurrence(substring, shortenString, i, output)
    
def outputLine(output):
    line = ""
    for i in output:
        line += str(i) + " "
    return line.rstrip(" ")
