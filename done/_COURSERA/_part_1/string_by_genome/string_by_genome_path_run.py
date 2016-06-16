import readFile
import parse
import useful
import genomePath

listOfLines = readFile.listFromInput()
result = genomePath.stringByGenomePath(listOfLines)
print result
readFile.lineToOutput(result)
    
