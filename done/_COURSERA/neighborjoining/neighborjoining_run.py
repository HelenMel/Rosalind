import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
import useful
import neighborjoining as nj

lines = readFile.listFromInput()
n = int(lines[0])
Dist = [[float(y) for y in x.split("\t")] for x in lines[1:]]
answer = nj.neighbor_joining_run(Dist, n)
def presentEdge(edge):
    return str(edge.node1.base) + "->" + str(edge.node2.base) + ":" + format(abs(edge.weight), '.2f')
result = "\n".join([presentEdge(edge) for edge in answer])
print result
readFile.lineToOutput(result)
    
