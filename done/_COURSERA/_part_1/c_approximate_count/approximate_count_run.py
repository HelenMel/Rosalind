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
maxDistance = int(lines[2])
Pattern = "AA"
Genome = "TACGCATTACAAAGCACA"
maxDistance = 1
print Pattern, Genome, maxDistance
result = approximateMatching.approximate_count(Pattern, Genome, maxDistance)
print result
readFile.lineToOutput(result)
    
