import readFile
import parse
import useful
import deBruijnGraph

k, Text = readFile.listFromInput()
print k, Text
result = useful.lineFromObjectsCollection(deBruijnGraph.deBruijn(Text, int(k)))
print result
readFile.lineToOutput(result)
    
