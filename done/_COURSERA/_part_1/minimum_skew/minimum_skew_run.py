import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import readFile
import parse
import useful
import minimumSkew

Genome = readFile.lineFromInput()
Genome = "CATTCCAGTACTTCGATGATGGCGTGAAGA"
print Genome
result = useful.listStringToPrint(minimumSkew.minimum_skew(Genome))
print result
readFile.lineToOutput(result)
    
