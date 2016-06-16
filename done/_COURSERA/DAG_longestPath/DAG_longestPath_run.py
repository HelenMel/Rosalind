import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import readFile
import useful
import directedGraph as dG
import simpleWeightGraphPresener as sWGP
import DAGLongestPath as root

lines = readFile.listFromInput()
sourseS = lines[0]
sinkS = lines[1]
nodes, weights = sWGP.parseAsLineGraphSet(lines[2:])
sourse = dG.nodeFromSet(sourseS, nodes)
sink = dG.nodeFromSet(sinkS, nodes)
length, path = root.longestPath(nodes, weights, sourse, sink)
lengthS = format(length, '.0f')
pathS = "->".join(map(str, path))
result = "\n".join([lengthS, pathS])
print result
readFile.lineToOutput(result)
    
