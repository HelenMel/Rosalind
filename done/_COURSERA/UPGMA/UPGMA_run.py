import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
import useful
import UPGMA

lines = readFile.listFromInput()
n = int(lines[0])
Dist = [[float(y) for y in x.split(" ")] for x in lines[1:]]
print Dist
answer = UPGMA.UPGMA(Dist, n)
def presentEdge(edge):
    return str(edge.node1.base) + "->" + str(edge.node2.base) + ":" + format(abs(edge.weight), '.3f')
result = "\n".join([presentEdge(edge) for edge in answer])
print result
readFile.lineToOutput(result)
    
