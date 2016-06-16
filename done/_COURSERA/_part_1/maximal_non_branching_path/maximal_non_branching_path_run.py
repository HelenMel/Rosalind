import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import directedGraph as dG
import maximalNonBranchingPath as root

lines = readFile.listFromInput()
Graph = dG.parseAsGraphSet(lines)
paths = root.maximalNonBranchingPath(Graph)
result = "\n".join([dG.nodesPathToLine(p) for p in paths])
print result
readFile.lineToOutput(result)
 