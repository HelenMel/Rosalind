import readFile
import parse
import useful
import clumpFinding

listOfLines = readFile.listFromInput()
Genome = listOfLines[0]
k, L, t = map(int, listOfLines[1].split(" "))
print Genome, k, t, L
result = " ".join(clumpFinding.betterClumpFinding(Genome, k, t, L))
print result
readFile.lineToOutput(result)
    
