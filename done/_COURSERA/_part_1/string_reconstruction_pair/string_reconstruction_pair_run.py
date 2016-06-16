import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import directedGraphGapped as dGG
import eulerianCycle as eC

lines = readFile.listFromInput()
k, d = map(int, lines[0].split(" "))
Graph = dGG.parseAsGraphSet(lines[1:])
print Graph
result = ""
path = eC.findEulerianPath(Graph)
print path
result = dGG.nodesPathToLine(path, k, d)
#print lenght
print result
readFile.lineToOutput(result)
    
