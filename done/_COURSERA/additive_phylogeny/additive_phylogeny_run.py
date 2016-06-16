import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
import useful
import additivePhylogeny as aP

sys.setrecursionlimit(10000) # 10000 is an example, try with different values
lines = readFile.listFromInput()
n = int(lines[0])
matrix = lines[1:]
D = []
[D.append(map(int, line.split(" "))) for line in matrix]
Tree, Weights = aP.additivePhylogenyRun(D, n)
result = aP.presentWeights(Weights)
print result
readFile.lineToOutput(result)
    
