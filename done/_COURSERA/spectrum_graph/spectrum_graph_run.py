import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
from bio_4 import spectrum_graph as core

lines = readFile.listFromInput()
nodes = core.parseLineToNodes(lines[0])
edges, nodes = core.nodesToSpectrumGraph(nodes)
result = "\n".join(core.edgeGraphToAnswer(edges))
print result
readFile.lineToOutput(result)
    
