import readFile
import parse
import useful
import lloydAlgorithm

listOfLines = readFile.listFromInput()
print listOfLines
Data, k, m = parse.parse(listOfLines)
Centers = lloydAlgorithm.lloydAlgorithm(Data,k)
print "result"
result = useful.listToPrint(Centers)
print result
readFile.lineToOutput(result)
    
