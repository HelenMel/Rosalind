import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import directedGraphString as dGS
import eulerianCycle as eC

lines = readFile.listFromInput()
lenght = lines[0]
Graph = dGS.parseAsGraphSet(lines[1:])
result = dGS.nodesPathToLine(eC.findEulerianPath(Graph))
print lenght
print result
readFile.lineToOutput(result)
    
