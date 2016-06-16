import readFile
import parse
import useful
import composition

k, Text = readFile.listFromInput()
print k, Text
result = useful.lineFromCollection(composition.composition(Text, int(k)))
print result
readFile.lineToOutput(result)
    
