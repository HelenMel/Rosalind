import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import directedGraph as dG
import eulerianCycle as eC

lines = readFile.listFromInput()
Graph = dG.parseAsGraphSet(lines)
result = dG.nodesPathToLine(eC.findEulerianPath(Graph))
print result
readFile.lineToOutput(result)
    
