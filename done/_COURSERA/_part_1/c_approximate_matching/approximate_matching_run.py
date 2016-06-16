import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import readFile
import parse
import useful
import approximateMatching

lines = readFile.listFromInput()
Pattern = lines[0]
Genome = lines[1]
maxDist = int(lines[2])
print Pattern, Genome, maxDist
intResult = approximateMatching.approximate_matching(Pattern,Genome,maxDist)
result = useful.listStringToPrint([str(x) for x in intResult])
print result
readFile.lineToOutput(result)
    
