import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import readFile
from bio_3 import middle_edge as mE

lines = readFile.listFromInput()
v = lines[0]
w = lines[1]
center, next, length = mE.middle_edge_run(v, w)
result = "("+ str(center[0]) + ", "+ str(center[1]) + ") ("+ str(next[0])+", "+str(next[1])+")"
print result
readFile.lineToOutput(result)
    
