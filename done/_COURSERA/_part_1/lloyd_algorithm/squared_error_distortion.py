import math
import sys

import readFile
import parse
import pointsDistances
import useful


inputLine = readFile.lineFromInput()
k, m, Centers, Data = parse.parse(inputLine)
print "result"
result = pointsDistances.squaredErrorDistortion(Data, Centers)
print result
readFile.lineToOutput(result)
    
