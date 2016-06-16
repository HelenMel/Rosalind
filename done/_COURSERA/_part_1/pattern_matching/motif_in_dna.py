import re
import readFile

def run():
    linesOfLines = readFile.listFromInput()
    print linesOfLines
    print "total " + str(len(linesOfLines[1]))
    output = occurrence(linesOfLines[0], linesOfLines[1])
    result = outputLine(output)
    print result
    readFile.lineToOutput(result)
    
def occurrence(substring, string):
    output = []
    it = re.finditer(substring, string)
    for match in it:
        output.append(match.start())
        output += additional_substring(substring, string, match.start())
    return output

def additional_substring(substring, string, acc):
    output = []
    end = acc + len(substring)
    acc += 1
    for i in range(acc, end):
        end = i + len(substring)
        if string[ i: end ] == substring:
            output.append(i)
    return output


def outputLine(output):
    line = ""
    for i in output:
        line += str(i) + " "
    return line.rstrip(" ")
