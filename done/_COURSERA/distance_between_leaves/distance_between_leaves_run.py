import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
import useful
import directedWeightGraphPresener as dWGP
import distanceBetweenLeaves as dBL

lines = readFile.listFromInput()
n = int(lines[0])
nodes, weights = dWGP.parseAsGraphSet(lines[1:])
answer = dBL.distancesWithNodesAndWeights(nodes, weights, n)
result = dBL.presentNodesWeights(answer, nodes, n)
print result
readFile.lineToOutput(result)
    
