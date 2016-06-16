import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import parse
import useful
import directedGraphBinary as dGB
import eulerianCycle as eC

lines = readFile.listFromInput()
k = int(lines[0])
Graph = dGB.generateBinaryGraphSet(k)
print Graph
result = dGB.nodesPathToLine(eC.findEulerianCycle(Graph), k)
print result
readFile.lineToOutput(result)
    
