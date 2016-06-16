import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import gibbsSampler as root

lines = readFile.listFromInput()
k, t, N = map(int, lines[0].split(" "))
Dna = lines[1:]
result = "\n".join(root.repeatedGibbsSampler(Dna, k, t, N, 50))
print result
readFile.lineToOutput(result)
    
