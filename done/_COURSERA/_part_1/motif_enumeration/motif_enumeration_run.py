import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import readFile
import useful
import motifEnumeration as root

lines = readFile.listFromInput()
k, d = map(int, lines[0].split(" "))
Dna = lines[1:]
result = " ".join(root.motifEnumeration(Dna, k, d))
print result
readFile.lineToOutput(result)
    
