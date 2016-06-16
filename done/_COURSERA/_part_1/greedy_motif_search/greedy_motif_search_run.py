import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import readFile
import useful
import greedyMotifSearch as root

lines = readFile.listFromInput()
k, t = map(int, lines[0].split(" "))
Dna = lines[1:]
result = useful.lineFromCollection(root.greedyMotifSearch(Dna, k, t))
print result
readFile.lineToOutput(result)
    
